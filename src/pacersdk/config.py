"""
Environment-specific API configuration for PACER endpoints.
"""

from importlib.resources import files
from json import loads
from typing import Optional


class ConfigLoader:
    """
    Loads environment-specific API configuration from a JSON file.

    This class reads configuration values for different environments (e.g., "qa", "prod")
    from either a bundled `default.json` or a user-supplied path.

    :param path: Optional path to a JSON file with configurations.
    :type path: str or None
    """

    def __init__(self, path: Optional[str] = None) -> None:
        """
        Initialize the configuration loader.

        :param path: Optional path to a JSON file with configurations.
        :type path: str or None
        """
        if path:
            with open(path) as f:
                content = f.read()
        else:
            file = files(__package__).joinpath("default.json")
            with file.open("r") as f:
                content = f.read()
        self._configs = loads(content)

    def get(self, env: str) -> dict:
        """
        Retrieve API URL configuration for the given environment.

        :param env: Environment name ("qa" or "prod").
        :type env: str
        :return: A dictionary containing auth and API URLs.
        :rtype: dict
        :raises ValueError: If the environment is not found in the configuration.
        """
        config = self._configs.get(env)
        if not isinstance(config, dict):
            raise ValueError(f"Environment '{env}' not found in config.")
        return config
