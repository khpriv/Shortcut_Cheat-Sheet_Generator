import pytest
import PIL.ImageOps
from PIL import Image, ImageDraw
from config_file import ConfigurationClass
from project import create_panel, update_style


def test_Configuration_Class_init():
    test_instance = ConfigurationClass()
    assert isinstance(test_instance, ConfigurationClass)
    assert test_instance.filename == "PyCharm"
    assert test_instance.banner_title == "PyCharm keybinds"
    assert test_instance.margines == 20
    assert test_instance.line_spacing == 20
    assert test_instance.font_size_desc == 25
    assert test_instance.font_size_title == 70
    assert test_instance.default_width_of_panel == 420
    assert test_instance.font == "DroidSans.ttf"  # font for Linux Machines
    assert test_instance.style_list == ['OLED', 'printer', 'ROSEPINE', 'GRUVBOX', 'LIGHT', 'DARK', 'CUSTOM']
    assert test_instance.style == 'LIGHT'
    assert test_instance.description_action == ((f'Run/Debug\n'
                                f'Search anywhere\n'
                                f'Context actions\n'
                                f'Comment line\n'
                                f'Extent selection\n'
                                f'New file\n'
                                f'Settings\n'
                                ), (
                                   f'Collapse current node\n'
                                   f'Collapse all\n'
                                   f'Go to declarations\n'
                                   f'Reformat code\n'
                                   f'Toggle case\n'
                                   f'Duplicate line\n'
                                   f'Cut line\n'
                                   f'Start new line\n'
                               ), (
                                   f'Go to start/end of block\n'
                                   f'\n'
                                   f'\n'
                                   f'\n'
                                   f'\n'
                                   f'\n'
                                   f'\n'
                               ))
    assert test_instance.description_key == ((f'Shift + F10/F9\n'
                             f'Double Shift\n'
                             f'Ctrl + Shift + A\n'
                             f'Ctrl + /\n'
                             f'Ctrl + W\n'
                             f'Alt + Insert\n'
                             f'Ctrl + Alt + S\n'
                             ), (
                                f'Ctrl + - (Num)\n'
                                f'Ctrl + Shift + -(Num)\n'
                                f'Ctrl + B\n'
                                f'Ctrl + Alt + L\n'
                                f'Ctrl + Shift + U\n'
                                f'Ctrl + D\n'
                                f'Ctrl + X\n'
                                f'Shift + Enter\n'
                            ), (
                                f'Ctrl + ] / [\n'
                                f'\n'
                                f'\n'
                                f'\n'
                                f'\n'
                                f'\n'
                                f'\n'
                            ))
    assert test_instance.bg_color == 'white'
    assert test_instance.border_color == 'white'
    assert test_instance.font_desc_color == 'black'
    assert test_instance.font_title_color == 'black'
    assert test_instance.banner_height == test_instance.font_size_title * 2
    assert test_instance.default_line_height == test_instance.font_size_desc + test_instance.line_spacing


def test_create_panel():
    test_image_size = [ 100, 200]
    test_image = Image.new('RGBA', test_image_size, 'black')
    C = ConfigurationClass()

    assert isinstance(create_panel(), PIL.Image.Image)


def test_set_style():
    test_instance = ConfigurationClass()
    current_style = test_instance.style
    assert current_style == 'LIGHT'

    assert test_instance.bg_color == 'white'
    test_instance.style = 'OLED'
    test_instance.set_style(test_instance.style)
    assert test_instance.bg_color == 'black'
    assert test_instance.border_color == 'grey'
    assert test_instance.font_desc_color == 'lightgray'
    assert test_instance.font_title_color == 'lightgray'

    test_instance.style = 'printer'
    test_instance.set_style(test_instance.style)
    assert test_instance.bg_color == 'white'
    assert test_instance.border_color == 'lightgray'
    assert test_instance.font_desc_color == 'black'
    assert test_instance.font_title_color == 'black'

    test_instance.style = 'ROSEPINE'
    test_instance.set_style(test_instance.style)
    assert test_instance.bg_color == (38, 35, 58)
    assert test_instance.border_color == (235, 111, 146)
    assert test_instance.font_desc_color == (224, 222, 244)
    assert test_instance.font_title_color == (224, 222, 244)

    test_instance.style = 'GRUVBOX'
    test_instance.set_style(test_instance.style)
    assert test_instance.bg_color == (40, 40, 40)
    assert test_instance.border_color == (152, 151, 26)
    assert test_instance.font_desc_color == (215, 153, 33)
    assert test_instance.font_title_color == (157, 0, 6)

    test_instance.style = 'LIGHT'
    test_instance.set_style(test_instance.style)
    assert test_instance.bg_color == (255, 255, 255)
    assert test_instance.border_color == (12, 28, 112)
    assert test_instance.font_desc_color == (0, 0, 0)
    assert test_instance.font_title_color == (0, 0, 0)

    test_instance.style = 'DARK'
    test_instance.set_style(test_instance.style)
    assert test_instance.bg_color == (21, 25, 29)
    assert test_instance.border_color == (49, 59, 75)
    assert test_instance.font_desc_color == (111, 111, 111)
    assert test_instance.font_title_color == (111, 111, 111)

    test_instance.style = 'CUSTOM'
    test_instance.set_style(test_instance.style)
    assert test_instance.bg_color == (21, 25, 29)
    assert test_instance.border_color == (49, 59, 75)
    assert test_instance.font_desc_color == (111, 111, 111)
    assert test_instance.font_title_color == (111, 111, 111)
    # default case
    test_instance.style = 'gibberish'
    test_instance.set_style(test_instance.style)
    assert test_instance.bg_color == 'white'
    assert test_instance.border_color == 'white'
    assert test_instance.font_desc_color == 'black'
    assert test_instance.font_title_color == 'black'

def get_size():
    '''
    get_size() function stub
    '''
    panel_width = 400
    panel_height = 200
    assert panel_width, panel_height