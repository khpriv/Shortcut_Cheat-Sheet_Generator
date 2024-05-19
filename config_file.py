import sys
import PIL
from PIL import Image, ImageDraw, ImageFont


class ConfigurationClass:

    filename = ''
    banner_title = ''
    margines = 0
    line_spacing = 0
    font_size_desc = 0
    font_size_title = 0
    default_width_of_panel = 0
    font = ""
    style = ""
    description_action = ()
    description_key = ()
    bg_color = ""
    border_color = ""
    font_desc_color = ""
    font_title_color = ""
    banner_height = 0
    default_line_height = 0


    def __init__(self):

        self.filename = "PyCharm"
        # Leave as "" if You don't want to add title banner
        self.banner_title = "PyCharm keybinds"
        # margin
        self.margines = 20
        # multiline text line spacing
        self.line_spacing = 20
        self.font_size_desc = 25
        self.font_size_title = 70
        # Controls how far apart "action" and "key" columns are
        self.default_width_of_panel = 420
        # self.font = "arial.ttf"  # font for windows machines
        self.font = "DroidSans.ttf"  # font for Linux Machines

        # uncomment one style
        # self.style = 'OLED'
        # self.style = 'printer'
        self.style = 'ROSEPINE'
        # self.style = 'GRUVBOX'
        # self.style = 'LIGHT'
        # self.style = 'DARK'
        # self.style = 'CUSTOM' # feel free to create color scheme that suits you

        # Make sure that every "key" has its "action", \n is also ok.
        self.description_action = ((f'Run/Debug\n'
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
        self.description_key = ((f'Shift + F10/F9\n'
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

        try:
            self.font_title = ImageFont.truetype(self.font, self.font_size_title)
            self.font_desc = ImageFont.truetype(self.font, self.font_size_desc)
        except OSError:
            sys.exit("Font can't be found or opened")


        # default colors
        self.bg_color = 'white'
        self.border_color = 'white'
        self.font_desc_color = 'black'
        self.font_title_color = 'black'

        self.banner_height = self.font_size_title * 2
        self.default_line_height = self.font_size_desc + self.line_spacing

    def set_style(self, styl):
        match styl:
            case 'OLED':
                self.bg_color = 'black'
                self.border_color = 'grey'
                self.font_desc_color = 'lightgray'
                self.font_title_color = 'lightgray'
            case 'printer':
                self.bg_color = 'white'
                self.border_color = 'lightgray'
                self.font_desc_color = 'black'
                self.font_title_color = 'black'
            case 'ROSEPINE':
                self.bg_color = 38, 35, 58
                self.border_color = 235, 111, 146
                self.font_desc_color = 224, 222, 244
                self.font_title_color = 224, 222, 244
            case 'GRUVBOX':
                self.bg_color = 40, 40, 40
                self.border_color = 152, 151, 26
                self.font_desc_color = 215, 153, 33
                self.font_title_color = 157, 0, 6
            case 'LIGHT':
                self.bg_color = 255, 255, 255
                self.border_color = 12, 28, 112
                self.font_desc_color = 0, 0, 0
                self.font_title_color = 0, 0, 0
            case 'DARK':
                self.bg_color = 21, 25, 29
                self.border_color = 49, 59, 75
                self.font_desc_color = 111, 111, 111
                self.font_title_color = 111, 111, 111
            case 'CUSTOM':
                # use color described as RGB color.
                self.bg_color = 21, 25, 29
                self.border_color = 49, 59, 75
                self.font_desc_color = 111, 111, 111
                self.font_title_color = 111, 111, 111
            case _:
                self.bg_color = 'white'
                self.border_color = 'white'
                self.font_desc_color = 'black'
                self.font_title_color = 'black'
