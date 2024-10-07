from __future__ import annotations

from collections.abc import Generator
from datetime import date, datetime, timedelta
from typing import Any, Literal, NoReturn, Self, TypeAlias

DecimalDateInitTypes: TypeAlias = int | str | datetime | date
"""
The regular types (excluding ``None`` and ``DecimalDate``)
that can be given as argument to 'init' methods.
"""


__all__ = [
    "DecimalDate",
    "DecimalDateRange",
]

#
# DecimalDate
#


class DecimalDate(object):
    """
    A class to represent a decimal date on the form ``yyyymmdd``.

    The class assumes *only* a Gregorian (went into effect in October 1582) calendar
    with: year, month, and day.

    Only dates that are valid for ``datetime.date`` are accepted.

    Used and exposed``datetime.date`` and ``datetime.datetime`` objects
    in this class are *naive* (meaning *not* TimeZone aware)!

    Examples::

        DecimalDate()            # today's date
        DecimalDate(None)        # today's date
        DecimalDate(20231225)
        DecimalDate("20230518")
        DecimalDate(date.today())
        DecimalDate(datetime.today())
    """

    # replace __dict__ : optimization and improving immutability
    __slots__ = (
        "_DecimalDate__dd_int",
        "_DecimalDate__dd_str",
        "_DecimalDate__dd_datetime",
        "_DecimalDate__dd_date",
        "_DecimalDate__year",
        "_DecimalDate__month",
        "_DecimalDate__day",
    )

    @staticmethod
    def __split(dd: int) -> tuple[int, int, int]:
        """
        A tuple with the constituent year, month, and day ``(yyyy, mm, dd)``
        from the argument decimal date on the form ``yyyymmdd``

        :param dd: A decimal date on the form ``yyyymmdd``.
        :type dd: int
        :return: A tuple with (year, month, day).
        :rtype: tuple[int, int, int]
        """
        yyyy, remain = divmod(dd, 1_00_00)
        mm, dd = divmod(remain, 1_00)
        return yyyy, mm, dd

    @staticmethod
    def __today_as_int() -> int:
        """
        Today's date as an integer on the form ``yyyymmdd``.\\
        The date is *not* TimeZone aware.

        :return: Today's date on the form ``yyyymmdd``.
        :rtype: int
        """
        today: date = date.today()  # no tzinfo
        return DecimalDate.__date_as_int(today)

    @staticmethod
    def __datetime_as_int(_datetime: datetime) -> int:
        """
        Returns an integer on the form ``yyyymmdd`` from the argument ``datetime``.

        >>> DecimalDate.__datetime_as_int(datetime.today())
            20240906

        :param _datetime: A ``datetime.datetime``.
        :type _datetime: datetime
        :return: Decimal date integer on the form ``yyyymmdd``.
        :rtype: int
        """
        return DecimalDate.__date_as_int(_datetime.date())

    @staticmethod
    def __date_as_int(_date: date) -> int:
        """
        Returns an integer on the form ``yyyymmdd`` from the argument ``datetime``.

        >>> DecimalDate.__date_as_int(date.today())
            20240906

        :param _date: A ``datetime.date``.
        :type _date: date
        :return: Decimal date integer on the form ``yyyymmdd``.
        :rtype: int
        """
        return DecimalDate.__ymd_as_int(_date.year, _date.month, _date.day)

    @staticmethod
    def __int_as_datetime(dd: int) -> datetime:
        """
        Returns a ``datetime`` from the argument ``int`` on the form ``yyyymmdd``.

        :param dd: A decimal date on the form ``yyyymmdd``.
        :type dd: int
        :return: ``datetime`` representing the argument ``yyyymmdd``.
        :rtype: datetime
        """
        year, month, day = DecimalDate.__split(dd)
        return datetime(year, month, day)

    @staticmethod
    def __ymd_as_int(year: int, month: int, day: int) -> int:
        return year * 1_00_00 + month * 1_00 + day

    @staticmethod
    def __start_of_month(dt: datetime) -> datetime:
        """
        Start date of a year and month taken from the argument.\\
        The day will always be ``1``.

        >>> DicimalDate(DecimalDate.__start_of_month(DecimalDate("2024_02_06").as_datetime()))
            DecimalDate(20240201)

        :param dt: A ``datetime``.
        :type dt: datetime
        :return: start date of year and month.
        :rtype: datetime
        """
        return dt.replace(day=1)  # new datetime

    @staticmethod
    def __end_of_month(dt: datetime) -> datetime:
        """
        End date of a year and month taken from the argument.

        >>> DicimalDate(DecimalDate.__end_of_month(DecimalDate("2024_02_06").as_datetime()))
            DecimalDate(20240229)

        :param dt: A ``datetime``.
        :type dt: datetime
        :return: end date of year and month.
        :rtype: datetime
        """
        # Day 28 exists in every month and 4 days later is always next month
        next_month: datetime = dt.replace(day=28) + timedelta(days=4)
        # Subtract day of next month gives last day of original month
        return next_month - timedelta(days=next_month.day)

    @staticmethod
    def __last_day_of_month(dt: datetime) -> int:
        """
        End day (1-31) of a year and month taken from the argument.

        >>> DecimalDate("2024_02_06")
            29

        :param dt: A ``datetime.datetime``.
        :type dt: datetime
        :return: End day (1-31)
        :rtype: int
        """
        return DecimalDate.__end_of_month(dt).day

    @staticmethod
    def __parse_int_value_from_argument(
        dd: DecimalDateInitTypes | DecimalDate | None,
    ) -> int:
        """
        Integer value of argument.

        The function returns an integer but does not validate the integer as a valid date.

        :param dd: A decimal date representation in one of the valid argument types.
        :type dd: DecimalDateInitTypes | DecimalDate | None
        :raises ValueError: If argument cannot be represented as an integer.
        :raises TypeError: If argument is not one of the valid argument types.
        :return: Integer value parsed from the argument.
                 The value is not guaranteed to be a valid date.
        :rtype: int
        """
        if dd is None:
            # Use the default today's date
            return DecimalDate.__today_as_int()

        elif isinstance(dd, int):
            return dd

        elif isinstance(dd, str):
            try:
                return int(dd)
            except ValueError as e_info:
                raise ValueError(f"argument {dd} is not a valid literal.") from e_info

        elif isinstance(dd, datetime):
            return DecimalDate.__datetime_as_int(dd)

        elif isinstance(dd, date):
            return DecimalDate.__date_as_int(dd)

        elif isinstance(dd, DecimalDate):
            return dd.as_int()

        else:
            raise TypeError(
                f"argument {dd} is not a valid literal on the form `yyyymmdd`."
            )

    #
    # Initialization
    #

    def __init__(
        self: Self,
        dd: DecimalDateInitTypes | Self | None = None,
    ) -> None:
        """
        Construct an immutable ``DecimalDate`` instance.

        If argument is not present or ``None``, then use today's date.

        :param dd: > date representation on the form ``yyyymmdd`` or a ``datetime``, defaults to ``None``
        :type dd: DecimalDateInitTypes | Self | None, optional
        :raises ValueError: If not a valid date, that can be represented on the form ``yyyymmdd``.
        :raises TypeError: If argument type is not valid (``None``, ``DecimalDate``, ``int``, ``str``, ``datetime``).
        """

        #
        # Instance variables
        # These have been placed in `__slots__`
        #

        self.__dd_int: int
        """ Internal instance value of the decimal date as an ``int`` on the form ``yyyymmdd``. """

        self.__dd_str: str
        """ Internal instance value of the decimal date as a ``str`` on the form ``"yyyymmdd"``. """

        self.__dd_datetime: datetime
        """ Internal instance value of the decimal date as a ``datetime.datetime``. """

        self.__year: int
        """ Internal instance value of the year (1-9999). """

        self.__month: int
        """ Internal instance value of the month (1-12). """

        self.__day: int
        """ Internal instance value of the day (1-31). """

        # ---

        self.__dd_int = DecimalDate.__parse_int_value_from_argument(dd)

        self.__dd_str = str(self.__dd_int)

        try:
            # If not a valid Gregorian date, then the following raises `ValueError`
            self.__dd_datetime = DecimalDate.__int_as_datetime(self.__dd_int)
        except ValueError as e_info:
            raise ValueError(
                f"argument {dd} is not a valid literal on the form `yyyymmdd`."
            ) from e_info

        self.__year, self.__month, self.__day = DecimalDate.__split(self.__dd_int)

    #
    # Comparisons
    #

    __UNSUPPORTED_OPERAND_TYPE: Literal["Unsupported operand type."] = (
        "Unsupported operand type."
    )

    def __eq__(self: Self, other: object) -> bool:
        """
        The equality operator, ``==``.

        :param other: the DecimalDate object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int == other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    def __ne__(self: Self, other: object) -> bool:
        """
        The inequality operator, ``!=``.

        :param other: Is the ``DecimalDate`` object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int != other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    def __gt__(self: Self, other: object) -> bool:
        """
        The greater-than operator, ``>``.

        :param other: Is the ``DecimalDate`` object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int > other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    def __ge__(self: Self, other: object) -> bool:
        """
        The greater-than-or-equal operator, ``>=``.

        :param other: Is the ``DecimalDate`` object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int >= other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    def __lt__(self: Self, other: object) -> bool:
        """
        The less-than operator, ``<``.

        :param other: Is the ``DecimalDate`` object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int < other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    def __le__(self: Self, other: object) -> bool:
        """
        The less-than-or-equal operator, ``<=``.

        :param other: Is the ``DecimalDate`` object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int <= other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    #
    # repr, str, int
    #

    def __repr__(self: Self) -> str:
        """
        When called by built-in ``repr()`` method returning a machine readable representation of ``DecimalDate``.

        >>> DecimalDate("2023_01_06")
            DecimalDate(20230106)

        :return: machine readable representation of this instance.
        :rtype: str
        """
        return f"DecimalDate({self.__dd_int})"

    def __str__(self: Self) -> str:
        """
        When ``str()`` is called on an instance of ``DecimalDate``.

        >>> str(DecimalDate(2023_01_06))
            '20230106'

        :return: string representation of this instance.
        :rtype: str
        """
        return self.__dd_str

    def __int__(self: Self) -> int:
        """
        When ``int()`` is called on an instance of ``DecimalDate``.

        >>> int(DecimalDate("2023_01_06"))
            20230106

        :return: integer representation of this instance.
        :rtype: int
        """
        return self.__dd_int

    #
    # convenience and utils
    #

    def year(self: Self) -> int:
        """
        Year (1-9999).

        >>> DecimalDate("2023_01_06").year()
            2023

        :return: Year (1-9999).
        :rtype: int
        """
        return self.__year

    def month(self: Self) -> int:
        """
        Month (1-12).

        >>> DecimalDate("2023_01_06").month()
            1

        :return: Month (1-12).
        :rtype: int
        """
        return self.__month

    def day(self: Self) -> int:
        """
        Day (1-31).

        >>> DecimalDate("2023_01_06").day()
            6

        :return: Day (0-31).
        :rtype: int
        """
        return self.__day

    def last_day_of_month(self: Self) -> int:
        """
        Day (28-31).

        >>> DecimalDate("2023_01_06").last_day_of_month()
            31

        >>> DecimalDate("2023_02_06").last_day_of_month()
            28

        >>> DecimalDate("2024_02_06").last_day_of_month()  # leap year
            29

        :return: Day (28-31).
        :rtype: int
        """
        return DecimalDate.__last_day_of_month(self.as_datetime())

    def weekday(self: Self) -> int:
        """
        The day of the week as an integer (0-6), where Monday == ``0`` ... Sunday == ``6``.

        :return: Day of the week (0-6)
        :rtype: int
        """
        return self.as_datetime().weekday()

    def isoweekday(self: Self) -> int:
        """
        The day of the week as an integer (1-7), where Monday == ``1`` ... Sunday == ``7``.

        :return: Day of the week (1-7)
        :rtype: int
        """
        return self.as_datetime().isoweekday()

    def isoformat(self: Self) -> str:
        """
        The decimal date formatted according to ISO ``yyyy-mm-dd``.

        >>> from decimaldate import DecimalDate
        >>> DecimalDate(2024_09_27).isoformat()
        '2024-09-27'

        To create a ``DecimalDate``from an ISO formatted date,
        use ``datetime.date.fromisoformat()`` or ``datetime.datetime.fromisoformat``.

        >>> from datetime import date
        >>> from decimaldate import DecimalDate
        >>> DecimalDate(date.fromisoformat('2024-09-27'))
        DecimalDate(20240927)

        :return: String representation formatted according to ISO.
        :rtype: str
        """
        return self.as_date().isoformat()

    def start_of_month(self: Self) -> DecimalDate:
        """
        The start date of the month and year of this instance.\\
        The day will always be ``1``.

        :return:  A new ``DecimalDate`` with the value of start-of-month.
        :rtype: DecimalDate
        """
        month_start: datetime = DecimalDate.__start_of_month(self.as_datetime())
        return DecimalDate(month_start)

    def end_of_month(self: Self) -> DecimalDate:
        """
        The end date of the month and year of this instance.\\
        For February the end day will be ``28`` or ``29`` depending on leap year.

        >>> DecimalDate("2023_01_06")
            DecimalDate(20230131)

        >>> DecimalDate("2023_02_06")
            DecimalDate(20230228)

        >>> DecimalDate("2024_02_06")
            DecimalDate(20240229)

        :return: A new ``DecimalDate`` with the value of end-of-month.
        :rtype: DecimalDate
        """
        return DecimalDate(DecimalDate.__end_of_month(self.as_datetime()))

    def split(self: Self) -> tuple[int, int, int]:
        """
        Return this object's integer value on the form ``yyyymmdd``
        as integer values for: year, month and day.

        >>> yyyy, mmm, dd = DecimalDate(2021_02_17).split()
        >>> print(yyyy, mmm, dd)
            2021 2 17

        :return: year, month, and day.
        :rtype: tuple[int, int, int]
        """
        return (self.__year, self.__month, self.__day)

    def clone(self: Self) -> DecimalDate:
        """
        Creates a new ``DecimalDate`` instance identical to original.

        Note that ``DecimalDate`` is immutable, so consider a regular assignment.

        >>> today = DecimalDate().today()
        >>> today.clone() == today
            True

        >>> today = DecimalDate().today()
        >>> today.clone() is today
            False

        :return: A new ``DecimalDate`` instance identical to original.
                 But not same reference.
        :rtype: DecimalDate
        """
        return DecimalDate(self.as_int())

    def next(self: Self, delta_days: int = 1) -> DecimalDate:
        """
        Creates a new ``DecimalDate`` instance ``delta_days`` days in the future.

        * The default argument value of ``1`` is the day after.
        * If the argument value is ``0`` then it the date of this instance.
        * If the argument is negative (<0) then it will be days in the past (opposite of future).

        :param delta_days: days in the future, defaults to ``1``.
        :type delta_days: int, optional
        :raises TypeError: if ``delta_days`` is not an ``int``.
        :return: A new ``DecimalDate`` offset with argument days.
        :rtype: DecimalDate
        """
        if not isinstance(delta_days, int):
            raise TypeError("argument for `next` is not `int`")
        next_date: datetime = self.as_datetime() + timedelta(delta_days)
        return DecimalDate(next_date)

    def previous(self: Self, delta_days: int = 1) -> DecimalDate:
        """
        Creates a new ``DecimalDate`` instance ``delta_days`` days in the past.

        * The default argument value of ``1`` is the day before.
        * If the argument value is ``0`` then it the date of this instance.
        * If the argument is negative (<0) then it will be days in the future (opposite of past).

        :param delta_days: days in the past, defaults to ``1``.
        :type delta_days: int, optional
        :raises TypeError: if ``delta_days`` is not an ``int``
        :return: A new ``DecimalDate`` offset with argument days.
        :rtype: DecimalDate
        """
        if not isinstance(delta_days, int):
            raise TypeError("argument for `previous` is not `int`")
        return self.next(-delta_days)

    #
    # As ...
    #

    def as_int(self: Self) -> int:
        """
        This ``DecimalDate`` instance's date as a ``int`` object on the form ``yyyymmdd``.

        Convenience method similar to ``int()``.

        >>> DecimalDate(2023_04_18).as_int()
            20230418

        >>> dd = DecimalDate(2023_04_18)
        >>> int(dd) == dd.as_int()
            True

        :return: Integer representation on the form ``yyyymmdd``.
        :rtype: int
        """
        return self.__dd_int

    def as_str(
        self: Self,
        sep: str | None = None,
    ) -> str:
        """
        This ``DecimalDate`` instance's date with an optional separator as a ``str`` object.

        >>> DecimalDate(2023_04_18).as_str()
            '20230418'

        >>> DecimalDate(2023_04_18).as_str('.')
            '2023.04.18'

        :param sep: Optional separator, defaults to ``None``.
        :type sep: str | None, optional
        :return: String representation on the form ``"yyyymmdd"``.
                 Or if separator then on the form ``"yyyy_mm_dd"`` where ``_`` is the separator.
        :rtype: str
        """
        if not sep:
            # None or empty string, then return the internal string value
            return self.__dd_str
        yyyy, mm, dd = self.split()
        return f"{yyyy:04d}{sep}{mm:02d}{sep}{dd:02d}"

    def as_date(self: Self) -> date:
        """
        This ``DecimalDate`` instance's date as a ``datetime.date`` object.

        :return: ``datetime.date`` representation.
        :rtype: date
        """
        return self.__dd_datetime.date()

    def as_datetime(self: Self) -> datetime:
        """
        This ``DecimalDate`` instance's date as a ``datetime.datetime`` object.

        :return: ``datetime.datetime`` representation.
        :rtype: datetime
        """
        return self.__dd_datetime

    #
    #
    #

    @classmethod
    def try_instantiate(
        cls,
        dd: DecimalDateInitTypes | DecimalDate | None = None,
    ):
        """
        A new instance of ``DecimalDate`` if successful;
        otherwise ``None``.

        If no argument is given then uses today's date.

        >>> dd: DecimalDate = DecimalDate.try_instantiate(2024_27_09)
        >>> if dd:
        >>>     print(f"success {dd}")
        >>> else:
        >>>     print(f"failure {dd}")
        success 20240927

        >>> dd: DecimalDate = DecimalDate.try_instantiate(2024_09_27)
        >>> if dd:
        >>>     print(f"success {dd}")
        >>> else:
        >>>     print(f"failure {dd}")
        failure None

        >>> DecimalDate.try_instantiate() == DecimalDate.today()
        True
        """

        try:
            return cls(dd)
        except (ValueError, TypeError):
            return None

    @classmethod
    def today(cls):
        """
        Todays's date as a ``DecimalDate`` instance.
        """
        return cls(cls.__today_as_int())

    @classmethod
    def yesterday(cls):
        """
        Yesterdays's date as a ``DecimalDate`` instance.
        """
        return cls.today().previous()

    @classmethod
    def tomorrow(cls):
        """
        Tomorrow's date as a ``DecimalDate`` instance.
        """
        return cls.today().next()

    @staticmethod
    def range(
        start: DecimalDate | DecimalDateInitTypes,
        stop: DecimalDate | DecimalDateInitTypes,
        step: int = 1,
        /,
    ) -> DecimalDateRange:
        """
        Return an object that produces a sequence of ``DecimalDate`` objects
        from ``start`` (inclusive) to ``stop`` (exclusive)
        by one day.

        Valid argument types are (except``None``) identical to ``DecimalDate``.

        >>> for dd in DecimalDate.range(2023_05_04, 2023_05_07):
        >>>     print(dd.as_str('.'))
        2023.05.04
        2023.05.05
        2023.05.06

        :param start: Sequence start (inclusive).
        :type start: DecimalDate | int | str | datetime
        :param stop: Sequence stop (exclusive).
        :type stop: DecimalDate | int | str | datetime
        """
        return DecimalDateRange(start, stop, step)

    @classmethod
    def count(
        cls,
        start: DecimalDate | DecimalDateInitTypes = None,
        step: int = 1,
    ) -> Generator[DecimalDate, Any, NoReturn]:
        """
        Make an iterator that returns evenly spaced decimal dates beginning with start.

        >>> from decimaldate import DecimalDate
        >>> for idx, dd in enumerate(DecimalDate.count(2024_03_01, 7)):
        >>>     if idx >= 6:
        >>>         break
        >>>     print(idx, dd.isoformat())
        0 2024-03-01
        1 2024-03-08
        2 2024-03-15
        3 2024-03-22
        4 2024-03-29
        5 2024-04-05

        Similar to ``itertools.count()``.
        https://docs.python.org/3/library/itertools.html#itertools.count
        intended for ``zip()`` and ``map()``.

        The iterator will continue until it reaches beyond valid ``decimal.date``values;
        eg. less than 1-1-1 (``datetime.MINYEAR``) or greater than 9999-12-31 (``datetime.MAXYEAR``)
        and then throw ``OverflowError``.

        :param start: The starting decimal date, defaults to ``None``. If no argument or ``None`` uses todays's date as start.
        :type start: DecimalDate | DecimalDateInitTypes, optional
        :param step: difference in day between dates in sequence, defaults to 1
        :type step: int, optional
        :raises TypeError: if ``start``is not a valid argument type for ``DecimalDate`` .
        :raises ValueError: if ``start``is not a valid date.
        :raises TypeError: if ``step``is not an integer.
        :raises ValueError: if ``step``is 0.
        :raises: OverflowError when generator reaches beyound valid ``datetime.date`` values (e.g. 9999-12-31).
        :yield: a sequence of evenly spaced decimal dates.
        :rtype: Generator[DecimalDate, Any, NoReturn]
        """
        if not isinstance(step, int):
            raise TypeError("count step argument is not an `int`.")
        if step == 0:
            raise ValueError("count step argument is 0.")

        dd: DecimalDate = cls(start)
        while True:
            yield dd
            dd = dd.next(step)


#
# DecimalDateRange
#

# TODO Implement step
# TODO Implement inverse argument order (start/stop)


class DecimalDateRange:

    # replace __dict__ : optimization and improving immutability
    __slots__ = (
        "_DecimalDateRange__start",
        "_DecimalDateRange__stop",
        "_DecimalDateRange__step",
        "_DecimalDateRange__length",
    )

    def __init__(
        self: Self,
        start: DecimalDate | DecimalDateInitTypes,
        stop: DecimalDate | DecimalDateInitTypes,
        step: int = 1,
        /,
    ) -> None:
        """
        Return an object that produces a sequence of ``DecimalDate`` objects
        from ``start`` (inclusive) to ``stop`` (exclusive)
        by ``step`` days
        (currently only value of step=1 is implemented).

        Valid argument types for ``start`` and ``stop``
        are identical to ``DecimalDate`` excepting ``None`` ('today').

        Start is expected to be before Stop or the sequence will be empty.

        >>> for dd in DecimalDateRange(2023_05_04, 2023_05_07):
        >>>     print(dd.as_str('.'))
            2023.05.04
            2023.05.05
            2023.05.06

        :param start: Sequence start (inclusive).
        :type start: DecimalDate | int | str | datetime
        :param stop: Sequence stop (exclusive).
        :type stop: DecimalDate | int | str | datetime
        :param step: Sequence step, defaults to 1 (on value of 1 is implemented)
        :type step: int, optional
        :raises ValueError: If any argument is ``None``
        :raises TypeError: If step argument is not instance of ``int``
        :raises ValueError: If step argument is ``0``
        :raises NotImplementedError: If step argument is other than ``1``
        """
        if start is None:
            raise ValueError("DecimalDateRange argument start is None.")
        if stop is None:
            raise ValueError("DecimalDateRange argument stop is None.")
        if step is None:
            raise ValueError("DecimalDateRange argument step is None.")
        if not isinstance(step, int):
            raise TypeError("DecimalDateRange step argument is not an `int`.")

        #
        # Instance variables
        # These have been placed in ``__slots__``
        #

        self.__start: DecimalDate
        """ The start of the decimal date range (*inclusive*). """

        self.__stop: DecimalDate
        """ The end of the decimal date range (*exclusive*). """

        self.__step: int
        """ The steps between items in the decimal date range from
        start (*inclusive*) to end (*exclusive*).

        A value of ``1`` will return every date in the decimal date range.

        *Currently only a value of ``1``is implemented*.
        """

        self.__length: int
        """ Internal instance value of the length of the range.\\
        The range start is *inclusive*.\\
        The range end is *exclusive*.
        """

        #

        self.__start = DecimalDate(start)
        self.__stop = DecimalDate(stop)
        self.__step = step

        if self.__step == 0:
            raise ValueError("DecimalDateRange argument step 0 is not valid.")

        if self.__step != 1:
            raise NotImplementedError(
                f"DecimalDateRange argument step {self.__step} != 1 is not implemented."
            )

        self.__length = (
            0
            if self.__start > self.__stop
            else (self.__stop.as_datetime() - self.__start.as_datetime()).days
        )

    def __iter__(self) -> Generator[DecimalDate, Any, None]:
        current: DecimalDate = self.__start
        while current < self.__stop:
            yield current
            current = current.next()

    def __len__(self) -> int:
        """
        The length operator, ``len()``.

        >>> len(DecimalDateRange(DecimalDate(2023_11_11), DecimalDate(2023_11_15)))
        4

        :return: Length of sequence.
        :rtype: int
        """
        return self.__length

    def __contains__(self, dd: DecimalDate) -> bool:
        """
        The containment-check operator, ``in``.

        >>> DecimalDate(2023_11_16) in DecimalDateRange(
        >>>     DecimalDate(2023_11_11), DecimalDate(2023_11_22)
        >>> )
        True
        """
        if not isinstance(dd, DecimalDate):
            raise TypeError(
                "DecimalDateRange contains argument is not a `DecimalDate`."
            )
        return self.__start <= dd < self.__stop

    def __getitem__(self, i: int) -> DecimalDate:
        """
        The index operator, ``[]``.

        >>> DecimalDateRange(2023_05_04, 2023_05_07)[2]
        DecimalDate(20230506)

        Negative argument is not implemented!

        :param i: index into range [0..len[.
        :type i: int
        :raises TypeError: If index is not an ``int``.
        :raises NotImplementedError: If index is negative (less than 0)
        :raises IndexError: If index is outside sequence [0..len[.
        :raises RuntimeError: If failed to compare index.
        :return: Object at index in sequence.
        :rtype: DecimalDate
        """
        if not isinstance(i, int):
            raise TypeError("DecimalDateRange index argument is not an `int`.")

        if i == 0:
            return self.__start

        if i > 0:
            if not (0 <= i < self.__length):
                raise IndexError(
                    f"DecimalDateRange object index {i} out of range: [0..{self.__length}[."
                )
            return self.__start.next(i)

        if i < 0:
            if not (-self.__length <= i < 0):
                raise IndexError(
                    f"DecimalDateRange object index {i} out of range: [-{self.__length}..0[."
                )
            return self.__stop.previous(-i)

        # To make `mypy` not complain about missing return statement -> exclude from coverage
        raise RuntimeError("Failure to compare argument")  # pragma: no cover
