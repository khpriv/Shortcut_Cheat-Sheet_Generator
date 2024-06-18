import dearpygui.dearpygui as dpg
# import dearpygui.demo as demo

from config_file import ConfigurationClass
global C
C = ConfigurationClass()


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


def start_gui():
    dpg.create_context()

    with dpg.window(tag='main_window'):
        dpg.add_text("Configuration for cheatsheet generator")
        dpg.add_input_text(label="Filename: ", tag="filename", default_value=C.filename)
        dpg.add_input_text(label="Banner title: ", tag="banner_title", default_value=C.banner_title)
        dpg.add_input_int(label="Margines: ", tag="margines", default_value=C.margines)
        dpg.add_input_int(label="Line spacing: ", tag="line_spacing", default_value=C.line_spacing)
        dpg.add_input_int(label="Font size for description: ", tag="font_size_desc", default_value=C.font_size_desc)
        dpg.add_input_int(label="Font size for title ", tag="font_size_title", default_value=C.font_size_title)
        dpg.add_input_int(label="Default width of panel: ", tag="default_width_of_panel", default_value=C.default_width_of_panel)
        ## add font select?, default_value=C.
        dpg.add_combo(label="Select style: ", items=C.style_list, tag="style", default_value=C.style)
        dpg.add_input_int(label="Banner heigh: ", tag="banner_height", default_value=C.banner_height)
        dpg.add_input_int(label="Default line height: ", tag="default_line_height", default_value=C.default_line_height)

        dpg.add_button(label="Change data", callback=update)
        dpg.add_button(label="Execute", callback=do_everything)
        dpg.add_button(label="Exit", callback=stop_gui)
    dpg.create_viewport(title=C.banner_title , width=800, height=600)
    # demo.show_demo()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("main_window", True)
    dpg.start_dearpygui()



def stop_gui():
    dpg.destroy_context()


def main():
    start_gui()
    stop_gui()


if __name__ in '__main__':
    main()
