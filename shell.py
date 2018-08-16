from inventory import *
from time import sleep
from datetime import datetime
from termcolor import colored, cprint
from disk import *

# make a dictionary for every item
# rental_code is needed
# days_rented is needed
# condition_rented is needed
# condition_returned is needed
# inital_price (basecharge) is needed
# price_after_days is needed

# if the customer rents an item for one day it's just the initial
# price for each day past that then it adds a dollar to the total

# def login():
# while True:
# user = input("[C]ustomer\n[E]mployee\n[L]eave\n<<<")
# if user.upper() == "C":
# return user.upper()
# if user.upper() == "E":
# return user.upper()
# if user.upper() == "L":
# return user.upper()
# else:
# print('Incorrect try again ')


def user_choice():

    choice = input("Are you a Customer or an Employee? ").upper()
    return choice
    if choice == 'CUSTOMER':
        return choice
    elif choice == "EMPLOYEE":
        return choice
    else:
        cprint('Would you please try again?', 'red', 'on_white')
        user_choice


def customer_choice():
    while True:
        choice = input
    choice = input("Would like to rent or return an item? ")
    if choice == 'RENT'.lower():
        return load_inventory()
    elif choice == 'RETURN'.lower():
        return return_item()
    else:
        print("Error ")
        customer_choice


def days():
    days = input("How long do you you plan on renting this item? ")
    max_days = 7
    min_days = 1
    days = customer_choice


def items_in_inventory():
    items = open('inventory.py', 'r')
    items = items.read()
    print(items)


def choose_item():
    items_in_inventory()
    choice = input('What item are you seeking? ')


def item_value():
    item_value = initial_price * 2.00


def input_rent_item(item_type):
    while True:
        rent_item = input('Movies:', 'Games:', 'Anime:')
        if rent_item in item_type:
            return rent_item
        else:
            print("Error please try again but with something vaild. ")


def rental_sale():
    cost = rental_price * number_of_days
    tax = cost * 0.07
    deposit = item_value * 0.10
    rental_sale = cost + tax + deposit
    return rental_sale


def return_item():
    choice = input('Are you returning a movie, game, or an anime? ')
    if choice in inventory:
        print(choice)


def main():
    #transactions = [replacement]
    #return replacement
    #{"Name": "Item Name", "Director", "Genre", "Initial Price", "Replacement"}
    choice = user_choice()
    if choice == 'CUSTOMER':
        choice = customer_choice()
        if choice == 'rent':
            # days
            # rent item
            if choice == 'return':
                print(return_item())
                if choice == 'EMPLOYEE':
                    print(history())

    print(items_in_inventory())


if __name__ == '__main__':
    main()
