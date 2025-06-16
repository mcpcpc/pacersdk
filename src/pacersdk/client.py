"""
Client interface to the PACER Case Locator API.
"""

from .auth import Authenticator
from .config import get_config
from .services.case_search import CaseSearchService
from .services.party_search import PartySearchService
from .services.batch_case_search import BatchCaseSearchService
from .services.batch_party_search import BatchPartySearchService
from .models.case import CaseSearchRequest
from .models.case import CaseSearchResponse
from .models.party import PartySearchRequest
from .models.party import PartySearchResponse
from .models.batch import BatchCaseRequest
from .models.batch import BatchCaseResponse
from .models.batch import BatchPartyRequest
from .models.batch import BatchPartyResponse


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
        token_provider = self.authenticator.get_token
        token = self.authenticator.get_token()
        self.case_search = CaseSearchService(token_provider, self.config, token)
        self.party_search = PartySearchService(token_provider, self.config, token)
        self.batch_case_search = BatchCaseSearchService(
            token_provider, self.config, token
        )
        self.batch_party_search = BatchPartySearchService(
            token_provider, self.config, token
        )

    def logout(self):
        """
        Log out of the session and revoke the token.
        """
        self.authenticator.logout()

    def search_cases(
        self, criteria: CaseSearchRequest, page: int = 0, sort: dict = None
    ) -> CaseSearchResponse:
        """
        Perform a case search.

        :param criteria: Dictionary of case search filters.
        :param page: Optional zero-based page number.
        :param sort: Optional list of sort field/direction pairs.
        :return: CaseSearchResponse containing matching results.
        """
        return self.case_search.search(criteria, page=page, sort=sort)

    def search_parties(
        self, criteria: PartySearchRequest, page: int = 0, sort: dict = None
    ) -> PartySearchResponse:
        """
        Perform a party search.

        :param criteria: Dictionary of party search filters.
        :param page: Optional zero-based page number.
        :param sort: Optional list of sort field/direction pairs.
        :return: PartySearchResponse containing matching results.
        """
        return self.party_search.search(criteria, page=page, sort=sort)

    def submit_batch_case(self, request: BatchCaseRequest) -> BatchCaseResponse:
        """
        Submit a batch case search.

        :param request: BatchCaseRequest with case search filters.
        :return: BatchCaseResponse containing the report ID.
        """
        return self.batch_case_search.submit(request)

    def submit_batch_party(self, request: BatchPartyRequest) -> BatchPartyResponse:
        """
        Submit a batch party search.

        :param request: BatchPartyRequest with party search filters.
        :return: BatchPartyResponse containing the report ID.
        """
        return self.batch_party_search.submit(request)

    def get_batch_case_status(self, report_id: str) -> dict:
        """
        Retrieve the status of a batch case search.

        :param report_id: The report identifier.
        :return: Dictionary with batch job status.
        """
        return self.batch_case_search.status(report_id)

    def get_batch_party_status(self, report_id: str) -> dict:
        """
        Retrieve the status of a batch party search.

        :param report_id: The report identifier.
        :return: Dictionary with batch job status.
        """
        return self.batch_party_search.status(report_id)

    def get_batch_case_results(self, report_id: str) -> dict:
        """
        Download results for a completed batch case search.

        :param report_id: The report identifier.
        :return: Dictionary containing search results.
        """
        return self.batch_case_search.download(report_id)

    def get_batch_party_results(self, report_id: str) -> dict:
        """
        Download results for a completed batch party search.

        :param report_id: The report identifier.
        :return: Dictionary containing search results.
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

    def list_batch_case_jobs(self) -> dict:
        """
        List all current batch case jobs.

        :return: Dictionary containing all current batch results.
        """
        return self.batch_case_search.listall()

    def list_batch_party_jobs(self) -> dict:
        """
        List all current batch party jobs.

        :return: Dictionary containing all current batch results.
        """
        return self.batch_party_search.listall()

