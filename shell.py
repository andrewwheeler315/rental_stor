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


def main():
    choice = category_choice()
    string = input('Title:')
    lines = open_file(choice)
    search_for_string(string, lines)


if __name__ == '__main__':
    main()
