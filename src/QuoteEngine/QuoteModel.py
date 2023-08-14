class QuoteModel:
    """Docstring for QuoteModel's class."""

    def __init__(self, body, author):
        """init with body and author."""
        self.body = body
        self.author = author

    def __str__(self):
        """Return both as formatted string"""
        return "{} - {}".format(self.body, self.author)
