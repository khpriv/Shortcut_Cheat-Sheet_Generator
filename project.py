import sys
import PIL.ImageOps
from PIL import Image, ImageDraw, ImageFont
from config_file import ConfigurationClass


i = 0  # used as index for description lists
sizefinal_alt = (1024, 1024)
global C
C = ConfigurationClass()


def main():
    # c = ConfigurationClass()
    C.set_style(C.style)
    global i
    panels = list()
    for _ in range(len(C.description_action)):
        panel = create_panel()
        panels.append(panel)
        i = i + 1
    final_image = generate_merged_panel(panels)
    if C.banner_title:
        final_image = add_title_banner(final_image)
    final_image.save(f'{C.filename}_final.png')


def create_panel():
    size_no_border = get_size()
    keymap = Image.new('RGBA', size_no_border, C.bg_color)
    keymap = write_multiline(keymap)
    keymap = draw_border(keymap, C.margines)
    return keymap


def draw_border(image, spacing):
    image = PIL.ImageOps.expand(image, spacing * 2, C.bg_color)
    border = ImageDraw.Draw(image)
    border.rounded_rectangle([(spacing, spacing), (image.width - spacing, image.height - spacing)],
                             width=5,
                             fill=None,
                             outline=C.border_color,
                             radius=30)
    return image


def write_multiline(image):
    # global i
    tekst = ImageDraw.Draw(image)
    tekst.multiline_text((0, 0),
                         C.description_action[i],
                         align='left', font=C.font_desc,
                         spacing=C.line_spacing,
                         fill=C.font_desc_color)
    tekst.multiline_text((C.default_width_of_panel, 0),
                         C.description_key[i],
                         align='right',
                         font=C.font_desc,
                         anchor='ra',
                         spacing=C.line_spacing,
                         fill=C.font_desc_color)
    return image


def get_size(size=sizefinal_alt):
    return C.default_width_of_panel, C.description_action[i].count('\n') * C.default_line_height - C.line_spacing


def generate_merged_panel(panels_list):
    size_of_final_image = get_size_of_final_panels(panels_list)
    final_image = Image.new('RGBA', size_of_final_image, C.bg_color)
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
    banner = Image.new('RGBA', (image.width, C.banner_height), C.bg_color)
    title = ImageDraw.Draw(banner)
    title.multiline_text((image.width / 2, (C.banner_height + C.font_size_title) / 2),
                         C.banner_title,
                         align='left', font=C.font_title,
                         spacing=C.line_spacing,
                         fill=C.font_title_color, anchor='ms')
    image_with_banner = Image.new('RGBA', (image.width, banner.height + image.height), C.bg_color)
    image_with_banner.paste(banner, (0, 0))
    image_with_banner.paste(image, (0, banner.height))
    return image_with_banner


if __name__ in '__main__':
    main()
