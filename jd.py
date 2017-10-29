# p.27, section 3

from math import trunc

# Note that trunc(-7.83) = -7.  This is the expected result for negative numbers in this module.


def jd(yyyy, mm, dd):
    """
    Julian Date
    Continuous count of days and fractions since noon UT on January 1, 4713 BC
    Meeus, p.28
    :param yyyy: negative, positive or 0
    :param mm: 1 to 12
    :param dd: 0.0 to 31.99
    :return: Julian Date
    """

    def ge_reform_day():
        if yyyy < 1582:
            return False
        if yyyy > 1582:
            return True

        if mm < 10:
            return False
        if mm > 10:
            return True

        if dd < 15:
            return False
        return True

    y = yyyy
    m = mm
    if mm < 3:
        y = yyyy-1
        m = mm + 12

    b = 0
    if ge_reform_day():
        a = trunc(y/100)
        b = 2 - a + trunc(a/4)

    c = trunc(365.25 * y)
    if y < 0:
        c = trunc(365.25 * y - 0.75)
    ret_jd = c + trunc(30.6001 * (m+1)) + dd + 1720994.5 + b
    return ret_jd


def mjd(jul_date):
    """
    Returns Modified Julian Date
    :param jul_date: Julian Date
    :return: Modified Julian Date
    """
    return jul_date - 2400000.5


def cd(jul_date):
    """
    Calendar Date
    Meeus, p.29
    :param jul_date: Julian Date, positive
    :return: yyyy, mm, dd
    """
    jdm = jul_date + 0.5
    z = trunc(jdm)
    f = jdm - z

    a = z
    if z >= 2299161:
        alpha = trunc((z - 1867216.25) / 36524.25)
        a = z + 1 + alpha - trunc(alpha / 4)

    b = a + 1524
    c = trunc((b - 122.1) / 365.25)
    d = trunc(365.25 * c)
    e = trunc((b - d) / 30.6001)

    dd = round(b - d - trunc(30.6001 * e) + f, 4)

    mm = e - 1
    if mm >= 13:
        mm -= 12

    if mm >= 3:
        yyyy = c - 4716
    else:
        yyyy = c - 4715

    return yyyy, mm, dd


def dow(yyyy, mm, dd):
    """
    Day of Week
    Meeus, p.31
    :param yyyy: negative, positive or 0
    :param mm: 1 to 12
    :param dd: 1.0 to 31.00
    :return: 0 - Sunday, 1 - Monday, ... 6 - Saturday
    """
    return round((jd(yyyy, mm, trunc(dd)) + 1.5) % 7)


def leap_year(yyyy):
    """
    Returns true if leap year
    :param yyyy: year
    :return: True if leap, otherwise, false
    """
    if yyyy % 400 == 0:
        return True

    if yyyy % 100 == 0:
        return False

    return yyyy % 4 == 0


def doy(yyyy, mm, dd):
    """
    Day of Year
    Meeus, p.31
    :param yyyy:
    :param mm:
    :param dd:
    :return:
    """
    a = trunc((mm + 9) / 12.0)

    res = trunc(275 * mm / 9.0) - a + trunc(dd) - 30.0
    if not leap_year(yyyy):
        res -= a

    return round(res)


def cd_diff(cd1, cd2):
    """
    Difference in days between two calendar dates
    :param cd1: (yyyy, mm, dd)
    :param cd2: (yyyy, mm, dd)
    :return: difference in days
    """
    return jd(cd2[0], cd2[1], cd2[2]) - jd(cd1[0], cd1[1], cd1[2])


def cd_by_num(yyyy, num):
    """
    Returns calendar date by the number of the day in the year
    :param yyyy: year
    :param num: day number
    :return: calendar date
    """
    return cd(jd(yyyy, 1, 0) + num)


def cd_inc(yyyy, mm, dd, cnt):
    """
    Returns the calendar date that is apart from the given date by any number of days
    :param yyyy: year
    :param mm: month
    :param dd: day
    :param cnt: number of days, can be negative
    :return: calendar date
    """
    return cd(jd(yyyy, mm, dd) + cnt)


if __name__ == "__main__":
    # tests
    print(jd(1957, 10, 4.81))  # 2436116.31
    print(jd(333, 1, 27.5))    # 1842713.0
    print(jd(-584, 5, 28.63))  # 1507900.13

    print(cd(jd(1957, 10, 4.81)))
    print(cd(jd(333, 1, 27.5)))
    print(cd(jd(-584, 5, 28.63)))

    print(cd_diff((1835, 11, 16), (1910, 4, 20)))  # 27,183
    print(cd_diff((2016, 1, 1), (2017, 1, 1)))     # 366
    print(cd_by_num(1900, 1))                      # 1900 Jan 1
    print(cd_by_num(2017, 365))                    # 2017 Dec 31
    print(cd_inc(1954, 6, 30, 10000))              # 1981 Nov 15
    print(cd_inc(2017, 10, 30, -1))                # 2017 Oct 29

    print(dow(1954, 6, 30))   # 3 - Wednesday
    print(dow(2017, 10, 29))  # 0 - Sunday

    print(doy(1978, 11, 14))  # 318
    print(doy(1980, 4, 22))   # 113
    print(doy(1600, 12, 31))  # 366
