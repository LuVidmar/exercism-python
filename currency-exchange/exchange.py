"""
This module has functions to exchange money.
"""


def exchange_money(budget: float, exchange_rate: float):
    """
    Gives the ammount of foreign currency you will own. 

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float):
    """
    Gives the remaining, unchanged ammount of money.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int):
    """
    Gives the total ammount of money.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return number_of_bills * denomination


def get_number_of_bills(budget: float, denomination: int):
    """
    Gives the number of bills (floor integer).

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget / denomination)


def get_leftover_of_bills(budget: float, denomination: int):
    """
    Gives the leftover change after exchanging bills
    
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int):
    """
    Gives the maximum ammount of bills you can exchange, taking into account spread
    
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    new_rate: float = exchange_rate * (1 + spread / 100)
    print("new_rate: " + str(new_rate))
    ammount_in_foreign = exchange_money(budget,new_rate)
    print(str(budget) + "USD is " + str(ammount_in_foreign) + "EUR")
    max_ammount_of_bills = get_number_of_bills(ammount_in_foreign,denomination)
    print("maxAmmount_of_bills: " + str(max_ammount_of_bills))

    return get_value_of_bills(denomination,max_ammount_of_bills)