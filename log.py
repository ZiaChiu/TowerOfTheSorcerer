"""
Author : ZIA CHIU
EMAIL: admin@crazyziye.xyz
Website： www.crazyziye.top
license：GPL
Created DATE: 29/9/21 10:34 pm
"""
import sys
import time


class Log:
    """
    Log class is to imitate the log classification system of android studio to help users debug.
    """

    def __init__(self, text: str, category: str, line: int):
        """

        :param text: the content of log
        :param category: the type for log
        :param line: log location, such as line equal 1 that will print "[1]..."
        """

        # 顯示方式: 0（默認值）、1（高亮）、4（下劃線）、 5（閃爍）、7（反顯）、22（非粗體）、24（非下劃線）、25（非閃爍）、27（非反顯）
        # 前景色: 30（黑色）、31（紅色）、32（綠色）、 33（黃色）、34（藍色）、35（洋 紅）、36（青色）、37（白色）
        # 背景色: 40（黑色）、41（紅色）、42（綠色）、 43（黃色）、44（藍色）、45（洋 紅）、46（青色）、47（白色）
        #

        self.style = [0, 1, 4, 5, 7, 22, 24, 25, 27]
        self.color = [30, 31, 32, 33, 34, 35, 36, 37]
        self.background = [40, 41, 42, 43, 44, 45, 46, 47]
        self.text = text
        self.category = category
        self.line = line
        self.command = ['error',
                        'debug',
                        'warning',
                        'info']
        self.run()

    def run(self):
        """
        Start function
        :return: func
        """
        if self.category.lower() not in self.command:
            raise ValueError('ERROR: wrong category for log!!!')
        if self.category.lower() == 'error':
            self.__error()
        elif self.category.lower() == 'debug':
            self.__debug()
        elif self.category.lower() == 'warning':
            self.__warning()
        elif self.category.lower() == 'info':
            self.__info()

    def __str__(self):
        return self.text

    @staticmethod
    def get_time():
        """
        getting system time.
        :return: time
        """
        time_return = "[" + \
                      str(time.localtime(time.time()).tm_year) + "/" + \
                      str(time.localtime(time.time()).tm_mon) + "/" + \
                      str(time.localtime(time.time()).tm_mday) + "{" + \
                      str(time.localtime(time.time()).tm_hour) + ":" + \
                      str(time.localtime(time.time()).tm_min) + ":" + \
                      str(time.localtime(time.time()).tm_sec) + "}" + \
                      "]"

        return time_return

    def __info(self, style=1, background=40, color=31):
        """

        :param style:0 (default),
                     1 (highlight),
                     4 (underline),
                     5 (flashing),
                     7 (reverse display),
                     22 (non-bold),
                     24 (non-underline),
                     25 (non-flashing),
                     27 (non-reversed)
        :param background: 40 (black),
                   41 (red),
                   42 (green),
                   43 (yellow),
                   44 (blue),
                   45 (magenta),
                   46 (cyan),
                   47 (white)
        :param color: 30 (black),
                      31 (red),
                      32 (green),
                      33 (yellow),
                      34 (blue),
                      35 (magenta),
                      36 (cyan),
                      37 (white)
        :return: log string
        """
        if style not in self.style:
            raise ValueError("wrong style number!!!")
        if background not in self.background:
            raise ValueError("wrong background color number!!!")
        if color not in self.color:
            raise ValueError("wrong text color number!!!")
        print('\033[' + str(style) + ';' +
              str(color) + ';' +
              str(background) + 'm' + "[" + str(self.line) + "]" + str(self.get_time()) +
              "INFO:" + self.text + '\033[0m')

    def __error(self, style=4, background=40, color=37):
        """

        :param style:0 (default),
                     1 (highlight),
                     4 (underline),
                     5 (flashing),
                     7 (reverse display),
                     22 (non-bold),
                     24 (non-underline),
                     25 (non-flashing),
                     27 (non-reversed)
        :param background: 40 (black),
                   41 (red),
                   42 (green),
                   43 (yellow),
                   44 (blue),
                   45 (magenta),
                   46 (cyan),
                   47 (white)
        :param color: 30 (black),
                      31 (red),
                      32 (green),
                      33 (yellow),
                      34 (blue),
                      35 (magenta),
                      36 (cyan),
                      37 (white)
        :return: log string
        """
        if style not in self.style:
            raise ValueError("wrong style number!!!")
        if background not in self.background:
            raise ValueError("wrong background color number!!!")
        if color not in self.color:
            raise ValueError("wrong text color number!!!")

        print('\033[' + str(style) + ';' +
              str(color) + ';' +
              str(background) + 'm' + "[" + str(self.line) + "]" + str(self.get_time()) +
              "ERROR:" + self.text + '\033[0m')

    def __debug(self, style=1, background=40, color=32):
        """

        :param style:0 (default),
                     1 (highlight),
                     4 (underline),
                     5 (flashing),
                     7 (reverse display),
                     22 (non-bold),
                     24 (non-underline),
                     25 (non-flashing),
                     27 (non-reversed)
        :param background: 40 (black),
                   41 (red),
                   42 (green),
                   43 (yellow),
                   44 (blue),
                   45 (magenta),
                   46 (cyan),
                   47 (white)
        :param color: 30 (black),
                      31 (red),
                      32 (green),
                      33 (yellow),
                      34 (blue),
                      35 (magenta),
                      36 (cyan),
                      37 (white)
        :return: log string
        """
        if style not in self.style:
            raise ValueError("wrong style number!!!")
        if background not in self.background:
            raise ValueError("wrong background color number!!!")
        if color not in self.color:
            raise ValueError("wrong text color number!!!")

        print('\033[' + str(style) + ';' +
              str(color) + ';' +
              str(background) + 'm' + "[" + str(self.line) + "]" + str(self.get_time()) +
              "DEBUG:" + self.text + '\033[0m')

    def __warning(self, style=1, background=40, color=36):
        """

        :param style:0 (default),
                     1 (highlight),
                     4 (underline),
                     5 (flashing),
                     7 (reverse display),
                     22 (non-bold),
                     24 (non-underline),
                     25 (non-flashing),
                     27 (non-reversed)
        :param background: 40 (black),
                   41 (red),
                   42 (green),
                   43 (yellow),
                   44 (blue),
                   45 (magenta),
                   46 (cyan),
                   47 (white)
        :param color: 30 (black),
                      31 (red),
                      32 (green),
                      33 (yellow),
                      34 (blue),
                      35 (magenta),
                      36 (cyan),
                      37 (white)
        :return: log string
        """
        if style not in self.style:
            raise ValueError("wrong style number!!!")
        if background not in self.background:
            raise ValueError("wrong background color number!!!")
        if color not in self.color:
            raise ValueError("wrong text color number!!!")

        print('\033[' + str(style) + ';' +
              str(color) + ';' +
              str(background) + 'm' + "[" + str(self.line) + "]" + str(self.get_time()) +
              "WARNING:" + self.text + '\033[0m')


L = Log('Hello world','error',sys._getframe().f_lineno)