Multi-Factor Authentication (MFA)
=================================

PACER supports multi-factor authentication (MFA) using time-based one-time
passwords (TOTP). This library supports MFA by allowing you to provide a
base32-encoded TOTP secret key when initializing the client.

Using MFA with PCLClient
------------------------

To authenticate with MFA enabled, provide your TOTP secret to the client:

.. code-block:: python

    from pacersdk.client import PCLClient

    client = PCLClient(
        username="your_username",
        password="your_password",
        secret="YOUR_BASE32_SECRET",  # TOTP secret from PACER
        environment="qa"
    )

    result = client.search_cases({
        "caseTitle": "Smith"
    })
    print(result)

Notes:

- The TOTP secret is optional and only required if MFA is enabled on your PACER account.
- The client uses the secret to automatically generate a valid TOTP code for each login.
- Each TOTP code is valid for about 30 seconds.

Managing Your MFA Secret
------------------------

.. warning::

    PACER allows up to **five registered authenticator apps**. To add a new one, you may need to delete an existing app.

To register a new TOTP secret with PACER:

1. Go to the appropriate PACER account management site:

   - **Production**: https://pacer.psc.uscourts.gov  
   - **QA/Test**: https://qa-pacer.psc.uscourts.gov

2. Navigate to **Settings** > **Manage MFA Settings**.

3. If five apps are already registered, delete one to make space.

4. Click **Add App** to generate a new TOTP secret and QR code.

5. Scan the QR code or manually enter the secret into an authenticator app (e.g., Google Authenticator, Authy).

6. Complete setup by entering the current TOTP from your app.

7. Save the base32-encoded secret securely, and configure it in your environment:

   .. code-block:: bash

       PACER_MFA_SECRET=YOUR_NEW_SECRET

8. Re-run your client code to verify that authentication works with the new secret.

.. note::

    The TOTP secret is effectively a password. Keep it private and secure.
    If it becomes compromised or inaccessible, you must delete the app and add a new one.
