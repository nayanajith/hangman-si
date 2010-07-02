from wxPython.wx import *
from wxPython.html import *
#import wxPython.lib.wxpTag

import  os.path, sys
path = "about"
version="0.1"

class HangmanAbout(wxDialog):
    text = '''
    <html>
    <body bgcolor="%s">
    <!-- <font size="-1"> -->
    <center>
    <table align="center" width="380" border="2" cellspacing="0">
    <tr>
    <td align="center"><img src="%s">
    </td></tr>
    <tr><td bgcolor="#000000" align="center">
    <font color="#ffffff">Hangman_si_ta Version %s on Python %s and wxPython %s
    </font>
    </td></tr>
    </table>
    </center>
    <!-- </font> -->
    <table border="0" cellpadding="0" cellspacing="0">
    <tr><td width="50"></td><td>
    <!-- <font size="-1"> -->
    <b><p>License: GPL (see <a href="show_license">license.txt</a>)</b><br>
    <!-- wxPyColourChooser code copyright (c) 2002-2004 <br>Michael Gilfix
    (wxWindows license) -->
    <p>Home page:
    <a href="http://code.google.com/p/hangman-si">http://code.google.com/p/hangman-si</a>
    <p>For credits, see
    <a href="show_credits">credits.txt</a>.<!-- </font> --></td>
    </tr></table>
    </body>
    </html>
    '''

    def __init__(self, parent=None):
        wxDialog.__init__(self, parent, -1, 'About Hangman-si-ta')
        class HtmlWin(wxHtmlWindow):
            def OnLinkClicked(self, linkinfo):
                href = linkinfo.GetHref()
                if href == 'show_license':
                    from wxPython.lib.dialogs import wxScrolledMessageDialog
                    try:
                        license = open(os.path.join(path,
                                                    'license.txt'))
                        dlg = wxScrolledMessageDialog(self, license.read(),
                                                      "Hangman-si-ta - License")
                        license.close()
                        dlg.ShowModal()
                        dlg.Destroy()
                    except IOError:
                        wxMessageBox("Can't find the license!\n"
                                     "You can get a copy at \n"
                                     "http://www.opensource.org/licenses/"
                                     "mit-license.php", "Error",
                                     wxOK | wxCENTRE | wxICON_EXCLAMATION)
                elif href == 'show_credits':
                    from wxPython.lib.dialogs import wxScrolledMessageDialog
                    try:
                        credits = open(os.path.join(path,
                                                    'credits.txt'))
                        dlg = wxScrolledMessageDialog(self, credits.read(),
                                                      "Hgnmang-si-ta - Credits")
                        credits.close()
                        dlg.ShowModal()
                        dlg.Destroy()
                    except IOError:
                        wxMessageBox("Can't find the credits file!\n", "Oops!",
                                     wxOK | wxCENTRE | wxICON_EXCLAMATION)
                else:
                    import webbrowser
                    webbrowser.open(linkinfo.GetHref(), new=True)
        html = HtmlWin(self, -1, size=(400, -1))
        py_version = sys.version.split()[0]
        bgcolor = "whitesmoke"
        icon_path = os.path.join(path,
                                 'hangman.png')
        html.SetPage(self.text % (bgcolor, icon_path, version,
                                  py_version, wx.__version__))
        ir = html.GetInternalRepresentation()
        ir.SetIndent(0, wxHTML_INDENT_ALL)
        html.SetSize((ir.GetWidth(), ir.GetHeight()))
        szr = wxBoxSizer(wxVERTICAL)
        szr.Add(html, 0, wxTOP | wxALIGN_CENTER, 10)
        szr.Add(wxStaticLine(self, -1), 0, wxLEFT | wxRIGHT | wxEXPAND, 20)
        szr2 = wxBoxSizer(wxHORIZONTAL)
        btn = wxButton(self, wxID_OK, "OK")
        btn.SetDefault()
        szr2.Add(btn)
        if wxPlatform == '__WXGTK__':
            extra_border = 5 # border around a default button
        else: extra_border = 0
        szr.Add(szr2, 0, wxALL | wxALIGN_RIGHT, 20 + extra_border)
        self.SetAutoLayout(True)
        self.SetSizer(szr)
        szr.Fit(self)
        self.Layout()
        if parent: self.CenterOnParent()
        else: self.CenterOnScreen()

# end of class HangmanAbout


if __name__ == '__main__':
    wxInitAllImageHandlers()
    app = wxPySimpleApp()
    d = HangmanAbout()
    app.SetTopWindow(d)
    d.ShowModal()
