"""
Model for aircraft flights
"""

class Flight:
    def __init__(self, number, aircraft):
        if len(number) != 5:
            print('wrong length')
            raise ValueError
        if not str.isalpha(number[:2]):
            print('not alpha')
            raise ValueError
        if not str.isupper(number[:2]):
            print('not upper')
            raise ValueError
        if not str.isnumeric(number[2:]):
            print('not number')
            raise ValueError
        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model


class Aircraft:
    """

    """
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        if num_seats_per_row > 10 :
            raise ValueError ("Invalid seating setup")
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats = num_rows * num_seats_per_row
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    #Seating plan: "ABCDEFGHJK"
    def seating_plan(self):
        """
        Produces an iterable sequence of row number up to the number of rows in the plane.
        The string and its lice method return a strign witone character per row.
        These two objects the range, and the string are bundled into a tuple.
        :return:
        """
        return (range(1, self._num_rows+1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


def main():
    """
    Test Function
    :return:
    """
    # f = Flight ("AA123")
    # print(f.number())
    # print(f.airline())
    #
    a = Aircraft('FCC', 'hopper', num_rows=22, num_seats_per_row=6)
    # print(a.registration())
    # print(a.model())
    # print(a.seating_plan())

    f = Flight("AA777", a)
    print(f.aircraft_model())

if __name__ == '__main__':
    main()