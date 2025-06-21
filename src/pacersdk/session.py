"""
Handles HTTP communication with the PACER Case Locator API.
"""

from json import dumps, loads
from typing import Any, Callable, Dict, Optional
from urllib.error import HTTPError
from urllib.request import Request, urlopen


class PCLSession:
    """
    A session wrapper for making authenticated POST requests to the API.
    """

    def __init__(
        self,
        token_provider: Callable[[], str],
        config: dict,
        max_retries: int = 0,
        token: Optional[str] = None,
    ) -> None:
        """
        Initialize the session.

        :param token_provider: Callable that returns a valid CSO token.
        :param config: Dictionary with base API URL.
        :param max_retries: Number of retries on token failure.
        :param token: Optional pre-fetched token.
        """
        self.token_provider = token_provider
        self.max_retries = max_retries
        self.base_path = config["pclapiurl"]
        self.token = token or self.token_provider()

    def _request(self, request: Request, attempt: int = 0) -> dict:
        """
        Internal request handler.

        :param request: Prepared urllib request object.
        :param attempt: Number of attempts since 401 error.
        :return: JSON response or {"status": "No Content"}.
        """
        request.headers["X-NEXT-GEN-CSO"] = self.token
        try:
            with urlopen(request) as response:
                if response.status == 204:
                    return {"status": "No Content"}
                data = response.read().decode()
            return loads(data)
        except HTTPError as e:
            if e.code == 401 and attempt < self.max_retries:
                self.token = self.token_provider()
                return self._request(request, attempt + 1)
            msg = e.read().decode()
            raise RuntimeError(f"HTTP {e.code} Error: {msg}")

    def get(self, path: str) -> dict:
        """
        Perform an authenticated GET request.

        :param path: URL path.
        :return: JSON response.
        """
        request = Request(
            url=f"{self.base_path}{path}",
            method="GET",
            headers={"Content-Type": "application/json", "Accept": "application/json"},
        )
        return self._request(request)

    def post(self, path: str, body: dict) -> dict:
        """
        Perform an authenticated POST request.

        :param path: URL path.
        :param data: Request body dictionary.
        :return: JSON response.
        """
        data = dumps(body).encode()
        request = Request(
            url=f"{self.base_path}{path}",
            method="POST",
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            data=data,
        )
        return self._request(request)

    def delete(self, path: str) -> dict:
        """
        Perform an authenticated DELETE request.

        :param path: URL path.
        :return: JSON response.
        """
        request = Request(
            url=f"{self.base_path}{path}",
            method="DELETE",
            headers={"Content-Type": "application/json", "Accept": "application/json"},
        )
        return self._request(request)
