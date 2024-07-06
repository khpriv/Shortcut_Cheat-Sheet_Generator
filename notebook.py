import sys
import PIL.ImageOps
from PIL import Image, ImageDraw, ImageFont
# from GUI_component import C
# from GUI_component import start_gui
from config_file import ConfigurationClass
import dearpygui.dearpygui as dpg

i = 0  # used as index for description lists
sizefinal_alt = (1024, 1024)
# global C
C = ConfigurationClass()


def main():
    # c = ConfigurationClass()
    start_gui()
    stop_gui()
    # do_everything()


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


def get_size(size=sizefinal_alt):
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
    # C.font = dpg.get_value()
    C.style = dpg.get_value("style")
    # C.description_action = dpg.get_value()
    # C.description_key = dpg.get_value()
    # C.bg_color = dpg.get_value()
    # C.border_color = dpg.get_value()
    # C.font_desc_color = dpg.get_value()
    # C.font_title_color = dpg.get_value()
    C.banner_height = dpg.get_value("banner_height")
    C.default_line_height = dpg.get_value("default_line_height")
    C.set_style(C.style)
    local_description_action = list()
    local_0 = dpg.get_value("description_action(0)")
    local_1 = dpg.get_value("description_action(1)")
    local_2 = dpg.get_value("description_action(2)")
    if len(local_0) > 1:
        local_description_action.append(local_0)
    if len(local_1) > 1:
        local_description_action.append(local_1)
    if len(local_2) > 1:
        local_description_action.append(local_2)
    C.description_action = local_description_action
    local_description_key = list()
    local_0 = dpg.get_value("description_key(0)")
    local_1 = dpg.get_value("description_key(1)")
    local_2 = dpg.get_value("description_key(2)")
    if len(local_0) > 1:
        local_description_key.append(local_0)
    if len(local_1) > 1:
        local_description_key.append(local_1)
    if len(local_2) > 1:
        local_description_key.append(local_2)
    C.description_key = local_description_key


def start_gui():
    dpg.create_context()
    first_col = 10
    second_col = 250

    with dpg.window(tag='main_window', width=800, height=380, no_title_bar=True, no_resize=True, pos=[0, 0],
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
        ## add font select?, default_value=C.
        dpg.add_combo(items=C.style_list, tag="style", default_value=C.style, pos=[second_col, 215], width=500)
        dpg.add_text("Banner height: ", pos=[first_col, 240])
        dpg.add_input_int(tag="banner_height", default_value=C.banner_height, pos=[second_col, 240], width=500)
        dpg.add_text("Default line height: ", pos=[first_col, 265])
        dpg.add_input_int(tag="default_line_height", default_value=C.default_line_height, pos=[second_col, 265],
                          width=500)
        dpg.add_button(label="Change data", callback=update, width=100, pos=[second_col + 200, 300])
        dpg.add_button(label="Execute", callback=do_everything, width=100, pos=[second_col + 200, 325])
        dpg.add_button(label="Exit", callback=stop_gui, width=100, pos=[second_col + 200, 350])

    with dpg.window(tag='description_action', width=400, height=520, no_title_bar=True, no_resize=True, pos=[0, 380],
                    no_move=True, no_collapse=True):
        dpg.add_text("Description: ", pos=[first_col, 0])
        # for x in range(len(C.description_action)):
        #     dpg.add_input_text(tag=f"description_action({x})", default_value=C.description_action[x], multiline=True, height=140)
        dpg.add_input_text(tag="description_action(0)", default_value=C.description_action[0], multiline=True,
                           height=150, width=380, pos=[first_col, 25])
        dpg.add_input_text(tag="description_action(1)", default_value=C.description_action[1], multiline=True,
                           height=150, width=380, pos=[first_col, 190])
        dpg.add_input_text(tag="description_action(2)", default_value=C.description_action[2], multiline=True,
                           height=150, width=380, pos=[first_col, 355])
    with dpg.window(tag='description_key', width=400, height=520, no_title_bar=True, no_resize=True, pos=[401, 380],
                    no_move=True, no_collapse=True):
        dpg.add_text("Key: ", pos=[first_col, 0])
        # for x in range(len(C.description_key)):
        #     dpg.add_input_text(tag=f"description_key({x})", default_value=C.description_key[x], multiline=True, height=140)
        dpg.add_input_text(tag="description_key(0)", default_value=C.description_key[0], multiline=True, height=150,
                           width=380, pos=[first_col, 25])
        dpg.add_input_text(tag="description_key(1)", default_value=C.description_key[1], multiline=True, height=150,
                           width=380, pos=[first_col, 190])
        dpg.add_input_text(tag="description_key(2)", default_value=C.description_key[2], multiline=True, height=150,
                           width=380, pos=[first_col, 355])

    dpg.create_viewport(title=C.banner_title, width=800, height=900)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # dpg.set_primary_window("main_window", True)
    dpg.start_dearpygui()


def stop_gui(sender, app_data, user_data):
    dpg.destroy_context()


if __name__ in '__main__':
    main()
