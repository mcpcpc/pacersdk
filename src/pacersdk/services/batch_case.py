"""
Service for submitting and managing batch case searches.
"""

from typing import Callable
from typing import cast
from typing import Optional

from ..models.query import CourtCaseSearchCriteria
from ..models.reports import ReportInfo
from ..models.reports import ReportList
from ..session import PCLSession


class BatchCaseService:
    """
    Provides access to the batch case search API endpoint.
    """

    def __init__(
        self,
        token_provider: Callable[[], str],
        config: dict,
        token: Optional[str] = None,
    ) -> None:
        """
        Initialize the BatchCaseSearchService.

        :param token_provider: Callable returning a valid CSO token.
        :param config: Dictionary with API endpoint URLs.
        :param token: Optional pre-fetched token.
        """
        self.session = PCLSession(token_provider, config, 1, token)

    def submit(self, criteria: CourtCaseSearchCriteria) -> ReportInfo:
        """
        Submit a batch case search job.

        :param criteria: CourtCaseSearchCriteria with optional filters.
        :return: ReportInfo object.
        """
        return cast(
            ReportInfo,
            self.session.post("/pcl-public-api/rest/cases/download", criteria),
        )

    def status(self, report_id: str) -> ReportList:
        """
        Query the status of a batch case search job.

        :param report_id: The report identifier.
        :return: ReportList object.
        """
        return cast(
            ReportList,
            self.session.get(f"/pcl-public-api/rest/cases/download/status/{report_id}"),
        )

    def download(self, report_id: str) -> ReportList:
        """
        Download results of a completed batch case search job.

        :param report_id: The report identifier.
        :return: ReportList object.
        """
        return cast(
            ReportList,
            self.session.get(f"/pcl-public-api/rest/cases/download/{report_id}"),
        )

    def delete(self, report_id: str) -> dict:
        """
        Delete a submitted batch case report by ID.

        :param report_id: Batch report identifier.
        :return: Response status or message.
        """
        return self.session.delete(f"/pcl-public-api/rest/cases/reports/{report_id}")

    def listall(self) -> ReportList:
        """
        Retrieve a list of all current batch case jobs.

        :return: ReportList object.
        """
        return cast(ReportList, self.session.get("/pcl-public-api/rest/cases/reports"))
