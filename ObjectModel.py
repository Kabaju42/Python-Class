def modify(k):
    """
    Modifieds the contenet of my list
    :param k: list
    :return: nothing
    """
    k.append(33)
    print("k= ", k) # this appends the calling parameter

def replace(g):
    """
    Replace the content of the list
    :param g: lisgt object
    :return: nothing
    """
    g = [17, 36, 22, 33] # this does not modify the calling paramater
    print("g = ", g)

def update_info(var_in):
    """
    Add 1 to each element in array var_in
    :param var_in: array to update
    :return: Nada
    """
    for i in range (0, len(var_in)):
        var_in[i] += 1

def banner(message, border='*'):
    """
    Display message surrounded by border
    :param message: message string
    :param border: border style <char> - optional
    :return: Nothing
    """
    # bstring = ''
    # i = message.__len__()
    # while i != 0:
    #     #bstring.append(border(0))
    #     bstring = bstring + border
    #     i -= 1
    bstring = border * (len(message) + 2)
    print(bstring)
    print(border + message + border)
    print(bstring)

# always use immutable objects such as integer
# or strings for default values
def add_spam(menu=None):
    """
    Add spam to my list
    :param menu: optional list object
    :return: manu
    """

    if menu is None:
        menu = []
    menu.append("spam")
    return menu

def number_info():
    """
    Write a funciton that prompts the user
    for two integers, then it prints: The sum, difference,
    product, the average, and the distance (abs value),
    the maximum, and the and the minimum
    :return:
    """
    print("What's your first number")
    x = int(input())
    print("What's your second number")
    y = int(input())

    print("Sum = " + str(x+y) )
    d = (x-y)
    print("Difference = " + str(d))
    print("product = " + str(x*y))
    print("average = " + str((x+y)/2))
    print("distance = " + str(abs(d)))
    print("Max = " + str(max(x, y)))
    print("Min = " + str(min(x, y)))


def main():
    m = [9, 12, 45]
    print("m = ", m)
    modify(m)
    print("m = ", m)
    replace(m)
    print("After replace, m= ", m)

    update_info(m)
    print("after update, m = ", m)

    # use all parameters
    banner('USU Rocks!', 'x')

    # use required params
    banner('WSU is OK too')

    #use parameters by name
    banner(border = "@", message = "Don't forget NPS!")

if __name__ == "__main__":
    main()