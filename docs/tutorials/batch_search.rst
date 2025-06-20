Batch Search
============

Batch searching supports long-running job submission and result polling.

Example:

.. code-block:: python

    from pacersdk.client import PCLClient

    client = PCLClient(
        username="your_username",
        password="your_password",
        environment="qa"
    )

    response = client.batch_case.submit({
        "caseTitle": "Acme"
    })

    report_id = response.get("reportId")

    # Check status
    status = client.batch_case.status(report_id)
    print(status)

    # Download results when complete
    if status["status"] == "COMPLETED":
        results = client.batch_case.download(report_id)
        print(results)
