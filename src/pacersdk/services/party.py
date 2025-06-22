"""
Service for performing party searches via the PACER Case Locator API.
"""

from logging import getLogger
from typing import Generator, Callable, cast, List, Optional
from urllib.parse import urlencode

from ..models.query import PartySearchCriteria
from ..models.reports import ReportList
from ..models.sort import PartyField
from ..session import PCLSession

logger = getLogger(__name__)


class PartyService:
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
        Initialize the PartyService.

        :param token_provider: Callable returning a valid CSO token.
        :param config: Dictionary with base API URL.
        :param token: Optional pre-fetched token for session reuse.
        """
        self.session = PCLSession(token_provider, config, 1, token)

    def search(
        self,
        criteria: PartySearchCriteria,
        page: int = 0,
        sort: Optional[List[PartyField]] = None,
    ) -> ReportList:
        """
        Perform a party search.

        :param criteria: PartySearchCriteria with optional filters.
        :param page: Zero-based page number of results to fetch.
        :param sort: Optional list of sort field/direction pairs.
        :return: ReportList containing search results.
        """
        logger.debug("Searching for parties with request: %s", criteria)
        query = {"page": page}
        if isinstance(sort, list):
            query["sort"] = [f"{s['field']},{s['order']}" for s in sort]
        params = urlencode(query, doseq=True)
        msg = self.session.post(
            path=f"/pcl-public-api/rest/parties/find?{params}",
            body=criteria,
        )
        return cast(ReportList, msg)

    def search_all(
        self,
        criteria: PartySearchCriteria,
        sort: Optional[List[PartyField]] = None,
    ) -> Generator[ReportList, None, None]:
        """
        Perform a paginated party search and yield results page-by-page.

        This method iterates over all available pages of results based on
        the initial search criteria.

        :param criteria: The party search criteria including filters such as court ID, date range, etc.
        :type criteria: PartySearchCriteria
        :param sort: Optional list of fields to sort the results by.
        :type sort: list[PartyField] or None
        :yield: A ReportList dictionary containing case results for a single page.
        :rtype: Generator[ReportList, None, None]
        """
        current_page = 0
        while True:
            report_list = self.search(criteria=criteria, page=current_page, sort=sort)
            yield report_list
            page_info = report_list.get("pageInfo", {})
            total_pages = page_info.get("totalPages", 1)
            if current_page + 1 < total_pages:
                current_page += 1
            else:
                break
