import MetroCardMachine, MetroCardTrips

if __name__ == '__main__':
    transit = MetroCardMachine.MTATransportation()
    metro_card = MetroCardMachine.MetroCardBalance(transit)
    metro_card.balance = metro_card.add_balance(150)

    print(metro_card.show_balance())

    MetroCardTrips.transit_usage_log(metro_card.show_balance())


#Sample Output
"""
15
Enter Transit: PTH
Invalid Data or Insufficient Fare
Enter Transit: PATH
12.25
Enter Transit: NYC Subwau
Invalid Data or Insufficient Fare
Enter Transit: NYC Subway
9.5
Enter Transit: NICE
6.75
Enter Transit: Express Bus
0.0
Name: Ron Karim
Public Transportation Fares Paid: 
$2.75
$2.75
$2.75
$6.75
Total Fares Paid: $15.0
Number Of Trips Made until insufficient balance: 4
Number Of Times Commuted on Particular Public Transit: {'PATH': 1, 'NYC Subway': 1, 'NICE': 1, 'Express Bus': 1}

"""

"""
15
Enter Transit: NYC Subway
12.25
Enter Transit: NICE
9.5
Enter Transit: NYC Subway
6.75
Enter Transit: Beeline System
4.0
Enter Transit: P
Invalid Data or Insufficient Fare
Enter Transit: PATH
1.25
Name: Ron Karim
Public Transportation Fares Paid: 
$2.75
$2.75
$2.75
$2.75
$2.75
Total Fares Paid: $13.75
Number Of Trips Made until insufficient balance: 5
Number Of Times Commuted on Particular Public Transit: {'NYC Subway': 2, 'NICE': 1, 'Beeline System': 1, 'PATH': 1}

"""

#This exception is thrown as metrocard cannot have balance over 100
"""
150
Traceback (most recent call last):
  File "/Users/rownoknowrose/Desktop/ProgrammingFiles/CSCourse/MetroCardTransitInfo/src/MetroCardFare/__init__.py", line 10, in <module>
    MetroCardTrips.transit_usage_log(metro_card.show_balance())
  File "/Users/rownoknowrose/Desktop/ProgrammingFiles/CSCourse/MetroCardTransitInfo/src/MetroCardFare/MetroCardTrips.py", line 41, in transit_usage_log
    raise BalanceFullException("Fare Cannot Go Over 100")
MetroCardMachine.BalanceFullException: Fare Cannot Go Over 100
"""