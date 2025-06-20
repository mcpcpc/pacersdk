pacersdk
=========

A Python SDK for interacting with the PACER Case Locator (PCL) API.

What Is PACER?
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

Use Case and Audience
---------------------

This SDK is intended for **research and educational purposes only**. It enables users
to perform structured queries against PACER's public RESTful API to retrieve metadata
about federal cases and parties.

Typical users include:

- Legal researchers and academics
- Educators and students studying legal systems
- Developers experimenting with court data

Quickstart
----------

Install the SDK:

.. code-block:: bash

   pip install -U pacersdk

Perform a basic case search:

.. code-block:: python

   from pacersdk import PCLClient

   client = PCLClient(
       username="your_username",
       password="your_password",
       environment="qa"
   )
   results = client.case.search({
       "caseTitle": "Smith",
       "courtId": ["cacd"]
   })

.. admonition:: Developer Testing Environment
   :class: tip

   For testing purposes, a separate PACER QA environment is available. It
   contains test data and does not incur billing. We strongly recommend
   using it during development

Resources
---------

- `PACER Website <https://pacer.uscourts.gov>`__
- `PCL API User Guide <https://pacer.uscourts.gov/sites/default/files/files/PCL-API-Document_4.pdf>`__
- `PACER Authentication API User Guide <https://pacer.uscourts.gov/sites/default/files/files/PACER%20Authentication%20API-2025_v2_0.pdf>`__
- `How to Use PACER <https://pacer.uscourts.gov/help/pacer>`__

Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Tutorials:

   tutorials/getting_started
   tutorials/basic_usage
   tutorials/sorting_results 
   tutorials/multi_factor_authentication
   tutorials/logging
   tutorials/best_practices

.. toctree::
   :maxdepth: 1
   :caption: Library Reference:

   auth
   client
   config
   models/index
   otp
   services/index
   session
   
.. toctree::
   :maxdepth: 1
   :caption: Project Information:

   contributing
   lic
