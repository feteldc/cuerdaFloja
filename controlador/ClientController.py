import wx
from controlador import controlador
        
if __name__ == "__main__":
    app = wx.App()
    controlador().Show()
    app.MainLoop() 