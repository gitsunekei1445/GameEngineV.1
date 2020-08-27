import glfw
from OpenGL.GL import *
import pyrr

class Gui():
    '''
    ########### GUI SYSTEM ###########
            - Create GUI window
            - Update GUI window
            - Close  GUI window
    ##################################
    '''
    def __init__(self,width,height,name,fullscreen,share):
        #
        self.widht      = width
        self.height     = height
        self.positionX  = 400
        self.positionY  = 200
        self.fullscreen = fullscreen
        self.name       = name
        self.share      = share
        self.gui        = None
        self.guiClose   = None
        #
        if not glfw.init():
            raise Exception('GLFW can not be created !')
        #
        self.gui = glfw.create_window(self.widht,self.height,self.name,self.fullscreen,self.share)
        #
        if not  self.gui:
            raise Exception('GLFW can not create window gui !')
        #
        glfw.set_window_pos(self.positionX,self.positionY)
        glfw.make_context_current(self.gui)
        #
        self.window_close = glfw.window_should_close(self.gui)

    def gui_update(self):
        glfw.poll_events()
        if not self.gui:
            raise Exception('GUI is not create !')
        else:
            glfw.swap_buffers(self.gui)

    def gui_terminate(self):
        glfw.terminate()

