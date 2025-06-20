Best Practices
==============

This page outlines recommended practices for securely and efficiently using
the `pacersdk` library when working with the PACER Case Locator (PCL) API.

Secure Your Credentials
-----------------------

Avoid hardcoding your PACER credentials or secrets directly into your scripts or source code.

**Recommendations:**

- Store your PACER credentials and TOTP secret as environment variables:

  .. code-block:: bash

     export PACER_USERNAME="your-username"
     export PACER_PASSWORD="your-password"
     export PACER_MFA_SECRET="your-base32-totp-secret"

- Access them in Python:

  .. code-block:: python

     from os import getenv

     username = getenv("PACER_USERNAME")
     password = getenv("PACER_PASSWORD")
     secret = getenv("PACER_MFA_SECRET")

     from pacersdk.client import PCLClient

     client = PCLClient(
         username=username,
         password=password,
         secret=secret,
         environment="prod"
     )

- Never commit secrets to version control. Use `.gitignore` to exclude `.env` or config files.

- For production environments, consider using secret managers such as:
  - HashiCorp Vault
  - AWS Secrets Manager
  - Azure Key Vault

- Rotate passwords and TOTP secrets regularly, especially if shared across systems.

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

- Avoid logging full request payloads that include credentials or secrets.
- Store secrets (e.g. TOTP keys) securely and limit access to them.
- Never expose PACER credentials or MFA secrets in stack traces or debug logs.
- Rotate secrets periodically to minimize the risk of compromise.
