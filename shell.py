from disk import *


def category_choice():
    """ These are the entertainment choices you have to choose from."""
    category = ['games', 'movies', 'anime']
    while True:
        choice = input('Games, Movies, or Anime? ')
        if choice.lower() in category:
            category_choice = ('{}.txt'.format(choice.lower()))
            return category_choice
        else:
            print('That is an invalid operation please try again. ')


def search_for_string(string, lines):
    ''' This searches the text files and tries to find the item or 
    related items and returns them. '''
    number = 0
    for line in lines:
        number += 1
        if string.lower() in line.lower():
            print('{}: {}'.format(number, line))


def item_price(item_type):
    ''' str -> float

    Returns the price of the selected item

    >>> item_price('Game')
    5.00
    >>> item_price('Movies')
    5.25
    >>> item_price('Anime')
    4.00
    '''
    if item_type == 'Game':
        return 5.00
    if item_type == 'Movies':
        return 5.25


def price_history(payment, rent_rate, item_name):
    time = datetime.now()
    text = '\n{}, {}, {},'.format(payment, rent_rate, item_name)
    with open('history.txt', 'a') as file:
        file.write(text)


def main():
    choice = category_choice()
    string = input('Title:')
    lines = open_file(choice)
    search_for_string(string, lines)


if __name__ == '__main__':
    main()
