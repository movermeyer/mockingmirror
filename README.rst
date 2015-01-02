Mocking Mirror
==============

Make strict mock objects using a mirror

.. code:: python

    import mockingmirror

    mirror = mockingmirror.Mirror()
    mock = mirror.mock

    # Create an object with a method that returns "Hello, World" when called
    mirror.myobject.mymethod()[:] = "Hello, World"
    assert mock.myobject.mymethod() == "Hello, World"
