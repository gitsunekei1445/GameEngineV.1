# Example Create GUI Window
# Import package name   (my package create)
# GameGame Module name GUI
import sys
from OpenGL.GL import glClear,GL_COLOR_BUFFER_BIT,glClearColor


from GameEngine import GUI
from GameEngine.Rendering import Render
import pyrr
import glfw
from OpenGL.GL import *

win=GUI.Gui()
glfw.init()
time1 = glfw.get_time()
winApp=win.gui_create(1270,800,"Test")

Render.set_background(0.5,0.5,0.5,1.0)

Render.render_model("Bin/model1.obj","Bin/texture1.png")
time2 = glfw.get_time()

print(time2-time1)
while not win.gui_Close:

    Render.render_update()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    Render.model_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))

    glBindVertexArray(Render.VAO[0])
    glBindTexture(GL_TEXTURE_2D, Render.textures[0])
    glUniformMatrix4fv(Render.model_loc, 1, GL_FALSE, Render.model_pos)

    glDrawArrays(GL_TRIANGLES, 0, len(Render.model_indices))

    win.gui_update()
    win.gui_showFPS()
win.gui_terminate()
