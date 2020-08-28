#Example Create GUI Window
from Bin.Gui import *
import glfw
#
winGui = Gui(1200,600,'test',None,None)
#
while not winGui.gui_Close:
    #
    winGui.gui_update()
#
winGui.gui_terminate()