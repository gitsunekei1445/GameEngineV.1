#Example Create GUI Window
# Import package name   (my package create)
# GameGame Module name GUI
from GameEngine import GUI
win=GUI.Gui()
# win2 = GUI.Gui()
winApp=win.gui_create(400,300,"Test")
# winApp1=win2.gui_create(400,300,"Test2")
while not win.gui_Close:
    win.gui_update()
    # win2.gui_update()
# win2.gui_terminate()
win.gui_terminate()

