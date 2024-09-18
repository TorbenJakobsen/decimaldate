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

   The ``decimaldate`` used are not timezone aware.

``DecimalDate`` has utility and convenience methods,
but for the more advanced like determine if a date is a Saturday,
or the difference in days between two dates,
you can use the methods of ``datetime``.

>>> DecimalDate.today().as_datetime() - DecimalDate.yesterday().as_datetime()
datetime.timedelta(days=1)

Creation
========

No argument or ``None``

  Will use today's date::

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
==============

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
===========

The usual comparison operators are available:
  
  - equality, ``==``
  - inequality, ``!=``
  - less-than, ``<``
  - less-than-or-equal, ``<=``
  - greater-than, ``>``
  - greater-than-or-equal, ``>=``

Methods
=======

``year()``

    >>> DecimalDate(2024_09_11).year()
    2024

``month()``

    >>> DecimalDate(2024_09_11).month()
    9

``day()``

    >>> DecimalDate(2024_09_11).day()
    11

``last_day_of_month()``

    >>> DecimalDate(2024_09_11).last_day_of_month()
    30

``start_of_month()``

    >>> DecimalDate(2024_09_11).start_of_month()
    DecimalDate(20240930)

``end_of_month()``

    >>> DecimalDate(2024_09_11).end_of_month()
    DecimalDate(20240930)

``split()``

    >>> DecimalDate(2024_09_11).split()
    (2024, 9, 11)

``clone()``

    >>> DecimalDate(2024_09_11).clone()
    DecimalDate(20240911)

``next()``

    >>> DecimalDate(2024_09_11).next()
    DecimalDate(20240912)

``previous()``

    >>> DecimalDate(2024_09_11).previous()
    DecimalDate(20240910)

As other types
==============

``as_int()``

    >>> DecimalDate(2024_09_11).as_int()
    20240911

``as_str()``

    >>> DecimalDate(2024_09_11).as_str()
    '20240911'

``as_datetime()``

    >>> DecimalDate(2024_09_11).as_datetime()

Static methods
==============

``today()``

    >>> DecimalDate.today()

``yesterday()``

    >>> DecimalDate.yesterday()

``tomorrow()``

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
========

``DecimalDateRange``

    >>> for dd in DecimalDateRange(DecimalDate(2024_02_14), DecimalDate(2024_02_17)):
    >>>     print(dd)
    20240214
    20240215
    20240216
