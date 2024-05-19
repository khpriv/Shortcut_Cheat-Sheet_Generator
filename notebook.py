import sys
import PIL.ImageOps
from PIL import Image, ImageDraw, ImageFont

import dearpygui.dearpygui as dpg


def change_text(sender, app_data):
    dpg.set_value("text item", f"Mouse Button ID: {app_data}")


def start_gui():
    dpg.create_context()
    with dpg.window(width= 500, height= 500):
        dpg.add_text("Click this shit", tag="text item")
        with dpg.item_handler_registry(tag="widget handler") as handler:
            dpg.add_item_clicked_handler(callback=change_text)
        dpg.bind_item_handler_registry("text item", "widget handler")

    dpg.create_viewport(title='Custom Title', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def main():
    start_gui()


if __name__ in '__main__':
    main()
