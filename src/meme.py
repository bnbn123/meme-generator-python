"""Docstring for main's module."""
import os
import random
import argparse
from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor, QuoteModel

root_dir = os.path.dirname(__file__)


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        abs_image_paths = os.path.join(images.replace(".", root_dir, 1))
        for root, dirs, files in os.walk(abs_image_paths):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = list(
            map(
                lambda path: os.path.join(path.replace(".", root_dir, 1)),
                [
                    "./_data/DogQuotes/DogQuotesTXT.txt",
                    "./_data/DogQuotes/DogQuotesDOCX.docx",
                    "./_data/DogQuotes/DogQuotesPDF.pdf",
                    "./_data/DogQuotes/DogQuotesCSV.csv",
                ],
            )
        )
        print("quote_files", quote_files)
        quotes = []
        if quote_files is not None:
            for f in quote_files:
                print("f", f)
                quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./tmp".replace(".", root_dir, 1))
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Say a Greeting.")
    parser.add_argument(
        "--path", type=str, action="append", help="quote body to add to the image"
    )
    parser.add_argument("--body", type=str,
                        help="quote author to add to the image")
    parser.add_argument("--author", type=str, help="author of image")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
