"""
Service for performing case searches via the PACER Case Locator API.
"""

from logging import getLogger
from typing import Generator, Callable, cast, List, Optional
from urllib.parse import urlencode

from ..models.query import CourtCaseSearchCriteria
from ..models.reports import ReportList
from ..models.sort import CaseField
from ..session import PCLSession

logger = getLogger(__name__)


class CaseService:
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
        Initialize the CaseService.

        :param token_provider: Callable returning a valid CSO token.
        :param config: Dictionary with base API URL.
        :param token: Optional pre-fetched token for session reuse.
        """
        self.session = PCLSession(token_provider, config, 1, token)

    def search(
        self,
        criteria: CourtCaseSearchCriteria,
        page: int = 0,
        sort: Optional[List[CaseField]] = None,
    ) -> ReportList:
        """
        Perform a case search.

        :param criteria: CourtCaseSearchCriteria with optional filters.
        :param page: Zero-based page number of results to fetch.
        :param sort: Optional list of sort field/direction pairs.
        :return: ReportList containing search results.
        """
        logger.debug("Searching for cases with request: %s", criteria)
        query = {"page": page}
        if isinstance(sort, list):
            query["sort"] = [f"{s['field']},{s['order']}" for s in sort]
        params = urlencode(query, doseq=True)
        msg = self.session.post(
            path=f"/pcl-public-api/rest/cases/find?{params}",
            body=criteria,
        )
        return cast(ReportList, msg)

    def search_all(
        self,
        criteria: CourtCaseSearchCriteria,
        sort: Optional[List[CaseField]] = None,
    ) -> Generator[ReportList, None, None]:
        """
        Perform a paginated case search and yield results page-by-page.

        This method iterates over all available pages of results based on
        the initial search criteria.

        :param criteria: The case search criteria including filters such as court ID, date range, etc.
        :type criteria: CourtCaseSearchCriteria
        :param sort: Optional list of fields to sort the results by.
        :type sort: list[CaseField] or None
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
