from unittest import main, TestCase
from unittest.mock import patch

from pacersdk.services.case import CaseService


class TestCaseService(TestCase):
    def setUp(self):
        self.service = CaseService(
            lambda: "mock_token",
            {"pclapiurl": "http://example.com"},
            "mock_token",
        )

    @patch("pacersdk.services.case.PCLSession.post")
    def test_search(self, mock_post):
        self.service.search("request")
        mock_post.assert_called_once()

    @patch("pacersdk.services.case.PCLSession.post")
    def test_search_with_sort(self, mock_post):
        sort = [
            {"field": "caseYear", "order": "DESC"},
            {"field": "caseType", "order": "ASC"},
        ]
        self.service.search("request", sort=sort)
        mock_post.assert_called_once_with(
            path="/pcl-public-api/rest/cases/find?page=0&sort=caseYear%2CDESC&sort=caseType%2CASC",
            body="request",
        )
