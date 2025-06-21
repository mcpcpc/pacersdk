"""
Authentication handler for PACER Case Locator API using CSO credentials.
"""

from logging import getLogger
from json import dumps, loads
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from .otp import totp

logger = getLogger(__name__)


class Authenticator:
    """
    Manages authentication with the PACER Case Locator API.
    """

    def __init__(
        self,
        username: str,
        password: str,
        config: dict,
        secret: str = None,
        client_code: str = None,
        redaction: bool = False,
    ) -> None:
        """
        Initialize the Authenticator.

        :param username: CSO username.
        :param password: CSO password.
        :param config: Dictionary with API endpoint configuration.
        :param secret: Optional TOTP base32 secret (for MFA accounts).
        :param client_code: Optional client code for court searches.
        :param redaction: Optional flag to indicate redaction compliance.
        """
        self.username = username
        self.password = password
        self.config = config
        self.secret = secret
        self.client_code = client_code
        self.redaction = redaction
        self.token = None

    def get_token(self) -> str:
        """
        Authenticate and retrieve a session token.

        :return: A valid session token string.
        """
        logger.debug("Requesting new CSO token for user: %s", self.username)
        host = self.config["authenticationurl"]
        body = {"loginId": self.username, "password": self.password}
        if isinstance(self.secret, str):
            body["otpCode"] = totp(self.secret)
        if isinstance(self.client_code, str):
            body["clientCode"] = self.client_code
        if self.redaction:
            body["redactFlag"] = "1"
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        request = Request(
            url=f"{host}/services/cso-auth",
            method="POST",
            headers=headers,
            data=dumps(body).encode(),
        )
        with urlopen(request) as response:
            data = response.read().decode()
        message = loads(data)
        self.token = message["nextGenCSO"]
        return self.token

    def logout(self) -> None:
        """
        Log out and invalidate the session token.
        """
        if not isinstance(self.token, str):
            return
        host = self.config["authenticationurl"]
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        body = {"nextGenCSO": self.token}
        request = Request(
            url=f"{host}/services/cso-logout",
            method="POST",
            headers=headers,
            data=dumps(body).encode(),
        )
        try:
            with urlopen(request) as response:
                pass
        except HTTPError as e:
            if e.code != 204:
                message = e.read().decode()
                raise Exception(message)
        finally:
            self.token = None
