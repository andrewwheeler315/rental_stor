from time import sleep
from datetime import datetime
from termcolor import colored, cprint
import disk
import core


def user_choice():

    choice = input("Are you a Customer or an Employee? ")
    return choice
    if choice == 'CUSTOMER':
        return choice
    elif choice == "EMPLOYEE":
        return choice
    else:
        cprint('Would you please try again?', 'red', 'on_white')
        user_choice


def customer_choice(inventory):
    choice = input('1--Return\n2--Rent\n3--Leave')
    if choice == '1':
        customer_return(inventory)
        exit()
    elif choice == '2':
        item = customer_rental(inventory)
        return item
    elif choice == '3':
        print('I hope you have nice day. ')
        exit()


def customer_return(inventory):
    while True:
        options = core.make_inven_options(inventory)
        choice = input(
            f'What items are you going to return today\n{options}\n???')
        if choice in options:
            item = inventory[choice]
            if core.can_return(item) == True:
                item['Stock'] += 1
                fee = core.deposit_fee(item)
                print(
                    f'Thank You for returning. Here is your deposit of $ {fee}'
                )
                disk.write_to_file_inven(inventory)
                exit()
            else:
                print("Hey this item isn't returnable. ")
                exit()
        else:
            print('You obviously can\'t do that. ')


def customer_rental(inventory):
    options = core.make_inven_options(inventory)
    print(f'These are the items that are available\n{options}')
    while True:
        choice = input("Now what would you like to rent. ")
        if choice in options:
            item = inventory[choice]
            if core.is_in_stock(item) == True:
                item['Stock'] -= 1
                return item
        else:
            print('This item isn\'t able to be rented. ')


def employee_choice(inventory):
    print(
        'Employee options :\n1--Check Stock\n2--Review Transaction History\n3--View Revenue\n4--Clockout'
    )
    while True:
        choice = input('Option you\'d like to choose. ')
        if choice == "1":
            inven = disk.open_file('inventory.txt')
            inven = core.employee_inven(inven)
            print(inven)
        elif choice == "2":
            receipt = disk.open_file_history()
            print(receipt)
        elif choice == "3":
            print(disk.revenue())
        elif choice == "4":
            print('Have a nice day. ')
            exit()
        else:
            print('Nein that won\'t work ')


def choose_days():
    while True:
        days = input('How many days')
        if days.isdigit():
            return days
        else:
            print('I\'m sorry but that is a invalid amount of time. ')


def main():
    store = True
    inventory = disk.open_file('inventory.txt')
    while store != False:
        choice = user_choice()
        if choice.upper() == 'C':
            item = customer_choice(inventory)
            fee_1 = core.deposit_fee(item)
            print(f'The deposit fee is ${fee_1}')
            days = choose_days()
            fee_2 = core.total_rental_fee(item, days)
            print(f'The total rental fee is s{fee_2}')
            print('Hope you have a good day.')
            disk.write_to_file_inven(inventory)
            time = datetime.now()
            name = item['Name']
            history = core.make_history(time, name, days, fee_1, fee_2)
            disk.write_to_file_history(history)
            store = False
        elif choice.upper() == 'E':
            employee_choice(inventory)


if __name__ == '__main__':
    main()
