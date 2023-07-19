from PIL import Image, ImageDraw, ImageFont
from random import randint

FONT_PATH = "src/fonts/Open_Sans/OpenSans-VariableFont_wdth,wght.ttf"
FONT_SIZE = 35


class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir + ".jpg"

    def load_images(self, paths):
        images = []
        try:
            for path in paths:
                img = Image.open(path)
                images.append(img)
        except Exception as e:
            print("Cannot load images", e)
            return None
        return images

    def make_meme(self, img, text, author, width=500) -> str:
        width = 500 if width > 500 else width
        if width is not None:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        I1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        I1.text(
            (randint(0, 500), randint(0, 500)),
            "{} {}".format(text, author),
            font=myFont,
            fill=(255, 0, 0),
        )
        img.save(self.output_dir)
        return self.output_dir
