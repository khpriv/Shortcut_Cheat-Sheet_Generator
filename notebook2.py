import sys

import PIL.ImageOps
from PIL import Image


def main():
    try:
        shirt, before = openfile(sys.argv)
        after_name = sys.argv[2].lower()
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')
    size_of_shirt = shirt.size
    after = PIL.ImageOps.fit(before, size_of_shirt)
    # fit is done correctly
    after.paste(shirt, (0, 0), shirt)
    after.save(f'{after_name}')


def openfile(filename):
    """
    Checks file for validity and opens it, if valid
    """
    if len(sys.argv) == 3:
        try:
            name1, extension1 = sys.argv[1].lower().strip().split('.')
            name2, extension2 = sys.argv[2].lower().strip().split('.')
        except ValueError:
            sys.exit('Wrong file name')
        if (extension1 not in ('png', 'jpg', 'jpeg')) or (extension2 not in ('png', 'jpg', 'jpeg')):
            sys.exit('Invalid output')
        elif extension1 != extension2:
            sys.exit('Input and output have different extensions')
        else:
            shirt = Image.open('shirt.png')
            before = Image.open(sys.argv[1])

            return shirt, before
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')


if __name__ in '__main__':
    main()