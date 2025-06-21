Getting Started
===============

This guide helps you get up and running with `pacersdk`.
It covers installation via pip or source, setting up a virtual environment,
and preparing your environment for development or use.

Install from PyPI
-----------------

The simplest method is to install from the Python Package Index:

.. code-block:: shell

    pip install -U pacersdk

Install from Source
-------------------

To install from source (e.g. to contribute or use the latest version):

1. **Clone the repository:**

   .. code-block:: shell

      git clone https://github.com/mcpcpc/pacersdk.git
      cd pacersdk/

2. **Create a virtual environment (optional but recommended):**

   .. code-block:: shell

      python -m venv venv

3. **Activate the virtual environment:**

   - On macOS/Linux:

     .. code-block:: shell

        source venv/bin/activate

   - On Windows:

     .. code-block:: shell

        venv\Scripts\activate

4. **Install the package in editable/development mode:**

   .. code-block:: shell

      pip install -e .

This setup allows you to modify the code and have changes reflected immediately.

Next Steps
----------

- :doc:`basic_usage` – Learn how to use pacersdk in your project
- :doc:`api_reference` – Explore the available API classes and methods
