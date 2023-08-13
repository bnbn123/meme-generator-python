class QuoteModel:
    """Docstring for QuoteModel's class."""

    def __init__(self, body, author):
        """Docstring for __init__ function."""
        self.body = body
        self.author = author

    def __str__(self):
        """Docstring for __str__ function."""
        return "{} - {}".format(self.body, self.author)
