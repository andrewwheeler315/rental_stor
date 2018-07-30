class Anime:
    """An anime you can rent. """

    def __init__(self, title, price):
        """ (Anime, str, float) -> NoneType

        Create a new anime named title and is worth price.
        """

        self.title = title
        self.price = price

    def __str__(self):
        """ (Anime) -> str

        Return a string representation of Anime. 
        
        >>> anime = Anime('Fairy Tail', '$0.25')
        >>> anime.__str__()
        'Fairy Tail\n$0.25'
        """

        return '{}\n{}'.format(self.title, self.price)



def load_anime():

     Anime = {
        'Fairy Tail': {'Price: $0.25'},
        'Seven Deadly Sins': {'Price: $0.50'},
        'Bleach': {'Price: $0.75'},
        'One Piece': {'Price: $1.00'},
        'Full Metal Alchemist': {'Price: $1.25'},
        'Naruto': {'Price: $1.50'},
        'Inuyasha' {'Price: $1.75'},
        'Black Clover': {'Price: $1.50'},
        'One Punch Man': {'Price: $1.25'},
        'Cowboy Bebop': {'Price: $1.00'},
        'Hellsing': {'Price: $0.75'},
        'Dragon Ball Z': {'Price: $0.50'},
        'Beyblade': {'Price: $0.25'},
        'Yu-Gi-Oh!': {'Price: $1.00'},
        'My Hero Academia': {'Price: $1.50'}
    }
