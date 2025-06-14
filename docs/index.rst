pacersdk
=========

A Python SDK for interacting with the PACER Case Locator (PCL) API.

What is PACER?
--------------

**PACER** (Public Access to Court Electronic Records) is a service of the
U.S. federal judiciary that provides electronic public access to federal
appellate, district, and bankruptcy court records. It allows users to search
and retrieve case and docket information filed in federal courts.

Key features of PACER include:

- **Nationwide access** to court records across all U.S. federal courts.
- **Case indexing and search** through the PACER Case Locator (PCL).
- **Document retrieval** for pleadings, motions, orders, and opinions.
- **Fee-based system** with exemptions for low-usage access and QA environments.

The PACER Case Locator (PCL) offers a consolidated, searchable index of court
cases and is now accessible via a public RESTful API. This SDK simplifies
interacting with that API from Python applications.

.. admonition:: PACER QA Environment

   For testing purposes, a separate PACER QA environment is available. It
   contains test data and does not incur billing. We strongly recommend
   using it during development.

Resources
---------

- `PACER website <https://pacer.uscourts.gov>`__
- `PCL API documentation <https://pacer.uscourts.gov/sites/default/files/files/PCL-API-Document_4.pdf>`__
- `PACER authentication API <https://pacer.uscourts.gov/sites/default/files/files/PACER%20Authentication%20API-2025_v2_0.pdf>`__
- `PACER help center <https://pacer.uscourts.gov/help/pacer>`__

Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Tutorials:

   tutorials/install
   tutorials/immediate_search
   tutorials/batch_search
   tutorials/sorting 
   tutorials/mfa

.. toctree::
   :maxdepth: 2
   :caption: Library Reference:

   auth
   client
   config
   models
   otp
   services
   session
   
.. toctree::
   :maxdepth: 1
   :caption: Project Information:

   contribute
   lic
