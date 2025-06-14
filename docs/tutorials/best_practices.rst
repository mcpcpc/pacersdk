Best Practices
==============

This page outlines recommended practices for securely and efficiently using
the `pacersdk` library when working with the PACER Case Locator (PCL) API.

Secure Your Credentials
-----------------------

Avoid hardcoding your PACER credentials directly into your scripts or source code.

**Recommendations:**

- Use environment variables:

  .. code-block:: bash

     export PACER_USERNAME="your-username"
     export PACER_PASSWORD="your-password"

- Access them in Python:

  .. code-block:: python

     import os
     username = os.getenv("PACER_USERNAME")
     password = os.getenv("PACER_PASSWORD")

- Consider using secret managers (e.g., HashiCorp Vault, AWS Secrets Manager)
  in production environments.

Use the QA Environment for Testing
----------------------------------

PACER provides a **QA environment** with test data that is not billable.
Always use this environment for development and testing:

.. code-block:: python

   client = PCLClient(username, password, environment="qa")

This helps avoid unintended charges during development.

Minimize Token Overhead
------------------------

When using services repeatedly, avoid reauthenticating every time:

- Initialize a single instance of `PCLClient` and reuse it.
- All service methods share a session and reuse the authentication token.
- Tokens are refreshed only when necessary.

Avoid Unnecessary Requests
--------------------------

The PACER API may rate-limit or restrict excessive use. You can reduce load by:

- Filtering your queries to narrow result sets.
- Using sorting parameters to organize results efficiently.
- Paginating results to limit the size of each request.

Use Batch Requests Wisely
--------------------------

Batch endpoints are ideal for submitting large searches asynchronously. Use them when:

- You're retrieving many cases or parties at once.
- You don’t need immediate results and can poll for completion.

For more details, see the :doc:`batch_search` guide.

Protect Sensitive Information
-----------------------------

If you use OTP-based authentication or store any redaction credentials:

- Avoid logging full request payloads that include secrets.
- Rotate credentials regularly.
- Use `.gitignore` to exclude sensitive config files from source control.
