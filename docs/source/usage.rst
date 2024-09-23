.. _PyPI: https://pypi.org/
.. _python-dateutil: https://dateutil.readthedocs.io/

#########
  Usage
#########

================
  Installation
================

First install package using ``pip``:

.. code:: bash

    python3 - m pip install decimaldate

===============
  DecimalDate
===============

.. note::

   The ``decimaldate`` objects used internally and being exposed by method calls
   ignores time (hours, minutes, and seconds) and are *not* timezone aware.

``DecimalDate`` has utility and convenience methods,
but for more advanced use,
like determine if a date is a Saturday,
or the difference in days between two dates,
you can use the methods of ``datetime``.

>>> DecimalDate.today().as_datetime() - DecimalDate.yesterday().as_datetime()
datetime.timedelta(days=1)

For more complex ``datetime`` computations see python-dateutil_,

Creation
--------

No argument or ``None``
    Will use today's date:
        
    .. code:: python
       
       DecimalDate()
       DecimalDate(None)

``int``
    >>> DecimalDate(20240911)
    DecimalDate(20240911)

``str``
    >>> DecimalDate("20240911")
    DecimalDate(20240911)

``decimaldate``
    >>> from datetime import datetime
    >>> DecimalDate(datetime.today()) == DecimalDate.today()
    True

Representation
--------------

``repr()``
    >>> repr(DecimalDate(2024_09_11))
    DecimalDate(20240911)

``int()``
    >>> int(DecimalDate(2024_09_11))
    20240911

``str()``
    >>> str(DecimalDate(2024_09_11))
    '20240911'


Comparisons
-----------

The usual comparison operators are available:
  
  - equality, ``==``
  
    >>> DecimalDate.today() == DecimalDate.yesterday()
    False
  
  - inequality, ``!=``

    >>> DecimalDate.today() != DecimalDate.yesterday()
    True
  
  - less-than, ``<``

    >>> DecimalDate.today() < DecimalDate.yesterday()
    False

  - less-than-or-equal, ``<=``

    >>> DecimalDate.today() <= DecimalDate.yesterday()
    False

  - greater-than, ``>``

    >>> DecimalDate.today() > DecimalDate.yesterday()
    True

  - greater-than-or-equal, ``>=``

    >>> DecimalDate.today() >= DecimalDate.yesterday()
    True

Methods
-------

``year()``
    The year of date as an integer (1-9999).

    >>> DecimalDate(2024_09_11).year()
    2024

``month()``
    The month of date as an integer (1-12).

    >>> DecimalDate(2024_09_11).month()
    9

``day()``
    The day of date as an integer (1-31).

    >>> DecimalDate(2024_09_11).day()
    11

``last_day_of_month()``
    The last day of date's month as an integer (1-31).

    >>> DecimalDate(2024_09_11).last_day_of_month()
    30

``start_of_month()``
    A new ``DecimalDate`` instance with the date of start-of-month.

    >>> DecimalDate(2024_09_11).start_of_month()
    DecimalDate(20240901)

``end_of_month()``
    A new ``DecimalDate`` instance with the date of end-of-month.

    >>> DecimalDate(2024_09_11).end_of_month()
    DecimalDate(20240930)

``split()``
    Splits date into constituent year, month, and day as a tuple of integers.

    >>> DecimalDate(2024_09_11).split()
    (2024, 9, 11)

``clone()``
    A new ``DecimalDate`` instance identical to original.

    >>> dd = DecimalDate(2024_09_11)
    >>> clone = dd.clone()
    >>> dd == clone
    True
    >>> dd is dd
    True
    >>> dd is clone
    False

    .. note:: 
        As ``DecimalDate`` is immutable you should consider an assignment instead.

``next()``
    A new ``DecimalDate`` instance with the day after.

    >>> DecimalDate(2024_09_11).next()
    DecimalDate(20240912)

    If ``next()`` is given an argument it will return value days forward.

    >>> DecimalDate(2024_09_11).next(42)
    DecimalDate(20241023)

    A negative argument is simlar to ``previous()``

    >>> DecimalDate(2024_09_11).next(-42)
    DecimalDate(20240731)

    >>> DecimalDate(2024_09_11).previous(42)
    DecimalDate(20240731)

``previous()``
    A new ``DecimalDate`` instance with the day before.

    >>> DecimalDate(2024_09_11).previous()
    DecimalDate(20240910)

    If ``previous()`` is given an argument it will return value days back.

    >>> DecimalDate(2024_09_11).previous(42)
    DecimalDate(20240731)

    A negative argument is simlar to ``next()``

    >>> DecimalDate(2024_09_11).previous(-42)
    DecimalDate(20241023)

    >>> DecimalDate(2024_09_11).next(42)
    DecimalDate(20241023)

As other types
--------------

``as_int()``
    ``int`` representation.

    >>> DecimalDate(2024_09_11).as_int()
    20240911

    Similar to ``ìnt()``

    >>> int(DecimalDate(2023_01_17))
    20230117

``as_str()``
    ``str`` representation.

    >>> DecimalDate(2024_09_11).as_str()
    '20240911'

    Similar to ``str()``

    >>> str(DecimalDate(2023_01_17))
    '20230117'

    There is an optional separator.

``as_datetime()``
    ``datetime`` representation.

    >>> DecimalDate(2024_09_11).as_datetime()
    datetime.datetime(2024, 9, 11, 0, 0)

    Returned ``datetime`` has no time (hours, minutes, and seconds) and is not TimeZone aware.

    The ``datetime`` representation is convenient to calculate the difference in days between two dates,
    or to determine if a date is a Saturday.

Static methods
--------------

``today()``
    A new ``DecimalDate`` instance with today's date.

    >>> DecimalDate.today()

``yesterday()``
    A new ``DecimalDate`` instance with yesterday's date.

    >>> DecimalDate.yesterday()

``tomorrow()``
    A new ``DecimalDate`` instance with tomorrows's date.

    >>> DecimalDate.tomorrow()

``range()``
    See ``DecimalDateRange``.

====================
  DecimalDateRange
====================

Intended use is by using the ``DecimalDate`` static method ``range()``.

.. code:: python

   DecimalDate.range(start, stop)

.. code:: python

   DecimalDateRange(start, stop)

will behave identically.

Creation
--------

``DecimalDateRange``
    >>> for dd in DecimalDateRange(DecimalDate(2024_02_14), DecimalDate(2024_02_17)):
    >>>     print(dd)
    20240214
    20240215
    20240216
