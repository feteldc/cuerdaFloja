import wx
import wx.grid as gridlib
from wx.grid import GridCellAutoWrapStringRenderer
from hashlib import new

##
#creamos nuestra clase en la cual se crea y configura la interfaz grafica
##
class Rompecabeza(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="CUERDA FLOJA", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(800,600))
        
       
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(10,0),size=(760, 680))
        self.lbl1 = wx.StaticText(self.box1, -1, pos =(10,25))
        
        
      
        self.lbl1 = wx.StaticText(self.box1, -1, 'Dificultad', pos =(605,15))
        self.btn1 =wx.Button(self.box1, label= "facil", size=(130,30),pos=(600,32))
                             
   
        self.btn2= wx.Button(self.box1, label="iniciar partida",size=(150,50),pos=(300,480))
        self.lbll= wx.StaticText(self.box1, -1,"Escoger imagen",pos =(20,15))
        self.btn3=wx.Button(self.box1, label="intermedio",size=(130,30),pos=(600,65))
        self.btn4=wx.Button(self.box1, label="Dificil", size= (130,30), pos=(600,98))

        self.grid = gridlib.Grid(self.panel,-1,size=(500,32),pos=(20,60))
        self.grid.SetDefaultRenderer(GridCellAutoWrapStringRenderer())
        self.grid.CreateGrid(0, 2)
        
        self.archivo = wx.Menu()
# Agregamos el sub-menú Guardar
        self.guardar = wx.MenuItem(self.archivo,-1,"Guardar")
        self.guardar.SetBitmap(wx.Bitmap("",wx.BITMAP_TYPE_ANY ))
        self.archivo.AppendItem(self.guardar)
# Agregamos el sub-menú Abrir
        self.abrir = wx.MenuItem(self.archivo,-1,"Abrir")
        self.abrir.SetBitmap(wx.Bitmap("", wx.BITMAP_TYPE_ANY ))
        self.archivo.AppendItem(self.abrir)
    
    # Creamos la barra de menú principal y la configuramos
        self.mb = wx.MenuBar()
        self.mb.Append(self.archivo, "Archivo")
        self.SetMenuBar(self.mb)
        
    
    