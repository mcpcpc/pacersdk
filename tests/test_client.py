from unittest import main
from unittest import TestCase
from unittest.mock import MagicMock

from pacersdk.client import PCLClient
from pacersdk.models.query import CourtCaseSearchCriteria
from pacersdk.models.query import PartySearchCriteria
from pacersdk.models.reports import ReportInfo
from pacersdk.models.reports import ReportList


class TestPCLClient(TestCase):
    def setUp(self):
        self.mock_authenticator = MagicMock()
        self.mock_authenticator.get_token.return_value = "mock_token"
        self.mock_case_search = MagicMock()
        self.mock_party_search = MagicMock()
        self.mock_batch_case_search = MagicMock()
        self.mock_batch_party_search = MagicMock()
        self.client = PCLClient(
            username="user",
            password="pass",
            authenticator=self.mock_authenticator,
            case_search=self.mock_case_search,
            party_search=self.mock_party_search,
            batch_case_search=self.mock_batch_case_search,
            batch_party_search=self.mock_batch_party_search,
        )

    def test_search_cases(self):
        criteria = CourtCaseSearchCriteria()
        self.client.search_cases(criteria)
        self.mock_case_search.search.assert_called_once_with(
            criteria, page=0, sort=None
        )

    def test_search_parties(self):
        criteria = PartySearchCriteria()
        self.client.search_parties(criteria)
        self.mock_party_search.search.assert_called_once_with(
            criteria, page=0, sort=None
        )

    def test_submit_batch_case(self):
        criteria = CourtCaseSearchCriteria()
        self.client.submit_batch_case(criteria)
        self.mock_batch_case_search.submit.assert_called_once_with(criteria)

    def test_get_batch_party_status(self):
        self.client.get_batch_party_status("report_id")
        self.mock_batch_party_search.status.assert_called_once_with("report_id")

    def test_logout(self):
        self.client.logout()
        self.mock_authenticator.logout.assert_called_once()

    def test_delete_batch_case(self):
        self.client.delete_batch_case("123")
        self.mock_batch_case_search.delete.assert_called_once_with("123")

    def test_list_batch_party_jobs(self):
        self.client.list_batch_party_jobs()
        self.mock_batch_party_search.listall.assert_called_once()


if __name__ == "__main__":
    main()
