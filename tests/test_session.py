from io import BytesIO
from unittest import main, TestCase
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

from pacersdk.session import PCLSession


class TestPCLSession(TestCase):
    def setUp(self):
        self.token = "test-token"
        self.token_provider = lambda: self.token
        self.config = {"pclapiurl": "https://example.com"}
        self.session = PCLSession(
            token_provider=self.token_provider, config=self.config, max_retries=1
        )

    @patch("pacersdk.session.urlopen")
    def test_request_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b'{"message": "ok"}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response
        req = self.session.get("/test")  # uses _request internally
        self.assertEqual(req["message"], "ok")

    @patch("pacersdk.session.urlopen")
    def test_request_204_no_content(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 204
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response
        req = self.session.get("/no-content")
        self.assertEqual(req["status"], "No Content")

    @patch("pacersdk.session.urlopen")
    def test_request_unauthorized_then_success(self, mock_urlopen):
        http_error = HTTPError(
            url="https://example.com/retry",
            code=401,
            msg="Unauthorized",
            hdrs=None,
            fp=BytesIO(b"Unauthorized"),
        )
        success = MagicMock()
        success.status = 200
        success.read.return_value = b'{"message": "retried"}'
        success.__enter__.return_value = success
        mock_urlopen.side_effect = [http_error, success]
        response = self.session.get("/retry")
        self.assertEqual(response["message"], "retried")

    @patch("pacersdk.session.urlopen")
    def test_request_unauthorized_exceeds_retry(self, mock_urlopen):
        http_error = HTTPError(
            url="https://example.com/fail",
            code=401,
            msg="Unauthorized",
            hdrs=None,
            fp=BytesIO(b"Unauthorized"),
        )
        mock_urlopen.side_effect = [http_error, http_error]
        with self.assertRaises(RuntimeError) as context:
            self.session.get("/fail")
        self.assertIn("HTTP 401 Error", str(context.exception))

    @patch.object(PCLSession, "_request")
    def test_get_calls_request(self, mock_request):
        mock_request.return_value = {"ok": True}
        result = self.session.get("/test")
        self.assertEqual(result["ok"], True)
        mock_request.assert_called_once()

    @patch.object(PCLSession, "_request")
    def test_post_calls_request(self, mock_request):
        mock_request.return_value = {"posted": True}
        result = self.session.post("/submit", {"data": 123})
        self.assertEqual(result["posted"], True)
        mock_request.assert_called_once()

    @patch.object(PCLSession, "_request")
    def test_delete_calls_request(self, mock_request):
        mock_request.return_value = {"deleted": True}
        result = self.session.delete("/remove")
        self.assertEqual(result["deleted"], True)
        mock_request.assert_called_once()


if __name__ == "__main__":
    main()
