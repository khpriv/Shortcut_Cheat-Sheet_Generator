import PIL.ImageOps
from PIL import Image, ImageDraw, ImageFont

sizefinal_alt = (1024, 1024)
filename = 'pliczek'
margines = 20
font_size = 25
line_spacing = 20
default_line_height = font_size + line_spacing
default_width_of_panel = 400
font_desc = ImageFont.truetype("arial.ttf", font_size)
i = 0

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
                    ))


def draw_border(image, spacing):
    image = PIL.ImageOps.expand(image, spacing * 2, 'black')
    border = ImageDraw.Draw(image)
    border.rounded_rectangle([(spacing, spacing), (image.width - spacing, image.height - spacing)],
                             width=5,
                             fill=None,
                             outline='grey',
                             radius=30)
    return image


def get_size(size=sizefinal_alt):
    return default_width_of_panel, description_action[i].count('\n') * default_line_height


def write_multiline(image):
    # global i
    tekst = ImageDraw.Draw(image)
    tekst.multiline_text((0, 0),
                         description_action[i],
                         align='left', font=font_desc,
                         spacing=line_spacing,
                         fill='lightgrey')
    tekst.multiline_text((default_width_of_panel, 0),
                         description_key[i],
                         align='right',
                         font=font_desc,
                         anchor='ra',
                         spacing=line_spacing)
    return image


def create_panel():
    size_no_border = get_size()
    keymap = Image.new('RGBA', size_no_border, 'black')
    keymap = write_multiline(keymap)
    keymap = draw_border(keymap, margines)
    return keymap


def generate_merged_panel(panels_list):
    for panel in panels_list:

    return final_image


def main():
    global i
    panels = list()
    for _ in range(len(description_action)):
        panel = create_panel()
        panel.save(f'{filename}{i}.png')
        panels.append(panel)
        i = i + 1
    final_image = generate_merged_panel(panels)
    final_image.save(f'{filename}_final.png')


if __name__ in '__main__':
    main()
