# Example Create GUI Window
# Import package name   (my package create)
# GameGame Module name GUI
import sys
from OpenGL.GL import glClear,GL_COLOR_BUFFER_BIT,glClearColor


from GameEngine import GUI
from GameEngine.Rendering import Render
from OpenGL.GL import *

win=GUI.Gui()

winApp=win.gui_create(1270,800,"Test")
Render.set_background(0.5,0.5,0.5,1.0)
Render.draw_rect(0,0)
while not win.gui_Close:
    glDisableClientState(GL_VERTEX_ARRAY)
    Render.render_update()

    glDrawArrays(GL_POLYGON, 0, 4)

    win.gui_update()
    win.gui_showFPS()
win.gui_terminate()




