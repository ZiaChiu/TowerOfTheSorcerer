from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 



class Tower_of_the_sorcerer_window(QMainWindow):
    def __init__(self):
        super(Tower_of_the_sorcerer_window,self).__init__()
        self.initGUI()
        self.setGeometry(200,200,300,300) # x-coordinates, y-coordinates, width, height
        self.setWindowTitle("Tower of The Sorcerer") # 設應用名稱

    def initGUI(self):
        """ Code goes here """
        pass    


def tower_of_the_sorcerer_window():
    app = QApplication(sys.argv)
    application_window = Tower_of_the_sorcerer_window()


    application_window.show() # display the GUI interface
    sys.exit(app.exec_()) # enable the user to exit the GUI through clicking the exit button

tower_of_the_sorcerer_window()