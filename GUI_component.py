from project import C

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

from config_file import ConfigurationClass

app_data = ConfigurationClass()
app_data = C


def change_text(sender, app_data):
    dpg.set_value("text item", f"Mouse Button ID: {app_data}")


def update_style(styl):
    print(C.bg_color)
    C.style = styl
    C.set_style(C.style)
    print(C.bg_color)


def update():
    C = app_data
    print("Data updated")
    print(C.style)
    print(app_data.font_size_desc)
    print(C.font_size_desc)


def start_gui():
    dpg.create_context()

    with dpg.window(tag='main_window'):
        dpg.add_text("Configuration for cheatsheet generator")
        dpg.add_text(f'Current style is {C.style}', user_data=C.style)
        dpg.add_input_int(label='integer', user_data=app_data.font_size_desc, default_value=app_data.font_size_desc, callback=update())
        dpg.add_combo(label='combo', items=app_data.style_list, user_data=app_data.style, default_value=app_data.style, callback=update())
    app_data.font_size_desc = dpg.get_value(item='integer')
    app_data.style = dpg.get_value(item='combo')
    print(dpg.get_value(item='integer'))


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





    update()
    stop_gui()


if __name__ in '__main__':
    main()
