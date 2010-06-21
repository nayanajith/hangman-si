from hangman.hangman import Hangman
import wx


def main():
   app = wx.PySimpleApp(0)
   wx.InitAllImageHandlers()
   frame_2 = Hangman(None, -1, "")
   app.SetTopWindow(frame_2)
   frame_2.Show()
   app.MainLoop()


if __name__ == '__main__':
   main()

