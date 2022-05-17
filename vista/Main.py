import wx
from controlador.controlador import Problem
 
        
if __name__ == "__main__":
    app = wx.App()
    Problem().Show()
    app.MainLoop()
    
