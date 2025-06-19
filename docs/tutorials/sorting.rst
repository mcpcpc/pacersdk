Sorting
=======

The PACER API supports sorting on many fields for both case and party searches.
This tutorial explains how to apply sorting parameters using the `pacersdk`
library.

Overview
--------

Sorting is specified using a list of field and direction pairs, where each
pair defines how to order the results. The sort order follows the sequence of
the provided list--meaning earlier fields take precedence in the sort order.

You can sort on one or more fields using `"ASC"` for ascending and `"DESC"` for
descending order.

Case Sorting Example
--------------------

Here's how to sort search results by case year (descending) and then by
case type (ascending):

.. code-block:: python

    from pacersdk.client import PCLClient

    client = PCLClient(
        username="your_username",
        password="your_password",
        environment="qa"
    )
    criteria = {"jurisdictionType": "civil"}

    sort_fields = [
        {"field": "caseYear", "order": "DESC"},
        {"field": "caseType", "order": "ASC"},
    ]

    response = client.search_cases(criteria, sort=sort_fields)
    print(response)

Important Notes
---------------

- The sort order in the list matters. The API will prioritize sorting
  by the first field, then within that by the second, and so on.
- Sorting is optional. If not provided, default API sorting will apply.
- Invalid field names or directions will result in an API error.

For available sortable fields, see the library reference documentation for:

- :class:`pacersdk.models.sort.SortableCaseField`
- :class:`pacersdk.models.sort.SortablePartyField`
