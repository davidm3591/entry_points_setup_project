import wx


class DemoPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        labels = ["Name", "Address", "City", "State",
                  "Zip", "Phone", "Email", "Notes"]

        mainSizer = wx.BoxSizer(wx.VERTICAL)
