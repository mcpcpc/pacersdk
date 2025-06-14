from json import dump
from tempfile import NamedTemporaryFile
from unittest import main
from unittest import TestCase

from pacersdk.config import get_config


class TestConfig(TestCase):
    def test_valid_qa_environment(self) -> None:
        config = get_config("qa")
        self.assertIsInstance(config, dict)
        self.assertIsInstance(config.get("registrationurl"), str)
        self.assertTrue(config["registrationurl"].startswith("https://"))
        self.assertIsInstance(config.get("authenticationurl"), str)
        self.assertTrue(config["authenticationurl"].startswith("https://"))
        self.assertIsInstance(config.get("pclapiurl"), str)
        self.assertTrue(config["pclapiurl"].startswith("https://"))

    def test_valid_prod_environment(self) -> None:
        config = get_config("prod")
        self.assertIsInstance(config, dict)
        self.assertIsInstance(config.get("registrationurl"), str)
        self.assertTrue(config["registrationurl"].startswith("https://"))
        self.assertIsInstance(config.get("authenticationurl"), str)
        self.assertTrue(config["authenticationurl"].startswith("https://"))
        self.assertIsInstance(config.get("pclapiurl"), str)
        self.assertTrue(config["pclapiurl"].startswith("https://"))

    def test_invalid_environment_raises(self) -> None:
        with self.assertRaises(ValueError):
            get_config("invalid-env")

    def test_custom_path(self) -> None:
        custom_config = {
            "qa": {
                "registrationurl": "https://custom-qa-pacer",
                "authenticationurl": "https://custom-qa-login",
                "pclapiurl": "https://custom-qa-pcl",
            }
        }
        with NamedTemporaryFile(mode="w+", delete=False) as tmp:
            dump(custom_config, tmp)
            tmp_path = tmp.name
        loaded_config = get_config("qa", path=tmp_path)
        self.assertIn("custom-qa-pacer", loaded_config["registrationurl"])
        self.assertIn("custom-qa-login", loaded_config["authenticationurl"])
        self.assertIn("custom-qa-pcl", loaded_config["pclapiurl"])


if __name__ == "__main__":
    main()
