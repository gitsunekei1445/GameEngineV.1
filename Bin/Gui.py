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
        # variable in Class GUI
        self.widht      = width
        self.height     = height
        self.positionX  = 400
        self.positionY  = 200
        self.fullscreen = fullscreen
        self.name       = name
        self.share      = share
        self.gui        = None
        self.gui_Close   = None
        # Setup and catch GLFW INIT Lisbrary
        if not glfw.init():
            raise Exception('GLFW can not be created !')
        # Setup GUI from GLFW Library
        if fullscreen == True:
            self.fullscreen = glfw.get_primary_monitor()
        self.gui = glfw.create_window(self.widht,self.height,self.name,self.fullscreen,self.share)
        # Catch GUI create on project
        if not  self.gui:
            raise Exception('GLFW can not create window gui !')
        # Setup GUI position on scene X and Y
        glfw.set_window_pos(self.gui,self.positionX,self.positionY)
        # Setup context current on GUI
        glfw.make_context_current(self.gui)
        # Setup gui close event
        self.gui_Close = glfw.window_should_close(self.gui)

    def gui_update(self):
        glfw.poll_events()
        if not self.gui:
            raise Exception('GUI is not create !')
        else:
            glfw.swap_buffers(self.gui)
            self.gui_Close = glfw.window_should_close(self.gui)


    def gui_terminate(self):
        glfw.terminate()

