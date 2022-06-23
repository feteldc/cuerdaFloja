import imagen as dyrke
import os
import wx
import random 


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)
        
        self.Centre()
        self.createWidgets()

    def createWidgets(self):

        self.panel = wx.Panel(self, -1)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        st = wx.StaticText(self.panel, label="Puzzle Game", style=wx.ALIGN_CENTER_HORIZONTAL)
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        self.cb = wx.ComboBox(self.panel, choices=['2', '3', '4'], style=wx.CB_READONLY, size=(400, 20))
        self.cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        self.vbox.Add(st, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        self.vbox.Add(self.cb, 0, wx.LEFT | wx.RIGHT ,50)

        self.panel.SetSizerAndFit(self.vbox)
        
       
    def OnSelect(self, e):

        self.cb.Enable(False)
        panel_juego = wx.Panel(self, -1)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        dyrke.vaciar_carpeta('screenshots')
        d = int(e.GetString())
        grid = wx.GridSizer(d, d, 0, 0)
        dyrke.cortar_imagen('gato1.png', 'screenshots', d)

        images = os.listdir('screenshots')
        random.shuffle(images)
        for i in images:
            pic = wx.Image(os.path.join('screenshots',i), wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            button = wx.BitmapButton(self.panel, wx.ID_ANY, pic)
            button.Bind(wx.EVT_BUTTON, self.doMe, button)
            grid.Add(button, 0)

        hbox.Add(grid, 0, wx.TOP | wx.LEFT, 70)
        panel_juego.SetSizerAndFit(hbox)
        
    def doMe(self, e):
        pass
        
    


# Set the app root to main page
if __name__ == "__main__":
    app = wx.App()
    ex = Example(None, title='CuerdaFloja')
    ex.Show()
    app.MainLoop()