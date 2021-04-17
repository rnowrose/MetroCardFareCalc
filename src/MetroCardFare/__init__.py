import MetroCardMachine, MetroCardTrips

if __name__ == '__main__':
    transit = MetroCardMachine.MTATransportation()
    metro_card = MetroCardMachine.MetroCardBalance(transit)
    metro_card.balance = metro_card.balance + 120

    print(metro_card.show_balance())

    MetroCardTrips.transit_usage_log(metro_card.show_balance())
