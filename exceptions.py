"""
Test exceptions in python
"""

import sys
from math import log

def convert(s):
    """
    Convert an integer
    :param s: Object to convert
    :return: integer object
    :raise: ValueError, TypeError
    """
    try:
        return int(s)
        #print('Conversion succeeded x = ', x)
    except (ValueError, TypeError) as e:
        print('Conversion failed: {}'.format(str(e)),
              file=sys.stderr)
        raise # re-raise the error - have someone else handle it

    return -1


def string_log(s):
    try:
        v = convert(s)
        return log(v)
    except (ValueError, TypeError) as e:
        print('Conversion failed: {}'.format(str(e)),
              file=sys.stderr)
    return -1


def main():
    # i = convert (55)
    # print(i)
    #
    # i = convert(str(55))
    # print(i)
    #
    # i = convert("Hello") # creates ValueError
    # print(i)
    #
    # i = convert([1, 2, 3])  # creates TypeError
    # print(i)

    i = string_log(55)
    print(i)

    i = string_log('Hello')
    print(i)

if __name__ == '__main__':
    main()

