from unittest import main, TestCase
from unittest.mock import MagicMock, patch

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

    def test_search_all_paginates_correctly(self):
        def mock_search(criteria, page, sort=None):
            return {"pageInfo": {"totalPages": 3}, "page": page}

        self.service.search = MagicMock(side_effect=mock_search)
        results = list(self.service.search_all(criteria={}))
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0]["page"], 0)
        self.assertEqual(results[1]["page"], 1)
        self.assertEqual(results[2]["page"], 2)
