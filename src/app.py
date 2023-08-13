"""Docstring for app's module."""
import random
from flask import Flask, render_template, abort, request
from QuoteEngine.Ingestor import Ingestor
import os
from glob import glob

from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor
import requests
import uuid

STATIC_FOLDER = "./static"
EXTENSION_DEFAULT = ".jpg"

app = Flask(__name__)
root_dir = os.path.dirname(__file__)

meme = MemeEngine(STATIC_FOLDER.replace(".", root_dir, 1))


def setup():
    """Docstring for setup function."""
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

    for path in quote_files:
        Ingestor.parse(path)
    quotes = Ingestor.ingestors

    images_path = "./_data/photos/dog/"
    images_path = os.path.join(images_path.replace(".", root_dir, 1))
    imgs = glob(os.path.join(images_path, "*.jpg"))

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    try:
        image_url = request.form["image_url"]
        body = '"{}"'.format(request.form["body"])
        author = request.form["author"]
        response = requests.get(image_url)
        local_image_url = "{}/{}{}".format(
            STATIC_FOLDER.replace(".", root_dir, 1),
            str(uuid.uuid4()),
            EXTENSION_DEFAULT,
        )
        with open(local_image_url, "wb") as handler:
            handler.write(response.content)
        path = meme.make_meme(local_image_url, body, author)
    except requests.exceptions.ConnectionError:
        print("<Enter user friendly error message>")
        return render_template("meme_error.html")
    else:
        os.remove(local_image_url)
        return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
