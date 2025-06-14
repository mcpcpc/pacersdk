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

    response = client.submit_batch_case({
        "caseTitle": "Acme"
    })

    report_id = response.get("reportId")

    # Check status
    status = client.get_batch_case_status(report_id)
    print(status)

    # Download results when complete
    if status["status"] == "COMPLETED":
        results = client.get_batch_case_result(report_id)
        print(results)
