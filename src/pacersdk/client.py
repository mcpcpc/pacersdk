"""
Client interface to the PACER Case Locator API.
"""

from .auth import Authenticator
from .config import get_config
from .models.query import CourtCaseSearchCriteria
from .models.query import PartySearchCriteria
from .models.reports import ReportList
from .models.reports import ReportInfo
from .services.case_search import CaseSearchService
from .services.party_search import PartySearchService
from .services.batch_case_search import BatchCaseSearchService
from .services.batch_party_search import BatchPartySearchService


class PCLClient:
    """
    Entry point for interacting with the PACER Case Locator API.
    """

    def __init__(
        self,
        username: str,
        password: str,
        secret: str = None,
        environment: str = "prod",
        client_code: str = None,
        redaction: bool = False,
        config_path: str = None,
    ) -> None:
        """
        Initialize the API client.

        :param username: PACER system user ID.
        :param password: PACER system password.
        :param secret: Optional TOTP base32 secret for MFA accounts.
        :param environment: Environment key ("qa" or "prod").
        :param client_code: Optional client code for court searches.
        :param redaction: Optional flag to indicate redaction compliance.
        :param config_path: Optional path to a custom JSON config file.
        """
        self.config = get_config(environment, config_path)
        self.authenticator = Authenticator(
            username=username,
            password=password,
            secret=secret,
            config=self.config,
            client_code=client_code,
            redaction=redaction,
        )
        self.token_provider = self.authenticator.get_token
        token = self.token_provider()
        self.case_search = CaseSearchService(self.token_provider, self.config, token)
        self.party_search = PartySearchService(self.token_provider, self.config, token)
        self.batch_case_search = BatchCaseSearchService(
            self.token_provider, self.config, token
        )
        self.batch_party_search = BatchPartySearchService(
            self.token_provider, self.config, token
        )

    def logout(self) -> None:
        """
        Log out of the session and revoke the token.
        """
        return self.authenticator.logout()

    def search_cases(
        self, criteria: CourtCaseSearchCriteria, page: int = 0, sort: dict = None
    ) -> ReportList:
        """
        Perform a case search.

        :param criteria: Dictionary of case search filters.
        :param page: Optional zero-based page number.
        :param sort: Optional list of sort field/direction pairs.
        :return: ReportList containing matching results.
        """
        return self.case_search.search(criteria, page=page, sort=sort)

    def search_parties(
        self, criteria: PartySearchCriteria, page: int = 0, sort: dict = None
    ) -> ReportList:
        """
        Perform a party search.

        :param criteria: Dictionary of party search filters.
        :param page: Optional zero-based page number.
        :param sort: Optional list of sort field/direction pairs.
        :return: ReportList containing matching results.
        """
        return self.party_search.search(criteria, page=page, sort=sort)

    def submit_batch_case(self, criteria: CourtCaseSearchCriteria) -> ReportInfo:
        """
        Submit a batch case search.

        :param criteria: CourtCaseSearchCriteria with case search filters.
        :return: ReportInfo containing the report ID.
        """
        return self.batch_case_search.submit(criteria)

    def submit_batch_party(self, criteria: PartySearchCriteria) -> ReportInfo:
        """
        Submit a batch party search.

        :param criteria: PartySearchCriteria with party search filters.
        :return: ReportInfo containing the report ID.
        """
        return self.batch_party_search.submit(criteria)

    def get_batch_case_status(self, report_id: str) -> ReportList:
        """
        Retrieve the status of a batch case search.

        :param report_id: The report identifier.
        :return: ReportList with batch job status.
        """
        return self.batch_case_search.status(report_id)

    def get_batch_party_status(self, report_id: str) -> ReportList:
        """
        Retrieve the status of a batch party search.

        :param report_id: The report identifier.
        :return: ReportList with batch job status.
        """
        return self.batch_party_search.status(report_id)

    def get_batch_case_results(self, report_id: str) -> ReportList:
        """
        Download results for a completed batch case search.

        :param report_id: The report identifier.
        :return: ReportList containing search results.
        """
        return self.batch_case_search.download(report_id)

    def get_batch_party_results(self, report_id: str) -> ReportList:
        """
        Download results for a completed batch party search.

        :param report_id: The report identifier.
        :return: ReportList containing search results.
        """
        return self.batch_party_search.download(report_id)

    def delete_batch_case(self, report_id: str) -> dict:
        """
        Delete a batch case search request by report ID.

        :param report_id: The report identifier.
        :return: Dictionary with deletion status.
        """
        return self.batch_case_search.delete(report_id)

    def delete_batch_party(self, report_id: str) -> dict:
        """
        Delete a batch party search request by report ID.

        :param report_id: The report identifier.
        :return: Dictionary with deletion status.
        """
        return self.batch_party_search.delete(report_id)

    def list_batch_case_jobs(self) -> ReportList:
        """
        List all current batch case jobs.

        :return: ReportList containing all current batch results.
        """
        return self.batch_case_search.listall()

    def list_batch_party_jobs(self) -> ReportList:
        """
        List all current batch party jobs.

        :return: ReportList containing all current batch results.
        """
        return self.batch_party_search.listall()
