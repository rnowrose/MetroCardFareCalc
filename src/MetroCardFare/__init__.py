import MetroCardMachine, MetroCardTrips

if __name__ == '__main__':
    transit = MetroCardMachine.MTATransportation()
    metro_card = MetroCardMachine.MetroCardBalance(transit)
    metro_card.add_balance(10)
    MetroCardTrips.transit_usage_log(metro_card.show_balance())


