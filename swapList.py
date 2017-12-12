
def swap(val):
    """
    swap the first half of the list with the second half of the list
    :param val: input array
    :return: swapped array
    """
    width = len(val)//2
    return val[width:] + val[:-width]


def main():
    val = [9, 13, 21, 4, 11, 7, 1, 3]
    print (val)
    val = swap(val)
    print(val)


if __name__ == '__main__':
    main()