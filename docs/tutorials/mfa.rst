Multi-Factor Authentication (MFA)
=================================

The PACER system supports multi-factor authentication (MFA) through a
time-based one-time password (TOTP) mechanism.

This library supports MFA by allowing you to pass a base32-encoded TOTP
secret key when initializing the client. This secret is available on the
PACER user account page when enabling MFA.

Using MFA with PCLClient
------------------------

To authenticate with MFA enabled, pass the TOTP secret directly:

.. code-block:: python

    from pacersdk.client import PCLClient

    client = PCLClient(
        username="your_username",
        password="your_password",
        secret="YOUR_BASE32_SECRET",  # PACER TOTP secret
        environment="qa"
    )

    result = client.search_cases({
        "caseTitle": "Smith"
    })
    print(result)

Notes
-----

- The base32-encoded TOTP secret is typically available from the PACER account
  settings page when enabling MFA.
- The `secret` argument is optional and only required when MFA is enabled.
- The client will automatically generate the correct TOTP code using the
  provided secret and attach it to the login request.
- Each TOTP code is valid for approximately 30 seconds.
