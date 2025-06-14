Immediate Search
================

This tutorial demonstrates how to perform immediate (real-time) searches
for case and party records using the `PCLClient` class. These types of
queries return results instantly and are suited for simple lookups.

Case Search
-----------

Use `PCLClient.search_cases()` to search for cases by various parameters.

Example:

.. code-block:: python

    from pacersdk.client import PCLClient

    client = PCLClient(
        username="your_username",
        password="your_password",
        environment="qa"
    )

    result = client.search_cases({
        "caseTitle": "Smith vs"
    })
    print(result)

Party Search
------------

Use `PCLClient.search_parties()` to find parties by name or role.

Example:

.. code-block:: python

    from pacersdk.client import PCLClient

    client = PCLClient(
        username="your_username",
        password="your_password",
        environment="qa"
    )

    result = client.search_parties({
        "lastName": "Johnson"
    })
    print(result)
