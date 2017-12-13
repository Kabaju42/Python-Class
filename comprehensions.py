from math import sqrt
from pprint import pprint as pp


def is_prime(x):
    """
    Tests for prime
    :param x:
    :return:
    """
    if x < 2:
        return False

    for i in range (2, int(sqrt(x)) +1):
        if x % i == 0:
            return False
    return True

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        return ValueError("Iterable is empty")


def gen246():
    print('about to yield2')
    yield 2
    print('about to yield4')
    yield 4
    print('about to yield6')
    yield 6
    print('about to return')
    return


def main():
    """
    Test function
    :return:
    """

    # # Filter predicates
    l = 1
    # l = [x for x in range (1000001) if is_prime(x)]
    # pp(l)
    # print(len(l))





if __name__ == '__main__':
    main()
    exit(0)