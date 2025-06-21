Logging
=======

The PACER SDK uses standard Python logging and follows the same conventions as the Azure SDK libraries.
This means logging is **off by default** and must be configured by the user.

Basic Configuration
-------------------

To enable logging and view debug output from the SDK:

.. code-block:: python

    import logging

    # Configure root logger
    logging.basicConfig(level=logging.DEBUG)

    # Optionally configure specific logger for the SDK
    logger = logging.getLogger("pacersdk")
    logger.setLevel(logging.DEBUG)

    # Use the SDK
    from pacersdk.client import PCLClient
    client = PCLClient(...)

Logging Hierarchy
-----------------

Each module in the SDK uses its own logger based on its import path:

- ``pacersdk.client``
- ``pacersdk.auth``
- ``pacersdk.services.case.search``
- ``pacersdk.services.case.batch``
- ``pacersdk.services.party.search``
- ``pacersdk.services.party.batch``

You can target a specific component:

.. code-block:: python

    logging.getLogger("pacersdk.services.case.search").setLevel(logging.DEBUG)

Structured Logging
------------------

While the SDK emits unstructured debug logs (using ``logger.debug(...)``), you can add formatters to improve output:

.. code-block:: python

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    handler.setFormatter(formatter)
    logging.getLogger("pacersdk").addHandler(handler)

Disabling Logging
-----------------

To disable all SDK logs:

.. code-block:: python

    logging.getLogger("pacersdk").setLevel(logging.CRITICAL)

Further Reading
---------------

See the `Python logging documentation <https://docs.python.org/3/library/logging.html>`_
for more advanced configuration options.
