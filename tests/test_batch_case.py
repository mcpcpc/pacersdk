from unittest import main, TestCase
from unittest.mock import patch

from pacersdk.services.batch_case import BatchCaseService


class TestBatchCaseService(TestCase):
    def setUp(self):
        self.service = BatchCaseService(
            lambda: "mock_token",
            {"pclapiurl": "http://example.com"},
            "mock_token",
        )

    @patch("pacersdk.services.batch_case.PCLSession.post")
    def test_submit(self, mock_post):
        self.service.submit("request")
        mock_post.assert_called_once()

    @patch("pacersdk.services.batch_case.PCLSession.get")
    def test_status(self, mock_get):
        self.service.status(1)
        mock_get.assert_called_once()

    @patch("pacersdk.services.batch_case.PCLSession.get")
    def test_download(self, mock_get):
        self.service.download(1)
        mock_get.assert_called_once()

    @patch("pacersdk.services.batch_case.PCLSession.delete")
    def test_delete(self, mock_delete):
        self.service.delete(1)
        mock_delete.assert_called_once()

    @patch("pacersdk.services.batch_case.PCLSession.get")
    def test_listall(self, mock_get):
        self.service.listall()
        mock_get.assert_called_once()
