========
Usage
========

To use djangomailup in a project:

.. code-block:: python

    from djangomailup import MailUpClient
    
    client = MailUpClient()
    
    # return account info
    info = client.get_info()
