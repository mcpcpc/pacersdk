"""
Service for submitting and managing batch party searches.
"""

from logging import getLogger
from typing import Callable, cast, Optional

from ..models.query import PartySearchCriteria
from ..models.reports import ReportInfo, ReportList
from ..session import PCLSession

logger = getLogger(__name__)


class BatchPartyService:
    """
    Provides access to the batch party search API endpoint.
    """

    def __init__(
        self,
        token_provider: Callable[[], str],
        config: dict,
        token: Optional[str] = None,
    ) -> None:
        """
        Initialize the BatchPartyService.

        :param token_provider: Callable returning a valid CSO token.
        :param config: Dictionary with API endpoint URLs.
        :param token: Optional pre-fetched token.
        """
        self.session = PCLSession(token_provider, config, 1, token)

    def submit(self, criteria: PartySearchCriteria) -> ReportInfo:
        """
        Submit a batch party search job.

        :param criteria: PartySearchCriteria with optional filters.
        :return: ReportInfo object.
        """
        logger.debug("Submitting batch party search job")
        return cast(
            ReportInfo,
            self.session.post("/pcl-public-api/rest/parties/download", criteria),
        )

    def status(self, report_id: str) -> ReportList:
        """
        Query the status of a batch party search job.

        :param report_id: The report identifier.
        :return: ReportList object.
        """
        logger.debug("Checking status for report ID: %s", report_id)
        return cast(
            ReportList,
            self.session.get(
                f"/pcl-public-api/rest/parties/download/status/{report_id}"
            ),
        )

    def download(self, report_id: str) -> ReportList:
        """
        Download results of a completed batch party search job.

        :param report_id: The report identifier.
        :return: ReportList object.
        """
        logger.debug("Downloading report with ID: %s", report_id)
        return cast(
            ReportList,
            self.session.get(f"/pcl-public-api/rest/parties/download/{report_id}"),
        )

    def delete(self, report_id: str) -> dict:
        """
        Delete a submitted batch party report by ID.

        :param report_id: Batch report identifier.
        :return: Response status or message.
        """
        logger.debug("Deleting report with ID: %s", report_id)
        return self.session.delete(f"/pcl-public-api/rest/parties/reports/{report_id}")

    def listall(self) -> ReportList:
        """
        Retrieve a list of all current batch party jobs.

        :return: ReportList object.
        """
        logger.debug("Listing all batch party reports")
        return cast(
            ReportList, self.session.get("/pcl-public-api/rest/parties/reports")
        )
