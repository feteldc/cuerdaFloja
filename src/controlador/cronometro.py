import time
import wx

class Cronometro(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title='Static Example')
        panel = wx.Panel(self)
        self.counter = 300

        font = wx.Font(24, wx.FONTFAMILY_ROMAN,
                       wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_BOLD)

        self.lbl = wx.StaticText(panel, label='5:00')
        self.lbl.SetFont(font)

        btn = wx.Button(panel, label='Start Countdown')
        btn.Bind(wx.EVT_BUTTON, self.start)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lbl, 0, wx.ALL, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

        self.Show()

    def start(self, event):
        self.timer.Start(1000)

    def update(self, event):
        if self.counter == 0:
            self.timer.Stop()
            self.lbl.SetLabel('KA-BOOM!')
            return
        else:
            minutes = self.counter //60
            seconds = self.counter -(minutes*60)
            self.counter -= 1

        self.lbl.SetLabel(f"{str(minutes)}:{str(seconds)}")


if __name__ == '__main__':
    app = wx.App(False)
    frame = Cronometro()
    app.MainLoop()