
Mocking Mirror
==============

* .. image:: https://img.shields.io/coveralls/NegativeMjark/mockingmirror.svg
   :target: https://coveralls.io/r/NegativeMjark/mockingmirror?branch=master

* .. image:: https://travis-ci.org/NegativeMjark/mockingmirror.svg?branch=master 
   :target: https://travis-ci.org/NegativeMjark/mockingmirror
 
Make strict mock objects using a mirror

.. code:: python

    import mockingmirror

    mirror, mock = mockingmirror.mirror()

    # Create an object with a method that returns "Hello, World" when called
    mirror.myobject.mymethod()[:] = "Hello, World"
    assert mock.myobject.mymethod() == "Hello, World"
