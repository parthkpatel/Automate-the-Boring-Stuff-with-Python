# A program that will detect valid dates between the years 1000 and 2999

import re


def detect_date(text):
    dateRegex = re.compile(r'''
    (([0-3])?\d)/           # DD/ check, also allow for D/ for Days 1-9 of a month
    (([0-1])?\d)/           # MM/ check, also allow for M/ for months January - September
    ([1-2]\d\d\d)           # YYYY check, allows years between 1000-2999
    ''', re.VERBOSE)

    mo = dateRegex.search(text)
    groups = mo.groups()
    day = groups[0]
    month = groups[2]
    year = groups[4]

    dayInt = int(day)
    monthInt = int(month)
    yearInt = int(year)

    if monthInt in (4, 6, 9, 11) and dayInt > 30:
        return "Nonexistent Date Provided"
    elif monthInt == 2:
        isLeapYear = yearInt % 4 == 0 and (yearInt % 100 != 0 or yearInt % 400 == 0)
        if (isLeapYear is True and dayInt > 29) or (isLeapYear is False and dayInt > 28):
            return "Nonexistent Date Provided"
    elif dayInt > 31:
        return "Nonexistent Date Provided"

    return '/'.join([day, month, year])


if __name__ == '__main__':
    print(detect_date('The date today is 31/01/2014'))
    print(detect_date('The date today is 29/02/2020'))
    print(detect_date('The date today is 29/02/1900'))
    print(detect_date('The date today is 29/02/2100'))
    print(detect_date('The date today is 29/02/2400'))
    print(detect_date('The date today is 6/6/2020'))
    print(detect_date('The date today is 11/6/2000'))
