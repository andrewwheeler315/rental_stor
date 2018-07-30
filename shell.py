#from disk import *
from games import *
from anime import *
from movies import *


def get_category():
    """ () -> str
    
    Asks the user which type of item they would like to rent.
    """
    category = ['games', 'movies', 'anime']
    while True:
        choice = input('Games, Movies, or Anime? ')
        if choice.lower() in category:
            category_choice = ('{}.txt'.format(choice.lower()))
            return category_choice
        else:
            print('That is an invalid operation please try again. ')


def item_in_category_quantity(item_type):
    ''' str -> dic

    Returns the quantity of the provided item.

    >>> item_quantity('Games')
    Games.keys()
    >>> item_quantity('Anime')
    Anime.keys()
    >>> item_quantity('Movies')
    Movies.keys()
    '''
    if item_type == 'Anime':
        return self.Anime
    elif item_type == 'Games':
        return self.Games
    elif item_type == 'Movies':
        return self.Movies
    else:
        print("Invalid operation. Please try again. ")


def input_items_took():
    while True:
        items_took = input('Anime:', 'Games:', 'Movies:')
        if items_took in item_type:
            return items_took
        else:
            print("Invalid operation. Please try again. ")


def input_category():
    while True:
        category = input('Anime, Games, or Movies:').strip().lower()
        if category == 'Anime':
            return self.anime
        elif category == 'Games':
            return self.games
        elif category == 'Movies':
            return self.movies
        else:
            print('Invalid operation. Please try again. ')


def input_item():
    while True:
        item = input('Which item will you take? ')
        if item in Anime:
            return anime.price
        elif item in Games:
            return games.price
        elif item in Movies:
            return movies.price
        else:
            print("Please provide an item that is in the inventory. ")


def show_choice():
    """ () -> dic

    Shows the user the dictionary of the items in their chosen category.
    """


def search_for_string(string, lines):
    ''' 
    This searches the text files and tries to find the item or 
    related items and returns them. 
    '''
    number = 0
    for line in lines:
        number += 1
        if string.lower() in line.lower():
            print('{}: {}'.format(number, line))


#def price_history(payment, rent_rate, item_name):
#    time = datetime.now()
#    text = '\n{}, {}, {},'.format(payment, rent_rate, item_name)
#    with open('history.txt', 'a') as file:
#        file.write(text)


def main():
    choice = get_category()
    string = input('Title:')
    if input_item == 'Games':
        return

    #lines = open_file(choice)
    #search_for_string(string, lines)


if __name__ == '__main__':
    main()
