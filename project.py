import sys
import PIL.ImageOps
from PIL import Image, ImageDraw, ImageFont
from config_file import ConfigurationClass


i = 0  # used as index for description lists
sizefinal_alt = (1024, 1024)
c = ConfigurationClass()

def main():
    # c = ConfigurationClass()
    c.set_style(c.style)
    global i
    panels = list()
    for _ in range(len(c.description_action)):
        panel = create_panel()
        panels.append(panel)
        i = i + 1
    final_image = generate_merged_panel(panels)
    if c.banner_title:
        final_image = add_title_banner(final_image)
    final_image.save(f'{c.filename}_final.png')


def create_panel():
    size_no_border = get_size()
    keymap = Image.new('RGBA', size_no_border, c.bg_color)
    keymap = write_multiline(keymap)
    keymap = draw_border(keymap, c.margines)
    return keymap


def draw_border(image, spacing):
    image = PIL.ImageOps.expand(image, spacing * 2, c.bg_color)
    border = ImageDraw.Draw(image)
    border.rounded_rectangle([(spacing, spacing), (image.width - spacing, image.height - spacing)],
                             width=5,
                             fill=None,
                             outline=c.border_color,
                             radius=30)
    return image


def write_multiline(image):
    # global i
    tekst = ImageDraw.Draw(image)
    tekst.multiline_text((0, 0),
                         c.description_action[i],
                         align='left', font=c.font_desc,
                         spacing=c.line_spacing,
                         fill=c.font_desc_color)
    tekst.multiline_text((c.default_width_of_panel, 0),
                         c.description_key[i],
                         align='right',
                         font=c.font_desc,
                         anchor='ra',
                         spacing=c.line_spacing,
                         fill=c.font_desc_color)
    return image


def get_size(size=sizefinal_alt):
    return c.default_width_of_panel, c.description_action[i].count('\n') * c.default_line_height - c.line_spacing


def generate_merged_panel(panels_list):
    size_of_final_image = get_size_of_final_panels(panels_list)
    final_image = Image.new('RGBA', size_of_final_image, c.bg_color)
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
    banner = Image.new('RGBA', (image.width, c.banner_height), c.bg_color)
    title = ImageDraw.Draw(banner)
    title.multiline_text((image.width / 2, (c.banner_height + c.font_size_title) / 2),
                         c.banner_title,
                         align='left', font=c.font_title,
                         spacing=c.line_spacing,
                         fill=c.font_title_color, anchor='ms')
    image_with_banner = Image.new('RGBA', (image.width, banner.height + image.height), c.bg_color)
    image_with_banner.paste(banner, (0, 0))
    image_with_banner.paste(image, (0, banner.height))
    return image_with_banner


if __name__ in '__main__':
    main()
