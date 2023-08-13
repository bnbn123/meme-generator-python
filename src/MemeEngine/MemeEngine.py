from PIL import Image, ImageDraw, ImageFont
from random import randint
import os
import uuid

FONT_PATH = "fonts/Open_Sans/OpenSans-VariableFont_wdth,wght.ttf"
FONT_SIZE = 25
EXTENSION_OUTPUT = ".jpg"


class MemeEngine:
    def __init__(self, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Load the image from disk, resize it, and add text to it"""
        img = Image.open(img_path)
        width = 500 if width > 500 else width
        if width is not None:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        I1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        coor_x = randint(0, int(img.width/4))
        coor_y = randint(0, int(img.height/4))
        I1.text(
            (coor_x, coor_y),
            "{} - {}".format(text, author),
            font=myFont,
            fill=(255, 0, 0),
        )

        temp_url = "{}{}".format(str(uuid.uuid4()), EXTENSION_OUTPUT)
        savedUrl = "{}/{}".format(self.output_dir, temp_url)
        img.save(savedUrl)
        return savedUrl
