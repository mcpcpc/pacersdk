Contributing
============

We welcome contributions to `pacersdk`!

This project is intended to make working with the PACER Case Locator API
intuitive and accessible through Python. Whether you're fixing bugs,
adding features, or improving documentation, your help is appreciated.

Getting Started
---------------

1. Fork the repository on GitHub.
2. Clone your fork locally:

   .. code-block:: bash

      git clone https://github.com/mcpcpc/pacersdk.git
      cd pacersdk/

3. Create a new virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate

4. Install the project in editable mode:

   .. code-block:: bash

      pip install -e .

5. Install development tools (optional):

   .. code-block:: bash

      pip install -e .[dev]

Making Changes
--------------

- Follow PEP8 guidelines for code style.
- Use clear, concise commit messages.
- Include Sphinx-style docstrings for public modules and functions.
- Use `black` to automatically format code before committing:

   .. code-block:: bash

      black .

Testing Your Changes
--------------------

This project uses Python’s built-in ``unittest`` framework.

To run the test suite:

.. code-block:: bash

   python -m unittest

.. note::

   Please ensure the test suite is updated and all tests pass before
   submitting changes. This helps maintain reliability and consistency
   across the project.

Submitting Pull Requests
------------------------

1. Create a new branch for your feature or fix:

   .. code-block:: bash

      git checkout -b feature/my-new-feature

2. Make your changes and commit them.

3. Push to your fork and submit a pull request through GitHub.

4. Clearly describe the motivation for the change and what it does.

Code of Conduct
---------------

Please be respectful and considerate in all interactions and discussions.
We follow the `Contributor Covenant <https://www.contributor-covenant.org/>`_.

Thank You!
----------

Thanks for helping make this project better!
