#!/usr/bin/python
# coding: UTF-8
"""
    Task:
    Write a software library that accepts 2 version string as input and returns
    whether one is greater than, equal, or less than the other. As an example: '1.2' is greater than '1.1'.
    Provide all test cases you could think of.


    Returning result of string comparison
    Testcases
    1. string and int ( 'banana' and 10 )
    2. different strings ( 'banana' and 'banan' )
    3. lowercase and uppercase same string ( 'Banana' and 'banana' )
    4. int and float ( 10 and 10.1 )
    5. float and float ( 1.2 and 1.3 )
    6. values not None

"""

import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('str', nargs='+')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.str is not None:
        first_string = namespace.str[0]
        second_string = namespace.str[1]

        if first_string < namespace.str[1]:
            result = '{} is less than {}'.format(first_string, second_string)
        elif first_string == second_string:
            result = '{} is equal {}'.format(first_string, second_string)
        else:
            result = '{} is greater than {}'.format(first_string, second_string)
    else:
        result = None
    print(result)
