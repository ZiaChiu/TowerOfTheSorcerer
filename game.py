"""A simple game development API for educational purposes.

This module was developed for educational purposes to provide a
a simple game development API to students with no prior knowledge of
TkInter or TK/TCL. It includes wrapper for tkinter.Tk and tkinter.Canvas
to ease their use for the purposes of game development.

Author: Michael Ulpen
Email: michael.ulpen@navitas.com
License: GPL
Date: 4 July 2021
"""
import abc
import math
import os
import time
import tkinter as tk

from PIL import Image as Img
from PIL import ImageTk


class Window(tk.Tk):
    """Window provides a simple graphic user interface for game development.

    Window extends tkinter.TK by providing some helpful methods for
    accessing the window size and state.By default, it provides a simple
    layout containing a 1-line text area and a canvas for drawing graphics
    and shapes.
    """

    def __init__(self, title="Game", width=1000, height=700,
                 master=None, default_layout=True):
        '''Creates Window.

        If default_layout is set to True, the window will be preconfigured
        to contain a 1-line text area and an 800x800 canvas
        '''
        super().__init__(master)

        self.title(title)
        self.geometry(str(width) + "x" + str(height) + "+0+0")
        self._canvas = None
        self.__text_area = None

        if default_layout:
            self.__text_area = tk.Label(self, font="18", text="", fg="black")
            self.__text_area.pack(side=tk.TOP)
            self._canvas = tk.Canvas(self, bg="light grey")
            self._canvas.pack(side=tk.BOTTOM, expand="YES", fill='both')

        self.update()
        self.__open = True
        self.__timer = time.time()
        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def destroy(self):
        """Closes the window.

        After the Window is destroyed a call to is_open will return false.
        Subsequent calls to other methods may fail with a _tkinter.TclError.
        """
        self.__open = False
        super().destroy()

    def is_open(self):
        """Returns True if the Window has not been closed.

        Otherwise returns False.
        """
        return self.__open

    def get_canvas(self):
        """Returns the canvas of the Window.

        """
        return self._canvas

    def get_canvas_width(self):
        """Returns the canvas's width.

        """
        return self._canvas.winfo_width()

    def get_canvas_height(self):
        """Returns the canvas's height.

        """
        return self._canvas.winfo_height()

    def set_text(self, new_text):
        """Changes the text in the Window's text field to new_text.

        Raises an AttributeError if default_layout was set to False.
        """
        if self.__text_area is not None:
            self.__text_area.config(text=str(new_text))
            self.update()

    def get_time_elapsed(self):
        """Returns seconds as a float since the last call to this method.

        Seconds is returned as a float with nanosecond precision.
        """
        secs = time.time()
        diff = secs - self.__timer
        self.__timer = secs
        return diff

    def bind_keys_to(self, function_arg):
        """Binds the argument function to all <KeyPress> events.

        The function_arg is the name of a function (without parentheses).
        This function will be called whenever a key is pressed down on
        the keyboard.
        """
        self.bind("<KeyPress>", function_arg)

    def __str__(self):
        return "game.Window"


class Game():
    """
    Game updates a list of GameObjects within a Window.

    Game should be inherited by another class.
    """

    def __init__(self):
        """Creates a Window and an empty list of GameObjects."""
        self._window = Window()
        self._gameObjects = []

    def add_game_obj(self, obj):
        """Adds the argument GameObject to the list."""
        self._gameObjects.append(obj)

    def _remove_game_obj(self, obj):
        """Removes the argument GameObject from the list.

        This should not be called directly;
        Call the GameObject's destroy() method instead."""
        self._gameObjects.remove(obj)

    def get_game_objs(self) -> list:
        """Returns all GameObjects as a list."""
        return self._gameObjects

    def get_window(self) -> Window:
        """Returns a reference to the window."""
        return self._window

    def run(self):
        """Starts a loop that updates all GameObjects and the window.

        Code written after calling run() may not execute until the
        Window is closed."""
        while self._window.is_open():
            timeElapsed = self._window.get_time_elapsed()
            for object in self.get_game_objs():
                object.update(timeElapsed)
            self._window.update()


class Vector2D:
    """Contains an x and y coordinate.
    A Vector2D may be used as a position, or a direction with length.
    """

    def __init__(self, x, y):
        """Constructs the Vector2D to the argument x and y."""
        self.x = x
        self.y = y

    def add(self, vec):
        """Adds the given Vector2D's x and y to this object's x and y.
        Returns as a new Vector2D."""
        return Vector2D(self.x + vec.x, self.y + vec.y)

    def subtract(self, vec):
        """Subtracts the given Vector2D's x and y to this object's x and y.
        Returns as a new Vector2D."""
        return Vector2D(self.x - vec.x, self.y - vec.y)

    def scale(self, scalar):
        """Scales the calling object by multiplying the x and y by the scalar.
        Returns as a new Vector2D."""
        return Vector2D(self.x * scalar, self.y * scalar)

    def length(self):
        """Calculates and returns the distance between (0, 0) and this object's (x, y).
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, vec):
        """Calculates and returns the distance between the given Vector2D's (x, y) and this object's (x, y).
        """
        return math.sqrt((self.x - vec.x) ** 2 + (self.y - vec.y) ** 2)

    def normalize(self):
        """Normalizes this object so that the vector is scaled to a length of 1.
        """
        length = self.length()
        if length != 0:
            return Vector2D(self.x / length, self.y / length)
        return Vector2D(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return 'Vector2D: ' + str(self.x) + ", " + str(self.y)

    def __repr__(self):
        return self.__str__()


class Rectangle:
    """A wrapper class for Rectangles drawn on the Window's canvas.

    Rectangle contains width, height, x, y coordinates and colour. This is
    designed to be used with a Tk canvas object. You can get the canvas
    from Window.get_canvas()
    """

    def __init__(self, position, w, h, window, colour=None):
        """Draws a width * height pixel Rectangle to the canvas at x, y.

        Rectangle will not be drawable if window is None.
        """
        self._position: Vector2D = Vector2D(position.x, position.y)
        self.__width = w
        self.__height = h
        self._window: Window = window
        self.__colour = colour
        self._id = None
        if window != None:
            self._draw()

    def _draw(self):
        """This is called by the __init__ method.
        Should not be called directly."""
        self._id = self._window.get_canvas().create_rectangle(
            self._position.x,
            self._position.y,
            self._position.x + self.__width,
            self._position.y + self.__height,
            fill=self.__colour,
            width=1)

    def get_x(self):
        """
        Returns the x coordinate of the Rectangle measured from top-left.

        """
        return self._position.x

    def get_y(self):
        """
        Returns the y coordinate of the Rectangle measured from top-left.
        """
        return self._position.y

    def get_position(self) -> Vector2D:
        """Returns the position as a Vector2D."""
        return self._position

    def get_width(self):
        """Returns the width of the Rectangle.
        """
        return self.__width

    def get_height(self):
        """Returns the height of the Rectangle.
        """
        return self.__height

    def set_width(self, w):
        """Changes the width of the Rectangle to the argument.
        """
        self.__width = w
        coords = self._window.get_canvas().coords(self._id)
        if len(coords) == 4:
            self._window.get_canvas().coords(self._id, coords[0], coords[1], coords[0] + w, coords[3])

    def set_height(self, h):
        """Changes the height of the Rectangle to the argument.
        """
        self.__height = h
        coords = self._window.get_canvas().coords(self._id)
        if len(coords) == 4:
            self._window.get_canvas().coords(self._id, coords[0], coords[1], coords[2], coords[1] + h)

    def move_by(self, dx, dy):
        """Adds the argument dx to the x coordinate and dy to the y coordinate.

        This can be used to move the Rectangle a given distance from its
        current position.
        """
        self._position.x += dx
        self._position.y += dy
        if self._window.get_canvas() != None:
            self._window.get_canvas().move(self._id, dx, dy)

    def move_to(self, x, y):
        """Sets the Rectangle's x and y coordinates to the argument x and y.
        """
        self.move_by(-self._position.x + x, -self._position.y + y)

    def get_id(self):
        """Returns the id of this object in the canvas.
        If canvas was set to None in __init__, this will return None.
        """
        return self._id

    def destroy(self):
        """Deletes the Rectangle from its canvas and sets its id and canvas to None.
        The Rectangle will not be drawable after a call to this method.
        """
        if self._window != None:
            self._window.get_canvas().delete(self._id)
            self._id = None
            self._window = None

    def __str__(self):
        """Returns a str representation of the Rectangle.
        Called automatically when the Rectangle is printed.
        """
        return "Rectangle: " + str(self._position.x) + "x, " + \
               str(self._position.y) + "y, " + str(self.get_width()) + "w, " + \
               str(self.get_height()) + "h"


class GameObject(Rectangle, metaclass=abc.ABCMeta):
    """
    Contains an image to be drawn in the attached Game's window.
    Subclasses of this must implement the abstract update method.
    Closely related to the Game class.
    """

    def __init__(self, position: Vector2D, width: float, height: float,
                 sourceImage: Img.Image, game: Game):
        """Initializes the argument image and attaches it to the Game.
        """
        self.__source = sourceImage
        self.__image = None
        self.__game = game
        self.__game.add_game_obj(self)
        super().__init__(position, width, height, game._window)

    def get_game(self) -> Game:
        """Returns the attached Game."""
        return self.__game

    def _draw(self):
        """This is called by the __init__ method.
        Should not be called directly."""
        if self._window != None:
            self.__image = ImageTk.PhotoImage(
                self.__source.resize((int(self.get_width()), int(self.get_height())),
                                     Img.NEAREST))
            self._id = self._window.get_canvas().create_image(self._position.x,
                                                              self._position.y, anchor=tk.NW, image=self.__image)

    def set_image(self, img):
        """May be called to change the source image.
        This can be used to animate the GameObject.
        """
        self.__source = img
        self.__image = ImageTk.PhotoImage(
            self.__source.resize((int(self.get_width()), int(self.get_height())),
                                 Img.NEAREST))
        if self._window != None:
            self._window.get_canvas().itemconfig(self._id, anchor=tk.NW, image=self.__image)

    def get_image(self) -> Img.Image:
        """Return the source image.
        """
        return self.__source

    def set_width(self, w):
        """Changes the width of the image/rectangle to the argument.
        """
        super().set_width(w)
        self.__image = ImageTk.PhotoImage(
            self.__source.resize((int(self.get_width()), int(self.get_height())),
                                 Img.NEAREST))
        if self._window != None:
            self._window.get_canvas().itemconfig(self._id, anchor=tk.NW, image=self.__image)

    def set_height(self, h):
        """Changes the height of the image/rectangle to the argument.
        """
        super().set_height(h)
        self.__image = ImageTk.PhotoImage(
            self.__source.resize((int(self.get_width()), int(self.get_height())),
                                 Img.NEAREST))
        if self._window != None:
            self._window.get_canvas().itemconfig(self._id, anchor=tk.NW, image=self.__image)

    def destroy(self):
        """Removes the GameObject from the attached Game and from its Window.
        """
        super().destroy()
        self.__game._remove_game_obj(self)

    @abc.abstractmethod
    def update(self, seconds):
        """Called automatically by the attached Game.
        This may be used to change the objects position, image, etc.
        Must be implemented by subclasses."""
        pass


class ImageLibrary:
    """ImageLibrary is a collection which maps .PNG images to names.
    Must first call the load method to read .PNG images from a folder.
    Then images may be accessed using their name, without the .png
    extension."""

    __images = {}

    def load(path):
        """Reads all .PNG images in the argument folder, and its
        subfolders. Each image is added to a dictionary using its
        name as the key. The names do not contain the .png extension.
        """
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith('.png'):
                    alias = name[: len(name) - 4]
                    image = Img.open(root + '/' + name)
                    ImageLibrary.__images[alias] = image

    def get(name) -> Img.Image:
        """Return the image associated with the argument key.
        """
        return ImageLibrary.__images[name]
