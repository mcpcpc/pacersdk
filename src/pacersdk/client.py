"""
Client interface to the PACER Case Locator API.
"""

from .auth import Authenticator
from .config import ConfigLoader
from .models.query import CourtCaseSearchCriteria, PartySearchCriteria
from .models.reports import ReportInfo, ReportList
from .services.case import CaseService
from .services.party import PartyService
from .services.batch_case import BatchCaseService
from .services.batch_party import BatchPartyService


class PCLClient:
    """
    Entry point for interacting with the PACER Case Locator API.
    """

    def __init__(
        self,
        username: str,
        password: str,
        secret: str = None,
        environment: str = "prod",
        client_code: str = None,
        redaction: bool = False,
        config_path: str = None,
    ) -> None:
        """
        Initialize the API client.

        :param username: PACER system user ID.
        :param password: PACER system password.
        :param secret: Optional TOTP base32 secret for MFA accounts.
        :param environment: Environment key ("qa" or "prod").
        :param client_code: Optional client code for court searches.
        :param redaction: Optional flag to indicate redaction compliance.
        :param config_path: Optional path to a custom JSON config file.
        """
        self._config_loader = ConfigLoader(config_path)
        config = self._config_loader.get(environment)

        #: Instance of :class:`pacersdk.auth.Authenticator`
        self.authenticator = Authenticator(
            username=username,
            password=password,
            secret=secret,
            config=config,
            client_code=client_code,
            redaction=redaction,
        )

        self.token_provider = self.authenticator.get_token
        token = self.token_provider()

        #: Instance of :class:`pacersdk.services.case.CaseService`
        self.case = CaseService(self.token_provider, config, token)

        #: Instance of :class:`pacersdk.services.party.PartyService`
        self.party = PartyService(self.token_provider, config, token)

        #: Instance of :class:`pacersdk.services.batch_case.BatchCaseService`
        self.batch_case = BatchCaseService(self.token_provider, config, token)

        #: Instance of :class:`pacersdk.services.batch_party.BatchPartyService`
        self.batch_party = BatchPartyService(self.token_provider, config, token)

    def logout(self) -> None:
        """
        Log out of the session and revoke the token.
        """
        return self.authenticator.logout()
