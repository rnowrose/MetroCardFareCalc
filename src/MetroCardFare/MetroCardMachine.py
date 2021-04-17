class MTATransportation:
    def __init__(self):
        self.transportation = {'NYC Local Bus': 2.75, 'NYC Subway': 2.75, 'Airtrain JFK': 7.75, 'Express Bus': 6.75,
                               'PATH': 2.75, 'Beeline System': 2.75, 'NICE': 2.75}

    def get_transportation_fare(self, transit_name):
        if transit_name not in self.transportation.keys():
            return 0
        else:
            return self.transportation[transit_name]

    def get_all_transit_info(self):
        return self.transportation

    def add_transit_system(self, transit_name, fare):
        self.transportation[transit_name] = fare


class MetroCardBalance:
    METROCARD_FEE = 1

    def __init__(self, transportation, balance=1):
        self.transportation = transportation
        self.balance = balance - self.METROCARD_FEE

    def add_balance(self, amount):
        self.balance += amount
        if self.balance > 100:
            raise BalanceFullException("Fare Cannot Go Over 100")
        return self.balance

    def show_balance(self):
        return self.balance

    def deduct_balance(self, transit_name):
        if self.balance < 0:
            raise InsufficientBalanceException()

        self.balance -= self.transportation.get_transportation_fare(transit_name)
        return self.balance


class BalanceFullException(Exception):
    def __init__(self, message='Balance is full'):
        self.message = message


class InsufficientBalanceException(Exception):
    def __init__(self, message='Insufficient Balance'):
        self.message = message
