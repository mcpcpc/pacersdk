Immediate Search
================

This tutorial demonstrates how to perform immediate (real-time) searches
for case and party records using the `PCLClient` class. These types of
queries return results instantly and are suited for simple lookups.

Case Search
-----------

Use `PCLClient.case.search()` to search for cases by various parameters.

Example:

.. code-block:: python

    from pacersdk.client import PCLClient

    client = PCLClient(
        username="your_username",
        password="your_password",
        environment="qa"
    )

    result = client.case.search({
        "caseTitle": "Smith vs"
    })
    print(result)

Party Search
------------

Use `PCLClient.party.search()` to find parties by name or role.

Example:

.. code-block:: python

    from pacersdk.client import PCLClient

    client = PCLClient(
        username="your_username",
        password="your_password",
        environment="qa"
    )

    result = client.party.search({
        "lastName": "Johnson"
    })
    print(result)
