import PIL.ImageOps
from PIL import Image, ImageDraw, ImageFont

sizefinal = (1024, 1024)
filename = 'pliczek'
margines = 20
font_desc = ImageFont.truetype("arial.ttf", 25)


def draw_border(image, spacing):
    image = PIL.ImageOps.expand(image, spacing * 2, 'black')
    border = ImageDraw.Draw(image)
    border.rounded_rectangle([(spacing, spacing), (image.width - spacing, image.height - spacing)], width=5, fill=None, outline='lightgrey', radius=30)

    return image


def create_panel(size=(128, 128)):
    new_panel = Image.new('RGBA', size, 'black')
    return new_panel


def write_multiline(image):
    tekst = ImageDraw.Draw(image)
    tekst.text((10, 25), "world", font=font_desc)
    return image


def main():
    keymap = Image.new('RGBA', sizefinal, 'black')
    panel = create_panel(sizefinal)
    keymap = write_multiline(keymap)
    keymap = draw_border(keymap, margines)

    keymap.save(f'{filename}.png')


if __name__ in '__main__':
    main()
