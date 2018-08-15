import sys
from time import sleep
from datetime import datetime
from termcolor import cprint
from disk import *

# rental_code is needed
# days_rented is needed
# condition_rented is needed
# condition_returned is needed
# inital_price (basecharge) is needed
# price_after_days is needed

def days():
    max_days = 7
    min_days = 1 


def user_choice():

    choice = input("Are you a Customer or an Employee? ").upper()
    return choice
    if choice == 'CUSTOMER':
        return choice
    if choice == "EMPLOYEE":
        return choice
    else:
        cprint('Would you please try again?', 'red', 'on_white')
        user_choice


def customer_choice():
    choice = input("Would like to rent or return an item? ")
    if choice == 'rent':
        days = input("How long do you you plan on renting this item? ")
        return days
    if choice == 'return':
        print("Did you enjoy it? ")
    else:
        print("Error ")


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
    if rental_code == 'D':
        print('How many days are you renting this for? ')
    if rental_code == 'W':
        print('How many weeks are you renting this for? ')


def main():
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

# Games
# Final Fantasy XV,Hajime Tabata,RPG,1.25,new,1.26
# Final Fantasy VII,Yoshinori Kitase,ATB Turn Based RPG,0.50,pre-owned,0.51
# Uncharted 3 Drakes Deception,Amy Henning,Adventure,2.00,pre-owned2.01
# Uncharted 4 A Thiefs End,Amy Henning,Adventure,3.75,new,3.76
# Saints Row IV,Steve Jaros,Action,3.50,pre-owned,3.51

# Anime
# Fairy Tail,Hiro Mashima,Action,0.25,new,0.26
# Seven Deadly Sins,Nakaba Suzuki,Fantasy,0.50,pre-owned,0.51
# Full Metal Alchemist,Hiromu Arakawa,Action,1.25,new,1.26
# Dragon Ball Z,Akria Toriyama,Martial Arts,0.50,new,0.51
# My Hero Academia,Kohei Horikoshi,Super Hero,1.50,new,1.51
