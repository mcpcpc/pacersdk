"""
Service for performing party searches via the PACER Case Locator API.
"""

from typing import Callable
from typing import cast
from typing import List
from typing import Optional
from urllib.parse import urlencode

from ..models.party import PartySearchRequest
from ..models.party import PartySearchResponse
from ..models.sort import SortablePartyField
from ..session import PCLSession


class PartySearchService:
    """
    Provides access to the party search API endpoint.
    """

    def __init__(
        self,
        token_provider: Callable[[], str],
        config: dict,
        token: Optional[str] = None,
    ) -> None:
        """
        Initialize the PartySearchService.

        :param token_provider: Callable returning a valid CSO token.
        :param config: Dictionary with base API URL.
        :param token: Optional pre-fetched token for session reuse.
        """
        self.session = PCLSession(token_provider, config, token)

    def search(
        self,
        criteria: PartySearchRequest,
        page: int = 0,
        sort: Optional[List[SortablePartyField]] = None,
    ) -> PartySearchResponse:
        """
        Perform a party search.

        :param criteria: PartySearchRequest with optional filters.
        :param page: Zero-based page number of results to fetch.
        :param sort: Optional list of sort field/direction pairs.
        :return: PartySearchResponse containing search results.
        """
        query = {"page": page}
        if isinstance(sort, list):
            query["sort"] = [f"{s['field']},{s['order']}" for s in sort]
        params = urlencode(query, doseq=True)
        msg = self.session.post(
            path=f"/pcl-public-api/rest/parties/find?{params}",
            body=criteria,
        )
        return cast(PartySearchResponse, msg)
