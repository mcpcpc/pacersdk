"""
Service for submitting and managing batch party searches.
"""

from typing import Callable
from typing import cast
from typing import Optional

from ..session import PCLSession
from ..models.batch import BatchPartyResponse
from ..models.batch import BatchPartyRequest


class BatchPartySearchService:
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
        Initialize the BatchPartySearchService.

        :param token_provider: Callable returning a valid CSO token.
        :param config: Dictionary with API endpoint URLs.
        :param token: Optional pre-fetched token.
        """
        self.session = PCLSession(token_provider, config, 1, token)

    def submit(self, request: BatchPartyRequest) -> BatchPartyResponse:
        """
        Submit a batch party search job.

        :param request: A batch party search request model.
        :return: A BatchPartyResponse dictionary.
        """
        return cast(
            BatchPartyResponse,
            self.session.post("/pcl-public-api/rest/parties/download", request),
        )

    def status(self, report_id: str) -> dict:
        """
        Query the status of a batch party search job.

        :param report_id: The report identifier.
        :return: JSON status response.
        """
        return self.session.get(
            f"/pcl-public-api/rest/parties/download/status/{report_id}"
        )

    def download(self, report_id: str) -> dict:
        """
        Download results of a completed batch party search job.

        :param report_id: The report identifier.
        :return: JSON response containing party data.
        """
        return self.session.get(f"/pcl-public-api/rest/parties/download/{report_id}")

    def delete(self, report_id: str) -> dict:
        """
        Delete a submitted batch party report by ID.

        :param report_id: Batch report identifier.
        :return: Response status or message.
        """
        return self.session.delete(f"/pcl-public-api/rest/parties/reports/{report_id}")
