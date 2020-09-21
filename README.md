# GameEngineV.1
Branch GUI on Graphic User Interface
``` Module name GUI
Class Gui
  Variable
    Globle
      timerAfter= 0
      timerOn= False
      timerStart = 0
      fps=0
    Object
      self.width = 400
      self.height = 300
      self.position_X = 400
      self.position_Y = 200
      self.fullscreen = None
      self.title = "GUI"
      self.share = None
      self.gui = None
      self.gui_Close = None
      self.icon_Referance = 'icon.png'
      self.icon = None
  function 
    gui_create(width,height,title)
    gui_update()
    gui_terminate()
    gui_setFullSrceenMode()
    gui_setWindowMode()
    gui_setTitle(title)
    gui_setSizeWindow(width,height)
    gui_setIconWindow(path)
    gui_ShowFPS()
```   
