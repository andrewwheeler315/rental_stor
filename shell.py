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
    choice = input("Would like to rent or return an item? ")
    if choice == 'rent':
        return days
    elif choice == 'return':
        print("Did you enjoy it? ")
    else:
        print("Error ")

def days():
    days = input("How long do you you plan on renting this item? ")
    max_days = 7
    min_days = 1 
    days = customer_choice

def items_in_inventory():
    items = open('inventory.txt', 'r')
    items = items.read()
    print(items)

def return_item():
    


def choose_item():
    items_in_inventory()
    choice = input('What item are you seeking? ')


def rental():
    rental_code = input("(I)nitial Price, (D)aily, or (W)eekly?\n").upper()
    rental_period = input("Number of weeks rented:\n")

    if rental_code == 'I':
        print('The initial price for that item is: ')
    elif rental_code == 'D':
        print('How many days are you renting this for? ')
    elif rental_code == 'W':
        print('How many weeks are you renting this for? ')


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
        elif choice == 'return':
            # return item
    elif choice == 'EMPLOYEE':
        print(history())

    print(items_in_inventory())


if __name__ == '__main__':
    main()

