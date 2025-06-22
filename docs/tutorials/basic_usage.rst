Basic Usage
===========

This guide shows how to perform a basic case or party search using the `pacersdk` client.

Initialize the Client
---------------------

Before performing any searches, create a client instance using your PACER credentials:

.. code-block:: python

    from pacersdk import PCLClient

    client = PCLClient(
        username="your-username",
        password="your-password",
        secret="your-client-secret",  # optional
        client_code="your-client-code"  # optional
        environment="qa",  # for testing purposes
    )

Immediate Search (Single Case or Party)
---------------------------------------

Immediate searches return results in groups of 54. Each group is referred to as a "page."
The maximum number of results returned by an immediate search is **5,400 items** (100 pages).
If more results are available beyond the first page, you must request additional pages explicitly.

Immediate searches are ideal for smaller queries or when users want fast access to limited sets of results. 
Search criteria are passed as a dictionary using the relevant model: `CourtCaseSearchCriteria` or `PartySearchCriteria`.

There are two ways to perform an immediate search:

1. **Single-page search** using `search()`
2. **Paginated search** using `search_all()` to retrieve all pages automatically

**Single-Page Case Search:**

.. code-block:: python

    from pacersdk.models.query import CourtCaseSearchCriteria

    criteria: CourtCaseSearchCriteria = {
        "caseNumberFull": "1:2002bk20340",
    }

    report_list = client.case.search(criteria)

    for case in report_list["content"]:
        print(case["caseNumberFull"], "-", case["caseTitle"])

**Paginated Case Search:**

.. code-block:: python

    from pacersdk.models.query import CourtCaseSearchCriteria

    criteria: CourtCaseSearchCriteria = {
        "courtId": "nysb",  # example: Southern District of New York
        "caseTitle": "Acme Corp"
    }

    for report_list in client.case.search_all(criteria):
        for case in report_list["content"]:
            print(case["caseNumberFull"], "-", case["caseTitle"])

**Single-Page Party Search:**

.. code-block:: python

    from pacersdk.models.query import PartySearchCriteria

    criteria: PartySearchCriteria = {
        "lastName": "smith",
        "ssn": "123456789",
    }

    report_list = client.party.search(criteria)

    for party in report_list["content"]:
        print(party["firstName"], party["lastName"], "--", party["caseNumberFull"])

**Paginated Party Search:**

.. code-block:: python

    from pacersdk.models.query import PartySearchCriteria

    criteria: PartySearchCriteria = {
        "lastName": "Smith"
    }

    for report_list in client.party.search_all(criteria):
        for party in report_list["content"]:
            print(party["firstName"], party["lastName"], "--", party["caseNumberFull"])

Batch Search
------------

Batch searches allow you to request a large set of search results (up to **108,000 items**) that are 
queued and processed asynchronously. Unlike immediate searches, which require manual pagination,
batch searches return **all results in one downloadable report** after processing completes.

Each batch search submission returns a `reportId`, which you can use to:

- Check job status (e.g. `RUNNING`, `WAITING`, `COMPLETED`)
- Download results once complete
- Delete results once consumed (recommended)

Batch search criteria are submitted using the same structure as immediate searches.

**Batch Case Search:**

.. code-block:: python

    from pacersdk.models.query import CourtCaseSearchCriteria

    criteria: CourtCaseSearchCriteria = {
        "caseNumberFull": "12-20340",
        "courtId": ["insbk"]
    }

    report_info = client.batch_case.submit(criteria)
    print("Submitted batch case search with report ID:", report_info["reportId"])

**Batch Party Search:**

.. code-block:: python

    from pacersdk.models.query import PartySearchCriteria

    criteria: PartySearchCriteria = {
        "lastName": "smith",
        "ssn": "123456789"
    }

    report_info = client.batch_party.submit(criteria)
    print("Submitted batch party search with report ID:", report_info["reportId"])

**Check Status of a Batch Job:**

.. code-block:: python

    report_id = report_info["reportId"]
    status = client.batch_case.status(report_id)
    print("Status:", status["status"])

**Download Results (when status is COMPLETED):**

.. code-block:: python

    results = client.batch_case.download(report_id)
    for case in results["content"]:
        print(case["caseNumberFull"], "-", case["caseTitle"])

**Delete Batch Job (optional, but recommended):**

.. code-block:: python

    client.batch_case.delete(report_id)
    print("Deleted batch report:", report_id)

Notes
-----

- Ensure your account has access to PACER Case Locator and the correct court IDs.
- Batch responses may be delayed depending on PACER load and queueing.
