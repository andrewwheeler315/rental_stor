class Movies:
    """A movie that you can rent. """

    def __init__(self, title, price):
        """ (Movies, str, float) -> NoneType

        Create a new movie named title and is worth price.
        """

        self.title = title
        self.price = price

    def __str__(self):
        """ (Movies) -> str

        Return a string representation of Movies. 
        
        >>> movies = Movies('Transformers', '$1.00')
        >>> movies.__str__()
        'Transformers\n$1.00'
        """

        return '{}\n{}'.format(self.title, self.price)


def load_movies():

    Movies = {
        'Transformers': {'Price: $1.00'},
        'Deadpool': {'Price: $1.25'},
        'X-Men Origins Wolverine': {'Price: $1.50'},
        'Die Hard': {'Price: $1.75'},
        '2012': {'Price: $2.00'},
        'The Day After Tomorrow': {'Price: $2.25'},
        'Armageddon': {'Price: $2.50'},
        'Thor': {'Price: $2.75'},
        'The Lord of the Rings': {'Price: $3.00'},
        'The Hobbit': {'Price: $3.25'},
        'Harry Potter': {'Price: $3.50'},
        'Chucky': {'Price: $3.75'},
        'A Quiet Place': {'Price: $4.00'},
        'Escape Plan': {'Price: $2.25'},
        'Rampage': {'Price: $1.50'}
    }
