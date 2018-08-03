class Games:
    """A game that you can rent. """

    def __init__(self, title, price):
        """ (Games, str, float) -> NoneType
        
        Create a new game named title and is worth price.
        """

        self.title = title
        self.price = price

    def __str__(self):
        """ (Games) -> str

        Return a string representation of Games. 
        
        >>> games = Games('Final Fantasy XV', '$1.25')
        >>> games__str__()
        'Final Fantasy XV\n$1.25'
        """

        return '{}\n{}'.format(self.title, self.price)


def load_games():

    Games = {
        'Final Fantasy XV': {'Price: $1.25'},
        'Final Fantasy XIII': {'Price: $1.00'},
        'Final Fantasy X': {'Price: $0.75'},
        'Final Fantasy X-2': {'Price: $0.75'},
        'Final Fantasy VII': {'Price: $0.50'},
        "Uncharted 3: Drake's Deception": {'Price: $2.00'},
        "Uncharted 4: A Thief's End": {'Price: $2.75'},
        'Gears of War 3': {'Price: $2.25'},
        'Gears of War Judgement': {'Price: $2.00'},
        'God of War 3': {'Price: $2.50'},
        'God of War 4': {'Price: $3.00'},
        'Doom 4': {'Price: $1.25'},
        'GTA V': {'Price: $3.25'},
        'Saints Row IV': {'Price: $3.50'},
        'Saints Row III': {'Price: $1.00'}
    }
