from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 

def tower_of_the_sorcerer_window():
    app = QApplication(sys.argv)
    application_window = QMainWindow()
    application_window.setGeometry(200,200,300,300) # x-coordinates, y-coordinates, width, height
    application_window.setWindowTitle("Tower of The Sorcerer") # 設應用名稱


    application_window.show() # display the GUI interface
    sys.exit(app.exec_()) # enable the user to exit the GUI through clicking the exit button




tower_of_the_sorcerer_window()