import wx
from controlador.controlador import Rompecabeza
from controlador.cronometro import Cronometro 
        
if __name__ == "__main__":
    app = wx.App()
    Rompecabeza().Show()
    Cronometro().Show()
    app.MainLoop()
    
