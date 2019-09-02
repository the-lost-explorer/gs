#!/usr/bin/env python
"""gs is an effort at enabling creation of graphical simulations on variable displays!"""

import argparse
from gs import gs


def main():
    """Main entry point for cli."""
    parser = argparse.ArgumentParser(
        description='Graphics Simulator '
        ': Simulate all resolution graphical displays!'
    )

    parser.add_argument(
        '-l',
        '--length',
        type = int,
        help='Get a grid of pixels with the given height and width as output ')

    parser.add_argument(
        '-w',
        '--width',
        type = int,
        help='Get a grid of pixels with the given height and width as output ')

    parser.add_argument(
        '-m',
        '--mode',
        type = str,
        help='Specify the screen mode.') 
    
    args = parser.parse_args()

    if((type(args.length) != (int)) and (type(args.width) != (int))):
        print('Enter height and width as integer numbers.')
        print('They define the number of horizontal and verticle pixels on your screen and cannot be fractional.')
        exit(1)
    elif(type(args.length) != int):
        args.length = args.width
        print('Since length was not specified/non-integer value was given, it will be assumed to be same as width')
        print('Canvas generated.')
    elif(type(args.width)!= int):
        args.width = args.length
        print('Since width was not specified/non-integer value given, it will be assumed to be same as length')
        print('Canvas generated.')
    elif(type(args.mode) != str):
        args.mode = "g 50"
        print('No mode specified. Using pixel space.')
        print('Canvas generated.')
    else:
        print('Canvas generated.')

    app = gs.GS(height=int(args.length), width=int(args.width), mode = str(args.mode))
    app.mainloop()


if __name__ == '__main__':
    main()
