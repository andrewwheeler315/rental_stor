from inventory import *


def item_in_category_quantity(item_type):
    ''' str -> dic

    Returns the quantity of the provided item.

    >>> item_quantity('Game')
    Game.keys()
    >>> item_quantity('Anime')
    Anime.keys()
    >>> item_quantity('Movie')
    Movie.keys()
    '''
    if item_type == 'Anime':
        return Anime.keys()
    elif item_type == 'Game':
        return Game.keys()
    elif item_type == 'Movie':
        return Movie.keys()
    else:
        print("Invalid operation. Please try again. ")


def input_category():
    while True:
        category = input('Anime, Game, or Movie? ').strip().lower()
        if category == 'Anime':
            return Anime.keys()
        elif category == 'Game':
            return Game.keys()
        elif category == 'Movie':
            return Movie.keys()
        else:
            print('Invalid operation. Please try again. ')


def item():
    while True:
        item = input('Which item will you take? ')
        if item in Anime:
            return Anime.keys()
        elif item in Game:
            return Game.keys()
        elif item in Movie:
            return Movie.keys()
        else:
            print("Please provide an item that is in the inventory. ")


def titles_in_category():
    """ str -> str

    Asks which title in the category the customers would like to rent.
    """
    Anime_Title = Anime.keys()
    Games_Title = Game.keys()
    Movie_Title = Movie.keys()


def main():

    # item_type = input('Would you like a Movie, Game, or Anime? ')
    # return (item_type)

    print("Welcome to BorderLands214's Entertainment Rental ")

    print('Which type of item are you looking for exactly? ')

    # item_in_category_quantity(item_type)
    input_category()
    input_item()
    titles_in_category()


if __name__ == '__main__':
    main()
