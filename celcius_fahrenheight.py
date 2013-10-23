#!/usr/bin/env python
'''\
Write two functions that will convert temperatures back and forth from the 
Celsius and Fahrenheit temperature scales. The formulas for making the 
conversion are as follows:

  Tc=(5/9)*(Tf-32)
  Tf=(9/5)*Tc+32

where Tc is the Celsius temperature and Tf is the Fahrenheit temperature. More 
information and further descriptions of how to do the conversion can be found 
at this NASA Webpage. If you finish this assignment quickly, add a function to 
calculate the wind chill.
Input

Your program should ask the user to input a temperature and then which 
conversion they would like to perform.

source:http://openbookproject.net/pybiblio/practice/\
'''


def fahrenheight_to_celcius(temp):
    '''\
    Take a Fahrenheight temperature and convert it to Celcius
    
    :param temp: Fahrenheight temperature
    :type temp: float
    :returns: Celcius temperature
    :rtype: float\
    '''
    return (5 / 9) * (temp - 32)


def celcius_to_fahrenheight(temp):
    '''\
    Take a Celcius temperature and convert it to Fahrenheight
    
    :param temp: Celcius temperature
    :type temp: float
    :returns: Fahrenheight temperature
    :rtype: float\
    '''
    return (9 / 5) * temp + 32


def main():
    '''\
    Ask the user whether they would like to convert celcius to fahrenheight
    or fahrenheight to celcius. Then ask them for the temperature that they
    would like to convert\
    '''
    conversion_type = input(
        "Convert to (F)ahrenheight or (C)elcius: ").lower()[0]
    temp = float(input("Enter the temperature you would like to convert: "))
    conversion_map = {"c": fahrenheight_to_celcius,
                      "f": celcius_to_fahrenheight}
    converted_value = conversion_map[conversion_type](temp)
    print(converted_value)
    return converted_value

if __name__ == "__main__":
    main()
