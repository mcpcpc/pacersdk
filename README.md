# pacersdk

Public Access to Court Electronic Records (PACER) API client library written in Python.

## Background

The PACER Case Locator (PCL) system is a nationwide index of federal court cases. Since November 2024, a PCL application programming interface (API) and its documentation have been made available to the public for searching the index.

This library implements the API calls in a Pythonic way, allowing for intuitive and easy access to REST endpoints. The services are grouped into immediate and batch categories, reflecting the API's structure.

> **Note:** This library supports both QA and production environments. The QA environment contains test data and is suitable for development and testing. Searches made in production may incur billing.

## Requirements

- Python 3.11+
- A valid PACER account (QA or production)

## Install

### PyPI

```bash
pip install -U pacersdk
```

### From Source

```bash
git clone https://github.com/mcpcpc/pacersdk
cd pacersdk/
python -m venv venv
source venv/bin/activate
pip install -e .
```

## Documentation

See the full documentation at: [https://mcpcpc.github.io/pacersdk](https://mcpcpc.github.io/pacersdk)

## License

This project is licensed under the terms of the BSD 3-Clause License. See [LICENSE](LICENSE) for details.
