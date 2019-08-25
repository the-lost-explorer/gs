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
        '-g',
        '--grid',
        type = int,
        help='Specifies how often you want grid lines on the screen. \n 1 means 1 line after every pixel line and 50 means 1 line after every 50 pixel lengths. \n Default = 50') 
    


    args = parser.parse_args()
    print(args)
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
    elif(type(args.grid) != int):
        args.grid = 50
        print('Since grid intensity was not specified/non-integer value was given, it will be assumed as 50.')
        print('Canvas generated.')
    else:
        print('Canvas generated.')

    app = gs.GS(height=int(args.length), width=int(args.width), lines = int(args.grid))
    app.mainloop()


if __name__ == '__main__':
    main()
