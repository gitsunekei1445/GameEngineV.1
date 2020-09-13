# Example Create GUI Window
# Import package name   (my package create)
# GameGame Module name GUI
import sys

from GameEngine import GUI
win=GUI.Gui()
#
winApp=win.gui_create(400,300,"Test")

while not win.gui_Close:
    win.gui_update()

win.gui_terminate()
