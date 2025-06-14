"""
Service for performing case searches via the PACER Case Locator API.
"""

from typing import Callable
from typing import cast
from typing import List
from typing import Optional
urllib.parse import urlencode

from ..models.case import CaseSearchRequest
from ..models.case import CaseSearchResponse
from ..models.sort import SortableCaseField
from ..session import PCLSession


class CaseSearchService:
    """
    Provides access to the case search API endpoint.
    """

    def __init__(
        self,
        token_provider: Callable[[], str],
        config: dict,
        token: Optional[str] = None,
    ) -> None:
        """
        Initialize the CaseSearchService.

        :param token_provider: Callable returning a valid CSO token.
        :param config: Dictionary with base API URL.
        :param token: Optional pre-fetched token for session reuse.
        """
        self.session = PCLSession(token_provider, config, token)

    def search(
        self,
        criteria: CaseSearchRequest,
        page: int = 0,
        sort: Optional[List[SortableCaseField]] = None,
    ) -> CaseSearchResponse:
        """
        Perform a case search.

        :param criteria: CaseSearchRequest with optional filters.
        :param page: Zero-based page number of results to fetch.
        :param sort: Optional list of sort field/direction pairs.
        :return: CaseSearchResponse containing search results.
        """
        query = {"page": page}
        if isinstance(sort, list):
            query["sort"] = [f"{s['field']},{s['order']}" for s in sort]
        params = urlencode(query, doseq=True)
        msg = self.session.post(
            path=f"/pcl-public-api/rest/cases/find?{params}",
            body=criteria,
        )
        return cast(CaseSearchResponse, msg)
