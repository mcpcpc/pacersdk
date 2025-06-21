Basic Usage
===========

This guide shows how to perform a basic case or party search using the `pacersdk` client.

Initialize the Client
---------------------

Before performing any searches, create a client instance using your PACER credentials:

.. code-block:: python

    from pacersdk.client import PCLClient

    client = PCLClient(
        username="your-username",
        password="your-password",
        secret="your-client-secret",  # optional
        client_code="your-client-code"  # optional
        environment="qa",
    )

Immediate Search (Single Case or Party)
---------------------------------------

Immediate searches return results in groups of 54. Each group of immediate search results is
referred to as a "page." The maximum search result size for an immediate search is 5,400 items
(cases or parties) or 100 pages.

**Case Search:**

.. code-block:: python

    from pacersdk.models.query import CourtCaseSearchCriteria

    criteria: CourtCaseSearchCriteria = {
        "caseNumberFull": "1:2002bk20340",
    }

    report_list = client.case.search(criteria)
    print(report_list)

**Party Search:**

.. code-block:: python

    from pacersdk.models.query import PartySearchCriteria

    criteria: PartySearchCriteria = {
        "lastName": "smith",
        "ssn": "123456789",
    }

    report_list = client.party.search(criteria)
    print(report_list)

Batch Search
------------

Batch searches function similarly to immediate searches except that the results of batch searches
are queued for later download. The benefit of batch searches is that they allow for a much larger
set of search results. In addition, immediate searches require multiple requests to page through
results, while batch searches return all rows in a single request. The maximum number of batch
search results is 108,000.

**Batch Case Search:**

.. code-block:: python

    from pacersdk.models.query import CourtCaseSearchCriteria

    criteria: CourtCaseSearchCriteria = {
        "caseNumberFull": "12-20340",
        "courtId": ["insbk",]
    }

    report_info = client.batch_case.submit(criteria)
    print(report_info)

**Batch Party Search:**

.. code-block:: python

    from pacersdk.models.query import PartySearchCriteria

    criteria: PartySearchCriteria = {
        "lastName": "smith",
        "ssn": "123456789",
    }

    report_info = client.batch_case.submit(criteria)
    print(report_info)

Notes
-----

- Ensure your account has access to PACER Case Locator and the correct court IDs.
- Batch responses may be delayed depending on PACER load and queueing.

Next Steps
----------

- :doc:`best_practices` – Security and usage guidelines.
