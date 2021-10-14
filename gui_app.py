"""
This is the GUI module for project
"""
import sys
import PyQt5.QtWidgets as Qt
from log import Log


# from PyQt5.QtWidgets import QApplication, QMainWindow  # pylint: disable=E0611


class TowerOfTheSorcererWindow(Qt.QMainWindow):
    """
    This is the window's main class.
    """

    def __init__(self):
        super().__init__()
        self.init_gui()
        self.setGeometry(200, 200, 300, 300)  # x-coordinates, y-coordinates, width, height
        self.setWindowTitle("Tower of The Sorcerer")  # 設應用名稱

    def init_gui(self):
        """ Code goes here """
        Log('running', 'info', sys._getframe().f_lineno)  # pylint: disable=W0212



def tower_of_the_sorcerer_window():
    '''

    :return:
    '''
    app = Qt.QApplication(sys.argv)
    application_window = TowerOfTheSorcererWindow()

    application_window.show()  # display the GUI interface
    sys.exit(app.exec_())  # enable the user to exit the GUI through clicking the exit button


tower_of_the_sorcerer_window()
