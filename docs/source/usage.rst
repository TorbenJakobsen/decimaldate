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

   The ``datetime`` objects used internally and being exposed by method calls
   ignores time (hours, minutes, and seconds) and are *not* timezone aware.

``DecimalDate`` has utility and convenience methods,
but for more advanced use,
like determine if a date is a Saturday,
or the difference in days between two dates,
you can use the methods of ``datetime``.

>>> from decimaldate import DecimalDate
>>> DecimalDate.today().as_datetime() - DecimalDate.yesterday().as_datetime()
datetime.timedelta(days=1)

For more complex ``datetime`` computations see python-dateutil_,

Initialization
--------------

No argument or ``None``
    Will use today's date:
        
    .. code:: python
       
       DecimalDate()
       DecimalDate(None)

``int``
    >>> from decimaldate import DecimalDate
    >>> DecimalDate(20240911)
    DecimalDate(20240911)

``str``
    >>> from decimaldate import DecimalDate
    >>> DecimalDate("20240911")
    DecimalDate(20240911)

``decimaldate``
    >>> from decimaldate import DecimalDate
    >>> from datetime import datetime
    >>> DecimalDate(datetime.today()) == DecimalDate.today()
    True

Representation
--------------

``repr()``
    >>> from decimaldate import DecimalDate
    >>> repr(DecimalDate(2024_09_11))
    DecimalDate(20240911)

``int()``
    >>> from decimaldate import DecimalDate
    >>> int(DecimalDate(2024_09_11))
    20240911

``str()``
    >>> from decimaldate import DecimalDate
    >>> str(DecimalDate(2024_09_11))
    '20240911'


Comparisons
-----------

The usual comparison operators are available:
  
  - equality, ``==``
  
    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() == DecimalDate.yesterday()
    False
  
  - inequality, ``!=``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() != DecimalDate.yesterday()
    True
  
  - less-than, ``<``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() < DecimalDate.yesterday()
    False

  - less-than-or-equal, ``<=``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() <= DecimalDate.yesterday()
    False

  - greater-than, ``>``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() > DecimalDate.yesterday()
    True

  - greater-than-or-equal, ``>=``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() >= DecimalDate.yesterday()
    True

Methods
-------

``year()``
    The year of date as an integer (1-9999).

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).year()
    2024

``month()``
    The month of date as an integer (1-12).

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).month()
    9

``day()``
    The day of date as an integer (1-31).

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).day()
    11


``weekday()``
    The day of the week as an integer (0-6), where Monday == ``0`` ... Sunday == ``6``.

    >>> from decimaldate import DecimalDate
    >>> FRIDAY = 4
    >>> DecimalDate(2024_09_27).weekday() == FRIDAY
    True

``isoweekday()``
    The day of the week as an integer (1-7), where Monday == ``1`` ... Sunday == ``7``.

    >>> from decimaldate import DecimalDate
    >>> ISO_FRIDAY = 5
    >>> DecimalDate(2024_09_27).isoweekday() == ISO_FRIDAY
    True

``isoformat()``
    The decimal date as a ``str`` formatted according to ISO (yyyy-mm-dd) and *not* including time or timezone.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_27).isoformat()
    '2024-09-27'

``last_day_of_month()``
    The last day of date's month as an integer (1-31).

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).last_day_of_month()
    30

``start_of_month()``
    A new ``DecimalDate`` instance with the date of start-of-month.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).start_of_month()
    DecimalDate(20240901)

``end_of_month()``
    A new ``DecimalDate`` instance with the date of end-of-month.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).end_of_month()
    DecimalDate(20240930)

``split()``
    Splits date into constituent year, month, and day as a tuple of integers.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).split()
    (2024, 9, 11)

``clone()``
    A new ``DecimalDate`` instance identical to original.

    >>> from decimaldate import DecimalDate
    >>> dd = DecimalDate(2024_09_11)
    >>> clone = dd.clone()
    >>> dd == clone
    True
    >>> dd is dd
    True
    >>> dd is clone
    False

    .. note:: 
        As ``DecimalDate`` is immutable, you should consider assignment instead.

``next()``
    A new ``DecimalDate`` instance with the day after.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).next()
    DecimalDate(20240912)

    If ``next()`` is given an argument it will return value days forward.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).next(42)
    DecimalDate(20241023)

    A negative argument is simlar to ``previous()``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).next(-42)
    DecimalDate(20240731)

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).previous(42)
    DecimalDate(20240731)

``previous()``
    A new ``DecimalDate`` instance with the day before.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).previous()
    DecimalDate(20240910)

    If ``previous()`` is given an argument it will return value days back.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).previous(42)
    DecimalDate(20240731)

    A negative argument is simlar to ``next()``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).previous(-42)
    DecimalDate(20241023)

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).next(42)
    DecimalDate(20241023)

As other types
--------------

``as_int()``
    ``int`` representation.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).as_int()
    20240911

    Similar to ``ìnt()``

    >>> from decimaldate import DecimalDate
    >>> int(DecimalDate(2023_01_17))
    20230117

``as_str()``
    ``str`` representation.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).as_str()
    '20240911'

    Similar to ``str()``

    >>> from decimaldate import DecimalDate
    >>> str(DecimalDate(2023_01_17))
    '20230117'

    There is an optional argument for separator.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).as_str('-')
    '2024-09-11'

``as_date()``
    ``datetime.date`` representation.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_27).as_date()
    datetime.date(2024, 9, 27)

    The returned ``date`` has no time (hours, minutes, and seconds) and is *not* TimeZone aware.

``as_datetime()``
    ``datetime.datetime`` representation.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).as_datetime()
    datetime.datetime(2024, 9, 11, 0, 0)

    The returned ``datetime`` has no time (hours, minutes, and seconds) and is *not* TimeZone aware.

    The ``datetime`` representation is convenient to calculate the difference in days between two dates,
    or to determine if a date is a Saturday.

Class Methods
-------------

``today()``
    A new ``DecimalDate`` instance with today's date.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today()

``yesterday()``
    A new ``DecimalDate`` instance with yesterday's date.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.yesterday()

``tomorrow()``
    A new ``DecimalDate`` instance with tomorrows's date.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.tomorrow()

``range()``
    See ``DecimalDateRange``.

``try_instantiate()``
    A new instance of ``DecimalDate`` if successful; otherwise ``None``.

    If no argument is given then uses today's date.\\

    .. note:: 
        No errors will be raised.
    
    >>> from decimaldate import DecimalDate
    >>> DecimalDate.try_instantiate() == DecimalDate(None)
    True
    >>> DecimalDate.try_instantiate(None) == DecimalDate.today()
    True

    An invalid date will return ``None``.

    >>> from decimaldate import DecimalDate
    >>> print(DecimalDate.try_instantiate(2024_27_09))
    None

    A valid date will instantiate a new ``DecimalDate``.

    >>> from decimaldate import DecimalDate
    >>> print(DecimalDate.try_instantiate("2024_09_27"))
    20240927

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
    >>> from decimaldate import DecimalDate, DecimalDateRange
    >>> for dd in DecimalDateRange(DecimalDate(2024_02_14), DecimalDate(2024_02_17)):
    >>>     print(dd)
    20240214
    20240215
    20240216
