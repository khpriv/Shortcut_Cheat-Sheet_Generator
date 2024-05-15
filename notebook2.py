import sys
import PIL.ImageOps
from PIL import Image, ImageDraw, ImageFont

filename = 'sheet'
# Leave as "" if You don't want to add title banner
banner_title = "Tytul"
# margin
margines = 20
# multiline text line spacing
line_spacing = 20
font_size_desc = 25
font_size_title = 70
# Controls how far apart "action" and "key" columns are
default_width_of_panel = 400
# font = "arial.ttf"  # font for windows machines
font = "DroidSans.ttf"  # font for Linux Machines

# uncomment one style
style = 'OLED'
# style = 'printer'
# style = 'ROSEPINE'
# style = 'GRUVBOX'
# style = 'LIGHT'
# style = 'DARK'

# Make sure that every "key" has its "action", \n is also ok.
description_action = ((f'action\n'
                       f'action1\n'
                       f'action2\n'
                       f'action3\n'
                       f'action4\n'
                       f'action5\n'
                       f'action6\n'
                       ),
                      (f'action\n'
                       f'action7\n'
                       f'action8\n'
                       f'action9\n'
                       f'action10\n'
                       f'action11\n'
                       f'action12\n'
                       f'action13\n'
                       f'action14\n'
                       f'action15\n'
                       ))
description_key = ((f'CTRL + K\n'
                    f'CTRL + W\n'
                    f'CTRL + W\n'
                    f'CTRL + W\n'
                    f'CTRL + W\n'
                    f'CTRL + W\n'
                    f'CTRL + W\n'
                    ),
                   (f'CTRL + K\n'
                    f'CTRL + L\n'
                    f'CTRL + L\n'
                    f'CTRL + L\n'
                    f'CTRL + L\n'
                    f'CTRL + L\n'
                    f'CTRL + L\n'
                    f'CTRL + L\n'
                    f'CTRL + L\n'
                    f'CTRL + L\n'
                    ))

try:
    font_title = ImageFont.truetype(font, font_size_title)
    font_desc = ImageFont.truetype(font, font_size_desc)
except OSError:
    sys.exit("Font can't be found or opened")
i = 0  # used as index for description lists
sizefinal_alt = (1024, 1024)

# default colors
bg_color = 'white'
border_color = 'white'
font_desc_color = 'black'
font_title_color = 'black'

banner_height = font_size_title * 2
default_line_height = font_size_desc + line_spacing


def set_style(styl):
    global bg_color
    global border_color
    global font_desc_color
    global font_title_color
    match styl:
        case 'OLED':
            bg_color = 'black'
            border_color = 'grey'
            font_desc_color = 'lightgray'
            font_title_color = 'lightgray'
        case 'printer':
            bg_color = 'white'
            border_color = 'lightgray'
            font_desc_color = 'black'
            font_title_color = 'black'
        case 'ROSEPINE':
            bg_color = 38, 35, 58
            border_color = 235, 111, 146
            font_desc_color = 224, 222, 244
            font_title_color = 224, 222, 244
        case 'GRUVBOX':
            bg_color = 40, 40, 40
            border_color = 152, 151, 26
            font_desc_color = 215, 153, 33
            font_title_color = 157, 0, 6
        case 'LIGHT':
            bg_color = 255, 255, 255
            border_color = 12, 28, 112
            font_desc_color = 0, 0, 0
            font_title_color = 0, 0, 0
        case 'DARK':
            bg_color = 21, 25, 29
            border_color = 49, 59, 75
            font_desc_color = 111, 111, 111
            font_title_color = 111, 111, 111
        case _:
            bg_color = 'white'
            border_color = 'white'
            font_desc_color = 'black'
            font_title_color = 'black'


def main():
    set_style(style)
    global i
    panels = list()
    for _ in range(len(description_action)):
        panel = create_panel()
        # panel.save(f'{filename}{i}.png')
        panels.append(panel)
        i = i + 1
    final_image = generate_merged_panel(panels)
    if banner_title:
        final_image = add_title_banner(final_image)
    final_image.save(f'{filename}_final.png')


def create_panel():
    size_no_border = get_size()
    keymap = Image.new('RGBA', size_no_border, bg_color)
    keymap = write_multiline(keymap)
    keymap = draw_border(keymap, margines)
    return keymap


def draw_border(image, spacing):
    image = PIL.ImageOps.expand(image, spacing * 2, bg_color)
    border = ImageDraw.Draw(image)
    border.rounded_rectangle([(spacing, spacing), (image.width - spacing, image.height - spacing)],
                             width=5,
                             fill=None,
                             outline=border_color,
                             radius=30)
    return image


def write_multiline(image):
    # global i
    tekst = ImageDraw.Draw(image)
    tekst.multiline_text((0, 0),
                         description_action[i],
                         align='left', font=font_desc,
                         spacing=line_spacing,
                         fill=font_desc_color)
    tekst.multiline_text((default_width_of_panel, 0),
                         description_key[i],
                         align='right',
                         font=font_desc,
                         anchor='ra',
                         spacing=line_spacing,
                         fill=font_desc_color)
    return image


def get_size(size=sizefinal_alt):
    return default_width_of_panel, description_action[i].count('\n') * default_line_height


def generate_merged_panel(panels_list):
    size_of_final_image = get_size_of_final_panels(panels_list)
    final_image = Image.new('RGBA', size_of_final_image, bg_color)
    x_cord = 0
    for panel in panels_list:
        w, h = panel.size
        final_image.paste(panel, (x_cord, 0))
        x_cord = x_cord + w
    return final_image


def get_size_of_final_panels(panels_list):
    width = 0
    height = 0
    for panel in panels_list:
        width = panel.width + width
        if height < panel.height:
            height = panel.height
    return width, height


def add_title_banner(image):
    banner = Image.new('RGBA', (image.width, banner_height), bg_color)
    title = ImageDraw.Draw(banner)
    title.multiline_text((image.width/2, (banner_height+font_size_title)/2),
                         banner_title,
                         align='left', font=font_title,
                         spacing=line_spacing,
                         fill=font_title_color, anchor='ms')
    image_with_banner = Image.new('RGBA', (image.width, banner.height + image.height), bg_color)
    image_with_banner.paste(banner, (0, 0))
    image_with_banner.paste(image, (0, banner.height))
    return image_with_banner


if __name__ in '__main__':
    main()
