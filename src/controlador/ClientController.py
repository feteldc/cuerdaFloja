import wx
from controlador.controlador import Rompecabeza
        
if __name__ == "__main__":
    app = wx.App()
    Rompecabeza().Show()
    app.MainLoop() 