#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2008 Nayanajit Mahendra Laxaman mail: nmlaxaman@gmail.com
# Copyright (C) 2008 Vincent Halahakone mail: halahakone@gmail.com

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

from 	   string import strip
from     wxPython.wx import *
import   re, random, sys, os

class Config(wxDialog):
   def __init__(self, LANG_DICT, DATA_DIR, CONFIG):
      wxDialog.__init__(self)

      self.LANG_DICT    =  LANG_DICT
      self.DATA_DIR     =  DATA_DIR
      self.CONFIG 	   =  CONFIG

      self.scope_dict   = {}
      self.TITLE_SCOPE  = ""
      self.LEVEL        = 1

      self.SetFont(self.DEFAULT_FONT)
      self.SetSize(size=(self.FONT_SIZE * 24, 250))
      self.SetTitle(self.LANG_DICT["CONFIGURE"])
      
      vbox_top = BoxSizer(wx.VERTICAL)
      panel    = Panel(self, -1)
      vbox     = BoxSizer(wx.VERTICAL)
      panel1   = Panel(panel, -1)
      grid1    = GridSizer(2, 2)

      grid1.Add(StaticText(panel1,
         - 1,
         self.LANG_DICT["CATEGORY"] + " :",
         (5, 5)),
         0,
         ALIGN_CENTER_VERTICAL)
      
      self.scope_combo = ComboBox(panel1, -1, size=(150, -1)) 
      for filename in os.listdir(self.DATA_DIR):
         file = open(self.DATA_DIR + "/" + filename)
         scope = file.readline().decode("UTF-8").rstrip("\n")
         self.scope_dict[scope] = filename
         self.scope_combo.Append(scope)
      grid1.Add(self.scope_combo)
      
      item_id = 0 
      for item in self.scope_combo.GetStrings():
         if item == self.TITLE_SCOPE:
            self.scope_combo.SetSelection(item_id)
         item_id += 1
      
      
      panel1.SetSizer(grid1)
      vbox.Add(panel1, 0, BOTTOM | TOP , 9) 
      
      # panel2

      panel2   = Panel(panel, -1)
      hbox2    = BoxSizer(HORIZONTAL)
      sizer21  = StaticBoxSizer(StaticBox(panel2, -1, self.LANG_DICT["DIFFICULTY"]), orient=VERTICAL)
      
      self.level_easy = RadioButton(panel2, -1, self.LANG_DICT["TRAINEE"], style=RB_GROUP)
      sizer21.Add(self.level_easy)
      if self.LEVEL == 1:
         self.level_easy.SetValue(True)
      
      self.level_bit_diff = RadioButton(panel2, -1, self.LANG_DICT["TRAINED"])
      sizer21.Add(self.level_bit_diff)
      if self.LEVEL == 2:
         self.level_bit_diff.SetValue(True)
      
      self.level_diff = RadioButton(panel2, -1, self.LANG_DICT["EXPERT"])
      sizer21.Add(self.level_diff)
      if self.LEVEL == 3:
         self.level_diff.SetValue(True)
      
      hbox2.Add(sizer21, 1, RIGHT, 5)
      
      sizer22 = StaticBoxSizer(StaticBox(panel2, -1, self.LANG_DICT["FONT_SIZE"]), orient=VERTICAL)
      self.large_font = RadioButton(panel2, -1, self.LANG_DICT["LARGE_FONT"], style=RB_GROUP)
      sizer22.Add(self.large_font)
      if self.FONT_SIZE == 18:
         self.large_font.SetValue(True)
      
      self.small_font = RadioButton(panel2, -1, self.LANG_DICT["SMALL_FONT"])
      sizer22.Add(self.small_font)
      if self.FONT_SIZE == 14:
         self.small_font.SetValue(True)
      
      hbox2.Add(sizer22, 1)

      panel2.SetSizer(hbox2)
      vbox.Add(panel2, 0, BOTTOM, 9)

      # panel5

      panel5 = Panel(panel, -1)
      sizer5 = BoxSizer(HORIZONTAL)
      sizer5.Add((self.FONT_SIZE * 2, -1), 1, EXPAND | ALIGN_CENTER)
      sizer5.Add(Button(panel5, 998, self.LANG_DICT["APPLY"]))
      sizer5.Add(Button(panel5, 997, self.LANG_DICT["EXIT"]))
      EVT_BUTTON(self, 998, self.apply_config)
      EVT_BUTTON(self, 997, self.close_config)

      panel5.SetSizer(sizer5)
      vbox.Add(panel5, 1, BOTTOM, 9)

      vbox_top.Add(vbox, 1, LEFT, 5)
      panel.SetSizer(vbox_top)
      
      
   def close_config(self, event):
      try:
         self.config_frame.Close()
      except:
         pass
     
   
   def apply_config(self, event):
      self.SCOPE = self.scope_dict[self.scope_combo.GetStringSelection()]
      
      level1 = self.level_easy.GetValue()
      level2 = self.level_bit_diff.GetValue()
      level3 = self.level_diff.GetValue()
      
      if level1 == True:
         self.LEVEL = 1
      elif level2 == True:
         self.LEVEL = 2
      elif level3 == True:
         self.LEVEL = 3
         
      
      font1 = self.small_font.GetValue()
      font2 = self.large_font.GetValue()
      
      if font1 == True:
         self.FONT_SIZE = 14
      elif font2 == True:
         self.FONT_SIZE = 18
         
      self.save_config() 
      self.message("Configuration saved")
      self.SetFocus()
      
   
   def save_config(self):
      
      file = open(self.CONFIG, "w")
      
      file.write("SCOPE=" + self.SCOPE + "\n")
      file.write("FONT=" + str(self.FONT_SIZE) + "\n") 
      file.write("LEVEL=" + str(self.LEVEL) + "\n")
      
      file.close()
      
      
   def read_config(self):
      try:
         file = open(self.CONFIG, "r")
         
         for line in file.readlines():
            if line.startswith("SCOPE"):
               self.SCOPE = strip(line.partition("=")[2])
            elif line.startswith("FONT"):
               self.FONT_SIZE = int(strip(line.partition("=")[2]))
            elif line.startswith("LEVEL"):
               self.LEVEL = int(strip(line.partition("=")[2]))
               
         file.close()
      except:
         self.save_config()
         #self.message("config file does not exists")
      
   def message(self, message):
      dlg = MessageDialog(self, message, self.LANG_DICT["INFORMATION"], OK | ICON_INFORMATION)
      dlg.SetFont(self.DEFAULT_FONT)
      dlg.ShowModal()
      dlg.Destroy()
 
      
if __name__ == "__main__":
   LANG_DICT = {
         "NAME"		   :u"Hangman-tamil",
         "EXIT"		   :u"Exit",
         "CONFIGURE"	   :u"Configure",
         "ABOUT"	      :u"About",
         "HELP"		   :u"Help",
         "NEW_WORD"	   :u"New word",
         "CATEGORY"	   :u"Category",
         "DIFFICULTY"   :u"Difficulty",
         "TRAINEE"	   :u"Trainee",
         "TRAINED"	   :u"Trained",
         "EXPERT"	      :u"Expert",
         "FONT_SIZE"	   :u"Font size",
         "LARGE_FONT"   :u"Large font",
         "SMALL_FONT"   :u"Small font",
         "APPLY"	      :u"Apply",
         "OK_TO_CLOSE"	:u"Confirm close",
         "GAME"		   :u"Game",
         "INTRODUCTION"	:u"Introduction",
         "INFORMATION"	:u"Information",
         "YOU_WON"	   :u"You Won!",
         "YOU_LOST"	   :u"You Lost!",
         "RESULTS"	   :u"Results",
	      "TRIES_LEFT"	:u"Tries Left",
	      "WORD_LIST_NOT_FOUND"	:u"Word list not found"
   }

   app = wxPySimpleApp(0)
   #frame = Config(None, -1, "")
   frame = Config(LANG_DICT,"lists","hangman.conf" )
   app.SetTopWindow(frame)
   frame.Show()
   app.MainLoop()

