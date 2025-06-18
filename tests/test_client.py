from unittest import main
from unittest import TestCase
from unittest.mock import patch

from pacersdk.client import PCLClient


class TestPCLClient(TestCase):
    def setUp(self):
        self.patcher = patch("pacersdk.client.Authenticator")
        mock_authenticator = self.patcher.start()
        mock_authenticator.get_token.return_value = "token"

    def tearDown(self):
        self.patcher.stop()

    @patch("pacersdk.client.CaseSearchService.search")
    def test_search_cases(self, mock_search):
        PCLClient("user", "pass").search_cases("criteria")
        mock_search.assert_called_once_with("criteria", page=0, sort=None)

    @patch("pacersdk.client.PartySearchService.search")
    def test_search_parties(self, mock_search):
        PCLClient("user", "pass").search_parties("criteria")
        mock_search.assert_called_once_with("criteria", page=0, sort=None)

    @patch("pacersdk.client.BatchCaseSearchService.submit")
    def test_submit_batch_case(self, mock_submit):
        PCLClient("user", "pass").submit_batch_case("request")
        mock_submit.assert_called_once_with("request")

    @patch("pacersdk.client.BatchPartySearchService.submit")
    def test_submit_batch_party(self, mock_submit):
        PCLClient("user", "pass").submit_batch_party("request")
        mock_submit.assert_called_once_with("request")

    @patch("pacersdk.client.BatchCaseSearchService.status")
    def test_get_batch_case_status(self, mock_status):
        PCLClient("user", "pass").get_batch_case_status("report1")
        mock_status.assert_called_once_with("report1")

    @patch("pacersdk.client.BatchPartySearchService.status")
    def test_get_batch_party_status(self, mock_status):
        PCLClient("user", "pass").get_batch_party_status("party_report1")
        mock_status.assert_called_once_with("party_report1")

    @patch("pacersdk.client.BatchCaseSearchService.delete")
    def test_delete_batch_case(self, mock_delete):
        PCLClient("user", "pass").delete_batch_case("report1")
        mock_delete.assert_called_once_with("report1")

    @patch("pacersdk.client.BatchPartySearchService.delete")
    def test_delete_batch_party(self, mock_delete):
        PCLClient("user", "pass").delete_batch_party("party_report1")
        mock_delete.assert_called_once_with("party_report1")

    @patch("pacersdk.client.BatchCaseSearchService.listall")
    def test_list_batch_case_jobs(self, mock_listall):
        PCLClient("user", "pass").list_batch_case_jobs()
        mock_listall.assert_called_once()

    @patch("pacersdk.client.BatchPartySearchService.listall")
    def test_list_batch_party_jobs(self, mock_listall):
        PCLClient("user", "pass").list_batch_party_jobs()
        mock_listall.assert_called_once()


if __name__ == "__main__":
    main()
