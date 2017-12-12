# could do "from scope import *"
# good for development, bad for release

count = 0 # global variable


def show_count():
    print(count)


def set_count(c):
    global count #use the global variable - don't create a local one
    count = c


