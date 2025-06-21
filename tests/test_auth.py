from io import BytesIO
from unittest import main, TestCase
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

from pacersdk.auth import Authenticator


class TestAuthenticator(TestCase):
    def setUp(self):
        self.config = {"authenticationurl": "https://example.com"}
        self.token = "mocked_token"

    @patch("pacersdk.auth.urlopen")
    def test_get_token_success_without_otp(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"nextGenCSO": "mocked_token"}'
        mock_urlopen.return_value.__enter__.return_value = mock_response
        auth = Authenticator("user", "pass", self.config)
        token = auth.get_token()
        self.assertEqual(token, "mocked_token")
        self.assertEqual(auth.token, "mocked_token")

    @patch("pacersdk.auth.totp", return_value="123456")
    @patch("pacersdk.auth.urlopen")
    def test_get_token_success_with_otp(self, mock_urlopen, mock_totp):
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"nextGenCSO": "mocked_token"}'
        mock_urlopen.return_value.__enter__.return_value = mock_response
        auth = Authenticator("user", "pass", self.config, secret="BASE32SECRET")
        token = auth.get_token()
        self.assertEqual(token, "mocked_token")
        mock_totp.assert_called_once_with("BASE32SECRET")

    @patch("pacersdk.auth.urlopen")
    def test_logout_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_urlopen.return_value.__enter__.return_value = mock_response
        auth = Authenticator("user", "pass", self.config)
        auth.token = self.token
        auth.logout()
        self.assertIsNone(auth.token)

    @patch("pacersdk.auth.urlopen")
    def test_logout_failure_with_message(self, mock_urlopen):
        mock_urlopen.side_effect = HTTPError(
            url="http://example.com",
            code=400,
            msg="error",
            hdrs=None,
            fp=BytesIO(b"Bad Request"),
        )
        auth = Authenticator("user", "pass", self.config)
        auth.token = self.token
        with self.assertRaises(Exception) as context:
            auth.logout()
        self.assertIn("Bad Request", str(context.exception))
        self.assertIsNone(auth.token)


if __name__ == "__main__":
    main()
