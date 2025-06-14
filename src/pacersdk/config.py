"""
Environment-specific API configuration for PACER endpoints.
"""

from importlib.resources import files
from json import loads


def get_config(env: str, path: str = None) -> dict:
    """
    Retrieve API URL configuration for the given environment.

    :param env: Environment name ("qa" or "prod").
    :param path: Optional path to a JSON file with configurations.
    :return: A dictionary containing auth and API URLs.
    """
    if isinstance(path, str):
        with open(path) as f:
            content = f.read()
    else:
        file = files(__package__).joinpath("default.json")
        with file.open("r") as f:
            content = f.read()
    configs = loads(content)
    config = configs.get(env, None)
    if not isinstance(config, dict):
        raise ValueError(f"Environment '{env}' not found in config.")
    return config
