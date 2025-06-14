"""
Service for submitting and managing batch case searches.
"""

from typing import Callable
from typing import cast
from typing import Optional

from ..session import PCLSession
from ..models.batch import BatchCaseResponse
from ..models.batch import BatchCaseRequest


class BatchCaseSearchService:
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
        self.session = PCLSession(token_provider, config, token)

    def submit(self, request: BatchCaseRequest) -> BatchCaseResponse:
        """
        Submit a batch case search job.

        :param request: A batch case search request model.
        :return: A BatchCaseResponse dictionary.
        """
        return cast(
            BatchCaseResponse,
            self.session.post("/pcl-public-api/rest/cases/download", request),
        )

    def status(self, job_id: str) -> dict:
        """
        Query the status of a batch case search job.

        :param job_id: The job identifier.
        :return: JSON status response.
        """
        return self.session.get(f"/pcl-public-api/rest/cases/download/status/{job_id}")

    def download(self, job_id: str) -> dict:
        """
        Download results of a completed batch case search job.

        :param job_id: The job identifier.
        :return: JSON response containing case data.
        """
        return self.session.get(f"/pcl-public-api/rest/cases/download/{job_id}")

    def delete(self, job_id: str) -> dict:
        """
        Delete a submitted batch case job by ID.

        :param job_id: Batch job identifier.
        :return: Response status or message.
        """
        return self.session.delete(f"/pcl-public-api/rest/cases/reports/{job_id}")
