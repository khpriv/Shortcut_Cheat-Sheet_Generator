import PIL.ImageOps
from PIL import Image, ImageDraw

import dearpygui.dearpygui as dpg

from config_file import ConfigurationClass
C = ConfigurationClass()

i = 0  # used as index for description lists
sizefinal_alt = (1024, 1024)


def main():
    start_gui()
    stop_gui()


def delete_popup_and_exit():
    dpg.delete_item("done_popup")
    dpg.delete_item("description_action")
    dpg.delete_item("description_key")
    dpg.delete_item("main_window")
    stop_gui()


def do_everything():
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

    with dpg.window(tag="done_popup", width= 200, height=80, no_title_bar=True, no_resize=True, pos=[300, 350],
                    no_move=True, no_collapse=True):
        dpg.add_text("File created", pos=[60, 35])
        dpg.add_button(label="Close", pos=[60, 60], callback=delete_popup_and_exit, width=80)


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
    global i
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


def get_size():
    global i
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


def update_style(styl):
    print(C.bg_color)
    C.style = styl
    C.set_style(C.style)
    print(C.bg_color)


def update(sender, app_data, user_data):
    C.filename = dpg.get_value("filename")
    C.banner_title = dpg.get_value("banner_title")
    C.margines = dpg.get_value("margines")
    C.line_spacing = dpg.get_value("line_spacing")
    C.font_size_desc = dpg.get_value("font_size_desc")
    C.font_size_title = dpg.get_value("font_size_title")
    C.default_width_of_panel = dpg.get_value("default_width_of_panel")
    C.style = dpg.get_value("style")
    C.banner_height = dpg.get_value("banner_height")
    C.default_line_height = dpg.get_value("default_line_height")
    C.set_style(C.style)
    local_description_action = list()
    local_0 = dpg.get_value("description_action(0)")
    local_1 = dpg.get_value("description_action(1)")
    local_2 = dpg.get_value("description_action(2)")
    if len(local_0) > 1:
        local_description_action.append(local_0 + '\n')
    if len(local_1) > 1:
        local_description_action.append(local_1 + '\n')
    if len(local_2) > 1:
        local_description_action.append(local_2 + '\n')
    C.description_action = local_description_action
    local_description_key = list()
    local_0 = dpg.get_value("description_key(0)")
    local_1 = dpg.get_value("description_key(1)")
    local_2 = dpg.get_value("description_key(2)")
    if len(local_0) > 1:
        local_description_key.append(local_0 + '\n')
    if len(local_1) > 1:
        local_description_key.append(local_1 + '\n')
    if len(local_2) > 1:
        local_description_key.append(local_2 + '\n')
    C.description_key = local_description_key


def start_gui():
    dpg.create_context()
    first_col = 10
    second_col = 250
    # dpg.create_viewport(title=C.banner_title, width=817, height=920)
    dpg.create_viewport(title='Configuration for cheatsheet generator', width=801, height=885)
    viewport_width = dpg.get_viewport_width()

    with dpg.window(tag='main_window', width=viewport_width, height=365, no_title_bar=True, no_resize=True, pos=[0, 0],
                    no_move=True, no_collapse=True):
        dpg.add_text("Configuration for cheatsheet generator")
        dpg.add_text("Filename: ", pos=[first_col, 40])
        dpg.add_input_text(tag="filename", default_value=C.filename, pos=[second_col, 40], width=500)
        dpg.add_text("Banner title: ", pos=[first_col, 65])
        dpg.add_input_text(tag="banner_title", default_value=C.banner_title, pos=[second_col, 65], width=500)
        dpg.add_text("Margines: ", pos=[first_col, 90])
        dpg.add_input_int(tag="margines", default_value=C.margines, pos=[second_col, 90], width=500)
        dpg.add_text("Line spacing: ", pos=[first_col, 115])
        dpg.add_input_int(tag="line_spacing", default_value=C.line_spacing, pos=[second_col, 115], width=500)
        dpg.add_text("Font size for description: ", pos=[first_col, 140])
        dpg.add_input_int(tag="font_size_desc", default_value=C.font_size_desc, pos=[second_col, 140], width=500)
        dpg.add_text("Font size for title: ", pos=[first_col, 165])
        dpg.add_input_int(tag="font_size_title", default_value=C.font_size_title, pos=[second_col, 165], width=500)
        dpg.add_text("Default width of panel: ", pos=[first_col, 190])
        dpg.add_input_int(tag="default_width_of_panel", default_value=C.default_width_of_panel, pos=[second_col, 190],
                          width=500)
        dpg.add_text("Select style: ", pos=[first_col, 215])
        dpg.add_combo(items=C.style_list, tag="style", default_value=C.style, pos=[second_col, 215], width=500)
        dpg.add_text("Banner height: ", pos=[first_col, 240])
        dpg.add_input_int(tag="banner_height", default_value=C.banner_height, pos=[second_col, 240], width=500)
        dpg.add_text("Default line height: ", pos=[first_col, 265])
        dpg.add_input_int(tag="default_line_height", default_value=C.default_line_height, pos=[second_col, 265],
                          width=500)
        dpg.add_button(label="Change data", callback=update, width=100, pos=[second_col + 200, 300])
        dpg.add_button(label="Execute", callback=do_everything, width=100, pos=[second_col + 200, 325])

    with dpg.window(tag='description_action', width=viewport_width/2, height=520, no_title_bar=True, no_resize=True,
                    pos=[0, 365], no_move=True, no_collapse=True):
        dpg.add_text("Description: ", pos=[first_col, 0])
        dpg.add_input_text(tag="description_action(0)", default_value=C.description_action[0], multiline=True,
                           height=150, width=380, pos=[first_col, 25])
        dpg.add_input_text(tag="description_action(1)", default_value=C.description_action[1], multiline=True,
                           height=150, width=380, pos=[first_col, 190])
        dpg.add_input_text(tag="description_action(2)", default_value=C.description_action[2], multiline=True,
                           height=150, width=380, pos=[first_col, 355])
    with dpg.window(tag='description_key', width=viewport_width/2, height=520, no_title_bar=True, no_resize=True,
                    pos=[viewport_width/2+1, 365], no_move=True, no_collapse=True):
        dpg.add_text("Key: ", pos=[first_col, 0])
        dpg.add_input_text(tag="description_key(0)", default_value=C.description_key[0], multiline=True, height=150,
                           width=viewport_width/2-2*first_col, pos=[first_col, 25])
        dpg.add_input_text(tag="description_key(1)", default_value=C.description_key[1], multiline=True, height=150,
                           width=viewport_width/2-2*first_col, pos=[first_col, 190])
        dpg.add_input_text(tag="description_key(2)", default_value=C.description_key[2], multiline=True, height=150,
                           width=viewport_width/2-2*first_col, pos=[first_col, 355])

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()


def stop_gui():
    dpg.destroy_context()


if __name__ in '__main__':
    main()
