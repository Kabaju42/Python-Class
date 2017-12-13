"""
Module to demonstrate generator execution
"""


def take(count, iterable):
    """
    Take items from the front of an iterable
    :param count: maximum number of items to retrieve
    :param iterable: The source series
    :yields at most 'count' items for that iterable
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_test():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """
    Returns unique items by elimiating duplicates
    :param iterable: The source series
    :yield: Unique elements in order form 'iterable"
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [1, 1, 2, 5, 8, 13, 21, 34]
    for item in distinct(items):
        print(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


def main():
    #run_test()
    #print("\n\n\n")
    #run_distinct()
    run_pipeline()


if __name__ == '__main__':
    main()