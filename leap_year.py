#!/usr/bin/env python
'''\
Leap years occur according to the following formula: a leap year is divisible 
by four, but not by one hundred, unless it is divisible by four hundred. 
For example, 1992, 1996, and 2000 are leap years, but 1993 and 1900 are not. 
The next leap year that falls on a century will be 2400.

source:http://openbookproject.net/pybiblio/practice/\
'''
 
def leap_year_check(year):
    '''\
    Takes a year as input and then returns True or False depending on if the
    year is a leap year or not
    
    :param year: Year to check
    :type year: int
    :returns: Whether a year is leap or not
    :rtype: boolean\
    '''
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        
        return True
    return False
 
 
def main():
    '''\
    Ask the user for a year as input and then return whether the year is a leap
    year or not\
    '''
    year = int(input("Enter the year that you want to check is leap or not: "))
    is_leap = leap_year_check(year)
    results = {True: "The year, {0}, is a leap year", 
               False: "The year, {0}, is not a leap year"}
    print(results[is_leap].format(year))
    return is_leap
    
if __name__ == "__main__":
    main()
