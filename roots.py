import sys

def sqrt(x):
    """
    Compute the square root using the method of
    Heron of Alexandria
    :param x: The nubmer for which the square root is to be computed
    :return: square root of x
    :raise:ValueError on negative numbers
    """

    if x <= 0:
        # less expensive to raise the error and avoid the try block
        raise ValueError("Cannot compute square root of a negative number")

    guess = x
    i = 0
    try:
        while(guess * guess != x and i < 20):
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(0))
        print(sqrt(-1))
        print('This is never printed')
    except ZeroDivisionError:
        print("Cannot compute square root of negative numbers")
    except ValueError as e:
        print(e, file=sys.stderr)

    print("Program execution continues here")

if __name__ == '__main__':
    main()



