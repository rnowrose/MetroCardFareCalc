from MetroCardMachine import MetroCardBalance, MTATransportation


def num_trips_using_base_fare(total_balance, base_fare):
    num_trips = total_balance / base_fare
    remaining_balance = total_balance % base_fare
    return int(num_trips), remaining_balance


def num_info_using_different_transit(metro_card_balance):
    count = 0
    balance = metro_card_balance.show_balance()
    mtaTransportation = MTATransportation()
    transit_list = []
    transit_fare = []
    while balance > 2.75:
        transportation = input("Enter Transit: ")
        if transportation not in mtaTransportation.get_all_transit_info().keys():
            continue
        balance = metro_card_balance.deduct_balance(transportation)
        transit_list.append(transportation)
        transit_fare.append(mtaTransportation.get_transportation_fare(transportation))
        count += 1

    return transit_list, transit_fare, count


def transit_usage_log(amount):
    mtaTransportation = MTATransportation()
    metro_card_balance = MetroCardBalance(mtaTransportation)
    metro_card_balance.add_balance(amount)
    transit_data = num_info_using_different_transit(metro_card_balance)
    total = 0
    print("Name: Ron Karim")
    print('Public Transportation ridden: ')
    for transit in transit_data[0]:
        print(transit)

    print('Public Transportation Fares Paid: ')
    for fare in transit_data[1]:
        print(fare)
        total += fare

    print(total)
    print('Number Of Trips Made until low balance: ' + str(transit_data[2]))




