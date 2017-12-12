# Python uses the keyword def to celdare a function or definition

def hello():
    print("Hello world")

def even_or_odd(n):
    if n%2 == 0:
        print("even")
        return
    else:
        print("odd")
        return

if __name__ == "__main__":
    # test the code
    hello()
    even_or_odd(1)
    even_or_odd(2)
    print(__name__)