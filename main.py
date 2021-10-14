"""
Author : ZIA CHIU
EMAIL: admin@crazyziye.xyz
Website： www.crazyziye.top
license：GPL
Created DATE: 29/9/21 10:34 pm
"""

from game import *


class MainGame(Game):

    def __init__(self):
        super().__init__()


def main():
    ImageLibrary.load("data/image")
    mainWindows = MainGame()
    mainWindows.run()


if __name__ == '__main__':
    main()
