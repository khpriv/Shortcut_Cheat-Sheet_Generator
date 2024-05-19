# KEY SHORTCUT CHEAT-SHEET GENERATOR
#### Video Demo:  <URL HERE>
### Description:
A script to generate cheat sheets with keybinds.

Easy and fast way to create an image that lists an action and associated keybind. 
Useful for learning shortcuts to new software, complex game shortcuts, having printed out shortcuts
for software you rarely use (color scheme made for printing).
It can also be used for just about any text (up to a reasonable point)

## Examples

### IDE Shortcuts - PyCharm Community Edition
<picture><img src="PyCharm_final.png"></picture>


### Board Game cheat sheet for print - Ticket to Ride: Europe

<picture><img src="board_game_example_final.png"></picture>

### Video Game keymap for OLED screen - ARMA Reforger

<picture><img src="ARMA_final.png"></picture>

## Usage

To create a new keymap description, you need to modify existing list in 
the project.py file. Every action should have a matching key, so the lines are kept
in aligment (You can just use \n - newline character to accomplish that). 
You can add more elements to the list, whill will result in creating another
panel (see PyCharm keymap example)

Following code
```Python
description_action = ((f'Action 1\n'
                       f'Action 2\n'
                       f'Action 3\n'
                       f'Action 4\n'
                       ), (
                       f'Action 5\n'
                       f'Action 6\n'
                       f'Action 7\n'
                       f'Action 8\n'
                       ))
description_key = ((f'key for Action 1\n'
                    f'key for Action 2\n'
                    f'key for Action 3\n'
                    f'key for Action 4\n'
                    ), (
                    f'key for Action 5\n'
                    f'key for Action 6\n'
                    f'key for Action 7\n'
                    f'key for Action 8\n'
                    ))
```
will result in showing following table:

<picture><img src="Usage_Example_final.png"></picture>
If the Action and Key description overlap each other you are able to increase the spacing between them with 
***default_width_of_panel*** parameter value.

### Color schemes

There are 6 color schemes included, so there should be something for you if you 
are dark or light user, have an OLED display or want something fancy. 
You can also create your own, so it matches your themes in your other software.
To use them just comment out the assigment of the variable in project.py, 
so your style of choice is assigned.

Configuration and strings to be included are kept at the top of the project.py file.
> [!IMPORTANT] 
> Make sure you use font that your Python runtime has access to.

Dependencies (also listed inside requirements.txt):
- sys
- pillow

Tested on Python 3.11 and 3.12

### Ideas for next changes

- move configuration to separate file (JSON or xml)
  - Moved to other .py file and there is a class that contains the configuration
- move action and key list to separate file (csv?)
  - Moved to other .py file and there is a class that contains the configuration
- more error handling
- GUI

### checklist
- [x] main i 3 funckje
- [ ] testy do 3 funkcji
- [ ] Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.
- [x] Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main
- [ ] Your test functions must be in a file called test_project.py, which should also be in the “root” of your project.
- [x] Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project.
- [x] What will your software do? What features will it have? How will it be executed?
- [ ] What new skills will you need to acquire? What topics will you need to research?
- [x] Color schemes - OLED/GRUBBOX/ROSEPINE/PRINT/WHITE THEME/DARK THEME