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

'''
Created on Dec 21, 2009

@author: nayanajith
'''
from 	   string import strip
import   wx, re, random, sys, os


class Hangman(wx.Frame):
   font 	 = ""
   level 	 = ""
   
   LEVEL 	 = 1
   SCOPE 	 = ""
   TITLE_SCOPE = ""
   CONFIG 	 = "hangman.conf"
   DATA_DIR  = "data"
   IMG_DIR 	 = "img"
   FONT_SIZE = 14
   DEBUG 	 = 1
   NO_OF_CHANSES = 15
   #LANGUAGE = "TAMIL" 
   LANGUAGE = "SINHALA"

    
   def __init__(self, *args, **kwds):
      kwds["style"] = wx.DEFAULT_FRAME_STYLE
      wx.Frame.__init__(self, *args, **kwds)
      if self.LANGUAGE == "TAMIL":
         '''
         Character Lists vowels, consonents, vowel diacritics...etc Tamil
         '''
         self.VOWELS 		 = (u"அ", u"ஆ", u"இ", u"ஈ", u"உ", u"ஊ", u"எ", u"ஏ", u"ஐ",
										u"ஒ", u"ஓ", u"ஔ")
         self.CONSONENTS 	 = (u"க", u"ங", u"ச", u"ஞ", u"ட", u"ண", u"த", u"ந", u"ப",
										u"ம", u"ய", u"ர", u"ல", u"வ", u"ழ", u"ள", u"ற", u"ன",
										u"ஶ", u"ஜ", u"ஷ", u"ஸ", u"ஹ", u"க", u"ஷ")
         self.VOWEL_DIACRITICS 	 = (u"்", u"ா", u"ி", u"ீ", u"ு", u"ூ",
												u"ெ", u"ே", u"ை", u"ொ", u"ோ", u"ௌ")
         self.VOWEL_DIACRITICS_2 = ("")
         self.VOWEL_DIACRITICS_3 = ("")

         '''
         Language dictionary
         '''
         self.LANG_DICT = {
         "NAME"		   :u"Hangman-tamil",
         "EXIT"		   :u"Exit",
         "CONFIGURE"	   :u"Configure",
         "ABOUT"	      :u"About",
         "HELP"		   :u"Help",
         "NEW_WORD"	   :u" New word ",
         "CATEGORY"	   :u'Category: ',
         "DIFFICULTY"   :u'Difficulty',
         "TRAINEE"	   :u'Trainee',
         "TRAINED"	   :u'Trained',
         "EXPERT"	      :u'Expert',
         "FONT_SIZE"	   :u'Font size',
         "LARGE_FONT"   :u'Large font',
         "SMALL_FONT"   :u'Small font',
         "APPLY"	      :u' Apply ',
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

      elif self.LANGUAGE == "SINHALA":
         '''
         Character Lists vowels, consonents, vowel diacritics...etc.  Sinhala 
         '''
         self.VOWELS 		 = (u"අ", u"ආ", u"ඇ", u"ඈ", u"ඉ", u"ඊ", u"උ", u"ඌ", u"ඍ",
								u"ඎ", u"එ", u"ඒ", u"ඓ", u"ඔ", u"ඕ", u"ඖ", u"අං ", u"අඃ")
         self.CONSONENTS 	 = (u"ක", u"ඛ", u"ග", u"ඝ", u"ඞ", u"ඟ", u"ච", u"ඡ",
										u"ජ", u"ඣ", u"ඤ", u"ඥ", u"ට", u"ඨ", u"ඩ", u"ඪ",
										u"ණ", u"ඬ", u"ත", u"ථ", u"ද", u"ධ", u"න", u"ඳ",
										u"ප", u"ඵ", u"බ", u"භ", u"ම", u"ඹ", u"ය", u"ර",
										u"ල", u"ව", u"ශ", u"ෂ", u"ස", u"හ", u"ළ", u"ෆ")
         self.VOWEL_DIACRITICS = (u"්", u"ා", u"ැ", u"ෑ", u"ි", u"ී", u"ු",
											u"ූ", u"ෙ", u"ේ", u"ො", u"ෝ",
											u"ෞ", u"ෟ", u"ෘ", u"ෛ", u"ං", u"ඃ")
         self.VOWEL_DIACRITICS_2 = (u"්‍ර", u"්‍ය")
         self.VOWEL_DIACRITICS_3 = (u"ං", u"ඃ")

         '''
         Language dictionary
         '''
         self.LANG_DICT = {
         "NAME"         :u"වචන හරඹ",
         "EXIT"         :u"හමාර කරන්න",
         "CONFIGURE"    :u"අභිරුවය",
         "ABOUT"        :u"වචන හරඹ ගැන",
         "HELP"         :u"උදවු",
         "NEW_WORD"     :u"අලුත් වචනයක්",
         "CATEGORY"     :u'විෂයපථය: ',
         "DIFFICULTY"   :u'අපහසු තරම',
         "TRAINEE"      :u'නවක',
         "TRAINED"      :u'පුරුදු',
         "EXPERT"       :u'ප්‍රවීණ',
         "FONT_SIZE"    :u'අකුරු',
         "LARGE_FONT"   :u'ලොකු අකුරු',
         "SMALL_FONT"   :u'පොඩි අකුරු',
         "APPLY"        :u'යොදන්න',
         "OK_TO_CLOSE"  :u"සමුගැනීමට අවසරද",
         "GAME"         :u"ක්‍රීඩාව",
         "INTRODUCTION" :u"හැදින්වීම",
         "INFORMATION"  :u"තොරතුරු",
         "YOU_WON"      :u"ඔබ දිනුම්",
         "YOU_LOOSE"    :u"ඔබ් පරාදයි",
         "RESULTS"      :u"තරග ප්‍රතිඵල",
	      "TRIES_LEFT"	:u"තව වාර",
	      "WORD_LIST_NOT_FOUND"	:u"වචන ගොනුවක් සොයාගත නොහැක"
         }

      self.DEFAULT_FONT 	 = wx.Font(self.FONT_SIZE, wx.TELETYPE, wx.NORMAL, wx.NORMAL, 0, "Iskoola Pota")
      #self.DEFAULT_FONT = wx.Font(self.FONT_SIZE, wx.TELETYPE, wx.NORMAL, wx.NORMAL, 0, "LKLUG")
      self.SetFont(self.DEFAULT_FONT)
      self.SetSize(size=(self.FONT_SIZE * 63, 585))
      self.vowel_button_list 		 = []
      self.consonent_button_list = []
      self.init_keyboard()
      self.NAME 				 = self.LANG_DICT["NAME"]
      self.SetTitle(self.NAME + " [" + self.TITLE_SCOPE + "]")
      
      '''
      Adding menubar
      '''
      self.menuBar	 = wx.MenuBar()
      menu 				 = wx.Menu()
      m_exit 			 = menu.Append(wx.ID_EXIT, self.LANG_DICT["EXIT"],
											"Close window and exit program.")
      m_config 		 = menu.Append(1009, self.LANG_DICT["CONFIGURE"], "Preferences.")
      self.menuBar.Append(menu, "&File")
      self.Bind(wx.EVT_MENU, self.onClose, m_exit)
      self.Bind(wx.EVT_MENU, self.config_panel, m_config)
     
      menu 				 = wx.Menu()
      m_about 			 = menu.Append(wx.ID_ABOUT, self.LANG_DICT["ABOUT"],
											"Information about this program")
      self.menuBar.Append(menu, "&Help")
      self.Bind(wx.EVT_MENU, self.onAbout, m_about)
      self.SetMenuBar(self.menuBar)

   '''
   Generate keyboard according to the language and the difficulty level
   '''
   def init_keyboard(self):
      self.read_config()   #Reading and loading the configuration
      
          
      '''
      Calculate the lengths of the character lists
      ''' 
      self.vowels_length = len(self.VOWELS) 
      self.consonents_length = len(self.CONSONENTS)
      self.vowel_diacritics_2_length = len(self.VOWEL_DIACRITICS_2)
      self.vowel_diacritics_1_length = len(self.VOWEL_DIACRITICS)
      
      if self.LANGUAGE == "SINHALA":
         self.vowel_diacritics_length = self.vowel_diacritics_1_length + self.vowel_diacritics_2_length
      elif self.LANGUAGE == "TAMIL":
         self.vowel_diacritics_length = self.vowel_diacritics_1_length 


      self.CHALLENGE_LIST = []     #List of challenging words
      self.CHALLENGE_WORD = ""     #Current Challenging word
      self.FINISHED_LETTER = ""     #Final Letter to be included in textArea
     
      
      '''
      Buttons and GUI information
      '''
      button_width = self.FONT_SIZE + 28
      button_height = self.FONT_SIZE + 28
      buttons_per_line = 10
      initial_button_x = 100
      initial_button_y = 100
      starting_event_id = 0
      current_sign = 0
      
      self.vowel_button_list = self.gen_button_array(
         self.VOWELS, self.vowel_click,
         buttons_per_line,
         initial_button_x,
         initial_button_y,
         starting_event_id,
         button_width,
         button_height)    

      for sign in self.VOWELS:
         vd_button = self.vowel_button_list[current_sign]
         vd_button.SetLabel(sign)
         current_sign += 1
         
      buttons_per_line = 6
      initial_button_y = 210
      current_sign = 0
      starting_event_id = self.vowels_length
      self.consonent_button_list = self.gen_button_array(
         self.CONSONENTS,
         self.consonent_click,
         buttons_per_line,
         initial_button_x,
         initial_button_y,
         starting_event_id,
         button_width,
         button_height)    

      for sign in self.CONSONENTS:
         vd_button = self.consonent_button_list[current_sign]
         vd_button.SetLabel(sign)
         current_sign += 1
      '''
      Textarea for desplaying the word
      '''
      self.textArea = wx.TextCtrl(self,
			pos=(20, 20),
         size=(self.FONT_SIZE * 28, self.FONT_SIZE + 29),
         style=wx.TE_CENTER | wx.TE_READONLY)

      self.textArea.SetFont(wx.Font(self.FONT_SIZE + 5, wx.TELETYPE, wx.NORMAL, wx.BOLD, 0, "Iskoola Pota"))
      
      '''
      Image of the hanging man
      '''
      self.BMP = wx.Bitmap(self.IMG_DIR + "/0.png", wx.BITMAP_TYPE_ANY)
      self.bitmap_image = wx.StaticBitmap(self, -1, self.BMP, pos=((self.FONT_SIZE * 28) + 130, 50))
      
      
      '''
      Labels for '<' mark and 'Enter'
      '''
      if self.LEVEL == 3:
         wx.StaticText(self, label="<", pos=((self.FONT_SIZE * 28) + 35, 32))

         '''
         Enter the Complete letter to the text area
         '''
         self.finish_button = wx.Button(self,
            1000,
            label=u"",
            pos=((self.FONT_SIZE * 28) + 65, 20),
            size=(self.FONT_SIZE + 47, self.FONT_SIZE + 35))

         self.finish_button.Disable()
         wx.EVT_BUTTON(self, 1000, self.finish_letter)
         
      wx.StaticText(self, label=self.LANG_DICT["TRIES_LEFT"], pos=((self.FONT_SIZE * 28) + 255, 18))
      self.chance_label = wx.StaticText(self, label="1", pos=((self.FONT_SIZE * 28) + 285, 50))
      
      

      '''
      Cheat button
      '''
      if self.LEVEL == 1 :
         self.cheat_button = wx.Button(self,
            999,
            label=self.LANG_DICT["HELP"],
            pos=((self.FONT_SIZE * 28) + 65, 20),
            size=(self.FONT_SIZE + 47, self.FONT_SIZE + 35))

         wx.EVT_BUTTON(self, 999, self.cheat_game)
      
      '''
      Game restart button
      '''
      self.restart_button = wx.Button(self,
         1001,
         label=self.LANG_DICT["NEW_WORD"],
         pos=((self.FONT_SIZE * 10) + 300, 500))
      wx.EVT_BUTTON(self, 1001, self.restart_game)
      
      '''
      Game close button
      '''
      self.restart_button = wx.Button(self,
         1002,
         label=self.LANG_DICT["EXIT"],
         pos=((self.FONT_SIZE * 10) + 100, 500))

      wx.EVT_BUTTON(self, 1002, self.onClose)
      
      self.init_game(True)
      
   '''
   Initialize game
   '''
   def init_game(self, read_file):
      self.read_config() #Reading and loading the configuration
      if self.SCOPE == "":
         try:
            self.SCOPE = os.listdir(self.DATA_DIR)[1]
         except:
            dlg = wx.MessageDialog(self,
                                   self.LANG_DICT["WORD_LIST_NOT_FOUND"],
                                   self.LANG_DICT["NAME"] + " : " + self.LANG_DICT["WORD_LIST_NOT_FOUND"] + "!",
                                   wx.OK | wx.ICON_ERROR)
            dlg.SetFont(self.DEFAULT_FONT)
            result = dlg.ShowModal()
            dlg.Destroy()
            sys.exit(1)
                                   
      #Read list of words from a file
      first_word = True
      if read_file == True:
         file = open(self.DATA_DIR + "/" + self.SCOPE)
         for line in file.readlines():
            word = line.decode("UTF-8").rstrip('\n')
            if first_word == True:
               self.TITLE_SCOPE = word
               first_word = False
            else:
               self.CHALLENGE_LIST.append(word)
         file.close()
         
      rand_num = random.randint(0, (len(self.CHALLENGE_LIST) - 1))
      
      self.CHALLENGE_WORD = self.CHALLENGE_LIST[rand_num]
      self.chances = 0
      self.check_letter(u"", True, True)
      
      '''
      Enable all buttons
      ''' 
      for btn in self.vowel_button_list:
         btn.Enable()
         
         
      for btn in self.consonent_button_list:
         btn.Enable()
         
   def dbg(self, msg, bullet):
      if self.DEBUG == 1:
         print "[" + bullet + "] " + msg.encode("utf-8")
   '''
   Configuration panel
   ''' 
   scope_dict = {}
   def config_panel(self, event):
      self.config_frame = wx.Frame(self)
      self.config_frame.SetFont(self.DEFAULT_FONT)
      self.config_frame.SetSize(size=(self.FONT_SIZE * 24, 250))
      self.config_frame.SetTitle(self.LANG_DICT["CONFIGURE"])
      
      vbox_top = wx.BoxSizer(wx.VERTICAL)
      panel = wx.Panel(self.config_frame, -1)
      vbox = wx.BoxSizer(wx.VERTICAL)
      
      panel1 = wx.Panel(panel, -1)
      grid1 = wx.GridSizer(2, 2)
      grid1.Add(wx.StaticText(panel1,
         - 1,
         self.LANG_DICT["CATEGORY"] + " :",
         (5, 5)),
         0,
         wx.ALIGN_CENTER_VERTICAL)
      
      self.scope_combo = wx.ComboBox(panel1, -1, size=(150, -1)) 
      for filename in os.listdir(self.DATA_DIR):
         file = open(self.DATA_DIR + "/" + filename)
         scope = file.readline().decode("UTF-8").rstrip('\n')
         self.scope_dict[scope] = filename
         self.scope_combo.Append(scope)
      grid1.Add(self.scope_combo)
      
      item_id = 0 
      for item in self.scope_combo.GetStrings():
         if item == self.TITLE_SCOPE:
            self.scope_combo.SetSelection(item_id)
         item_id += 1
      
      
      panel1.SetSizer(grid1)
      vbox.Add(panel1, 0, wx.BOTTOM | wx.TOP , 9) 
      
      # panel2

      panel2 = wx.Panel(panel, -1)
      hbox2 = wx.BoxSizer(wx.HORIZONTAL)

      sizer21 = wx.StaticBoxSizer(wx.StaticBox(panel2, -1, self.LANG_DICT["DIFFICULTY"]), orient=wx.VERTICAL)
      
      self.level_easy = wx.RadioButton(panel2, -1, self.LANG_DICT["TRAINEE"], style=wx.RB_GROUP)
      sizer21.Add(self.level_easy)
      if self.LEVEL == 1:
         self.level_easy.SetValue(True)
      
      self.level_bit_diff = wx.RadioButton(panel2, -1, self.LANG_DICT["TRAINED"])
      sizer21.Add(self.level_bit_diff)
      if self.LEVEL == 2:
         self.level_bit_diff.SetValue(True)
      
      self.level_diff = wx.RadioButton(panel2, -1, self.LANG_DICT["EXPERT"])
      sizer21.Add(self.level_diff)
      if self.LEVEL == 3:
         self.level_diff.SetValue(True)
      
      hbox2.Add(sizer21, 1, wx.RIGHT, 5)
      
      sizer22 = wx.StaticBoxSizer(wx.StaticBox(panel2, -1, self.LANG_DICT["FONT_SIZE"]), orient=wx.VERTICAL)
      self.large_font = wx.RadioButton(panel2, -1, self.LANG_DICT["LARGE_FONT"], style=wx.RB_GROUP)
      sizer22.Add(self.large_font)
      if self.FONT_SIZE == 18:
         self.large_font.SetValue(True)
      
      self.small_font = wx.RadioButton(panel2, -1, self.LANG_DICT["SMALL_FONT"])
      sizer22.Add(self.small_font)
      if self.FONT_SIZE == 14:
         self.small_font.SetValue(True)
      
      hbox2.Add(sizer22, 1)

      panel2.SetSizer(hbox2)
      vbox.Add(panel2, 0, wx.BOTTOM, 9)

      # panel5

      panel5 = wx.Panel(panel, -1)
      sizer5 = wx.BoxSizer(wx.HORIZONTAL)
      sizer5.Add((self.FONT_SIZE * 2, -1), 1, wx.EXPAND | wx.ALIGN_CENTER)
      sizer5.Add(wx.Button(panel5, 998, self.LANG_DICT["APPLY"]))
      sizer5.Add(wx.Button(panel5, 997, self.LANG_DICT["EXIT"]))
      wx.EVT_BUTTON(self, 998, self.apply_config)
      wx.EVT_BUTTON(self, 997, self.close_config)

      panel5.SetSizer(sizer5)
      vbox.Add(panel5, 1, wx.BOTTOM, 9)

      vbox_top.Add(vbox, 1, wx.LEFT, 5)
      panel.SetSizer(vbox_top)
      
      self.config_frame.Show()
      
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
      self.config_frame.SetFocus()
      
   
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
      
      
   '''
   Restart game event handler
   '''
   def restart_game(self, event):
      self.init_game(False)
      self.cheat_count = 0
      
   '''
   On close event handler: Prompt when closing the window
   '''
   def onClose(self, event):
      dlg = wx.MessageDialog(self,
         self.NAME + self.LANG_DICT["OK_TO_CLOSE"] + "?",
         self.LANG_DICT["OK_TO_CLOSE"],
         wx.OK | wx.CANCEL | wx.ICON_EXCLAMATION)

      dlg.SetFont(self.DEFAULT_FONT)
      result = dlg.ShowModal()
      dlg.Destroy()
      if result == wx.ID_OK:
         sys.exit(1)
   '''
   On About event handler: display about information
   '''
   def onAbout(self, event):
      dlg = wx.MessageDialog(self,
         self.NAME + u"\n\n\n " + self.LANG_DICT["GAME"] + "\n ",
         self.LANG_DICT["INTRODUCTION"],
         wx.OK | wx.ICON_INFORMATION)
      
      dlg.SetFont(self.DEFAULT_FONT)
      dlg.ShowModal()
      dlg.Destroy()

   def message(self, message):
      dlg = wx.MessageDialog(self, message, self.LANG_DICT["INFORMATION"], wx.OK | wx.ICON_INFORMATION)
      dlg.SetFont(self.DEFAULT_FONT)
      dlg.ShowModal()
      dlg.Destroy()
   

   '''
   Generate an array of button for the list of labels given and assign events to each button
   ''' 
   def gen_button_array(self,
                        label_list,
                        onclick_function,
                        buttons_per_line,
                        initial_button_x,
                        initial_button_y,
                        starting_event_id,
                        button_width, button_height):    
      
      current_button_x = initial_button_x 
      current_button_y = initial_button_y
      current_sign = 0
      event_id = starting_event_id
      button_list = []
      
      for sign in label_list:
         vd_button = wx.Button(self,
            event_id,
            label=sign,
            pos=(current_button_x - 60 - 15, current_button_y),
            size=(button_width, button_height))
         
         button_list.append(vd_button)
         wx.EVT_BUTTON(self, event_id, onclick_function)
         current_button_x += button_width
         current_sign += 1
         event_id += 1
         if  current_sign % buttons_per_line == 0:
            current_button_y += button_height
            current_button_x = initial_button_x
      return button_list 
   
   '''
   Setting the suitable image for the step
   ''' 
   def set_image(self, img_no):
      self.BITMAP = wx.Bitmap(self.IMG_DIR + "/" + str(img_no) + ".png", wx.BITMAP_TYPE_ANY)
      self.bitmap_image.SetBitmap(self.BITMAP)
      self.bitmap_image.Refresh()
      
   '''
   return challenge word as a list divided in to complete letters
   ''' 
   def challenge_word(self, word):
      letter = ""
      letter_list = []
      #print u"ට්‍රෝ" "‍" u"්" ‍
      for sign in word:
         #if sign == u"‍" or re.search(sign, self.VOWEL_DIACRITICS) or (re.search(u"‍" , letter)  and (sign == u'ර' or sign == u'ය')):
         #EDITING
         is_sign = False
         if sign in self.VOWEL_DIACRITICS:
            is_sign = True

         if sign == u"‍" or is_sign or (re.search(u"‍" , letter)  and (sign == u'ර' or sign == u'ය')):
            letter += sign
            #self.dbg(letter, "letter1")
         else:
            if letter != "" and letter != " ":
               letter_list.append(letter)
               #self.dbg(letter, "letter1")
            letter = sign
      
      letter_list.append(letter)
      #self.dbg(letter, "letter1")
      return letter_list
   
   '''
   Cheat function ;
   Auto fill some letters for you
   ''' 
   cheat_count = 0
   def cheat_game(self, event):
      letter_list = self.challenge_word(self.CHALLENGE_WORD)
      rand_num = random.randint(0, (len(letter_list) - 1))
      letter = letter_list[rand_num]
      if letter != "":
         self.cheat_count += 1
         self.check_letter(letter_list[rand_num], False, True)
      
   
   '''   
   Check final letter entered and print it in the text area
   '''
   correct_letters = []  # To store correct letters  entered by user
   wrong_letters = []  # To store incorrect letters
   chances = 0   # To count chances
   def check_letter(self, letter, reset, cheat):
      '''
      Generate complete letter list for the CHALLENGE_WORD
      '''
      letter_list = self.challenge_word(self.CHALLENGE_WORD)
      correct = False #If the letter entered is correct this will turn True
      #for let in letter_list:
      #   self.dbg(let.encode("utf-8"), "check_letter")#DEBUG INFO
         
      if reset == True or self.correct_letters == []: #Reset the correct_letters list
         self.correct_letters = []
         for let in letter_list:
            self.correct_letters.append("*") #Fill the correct letter list with '-'
            
      if cheat == True:
         pos = 0
         for let in letter_list:
            if re.match(let, letter):
               self.correct_letters[pos] = let
               correct = True
            else:
               self.wrong_letters.append(let)
            pos += 1
         
            
      if letter != "" and cheat == False: #Check whether the letter is available
         pos = 0
         self.textArea.SetValue("") #Clea textArea
         
      
         if self.LEVEL == 1 or self.LEVEL == 2:
            '''
            For the biginners level all the combinations of the latter is filled
            ''' 
            if self.LANGUAGE == "SINHALA":
               tmp_list = ("", self.VOWEL_DIACRITICS_2[0], self.VOWEL_DIACRITICS_2[1])
               tmp_list2 = ("", u"ං", u"ඃ")

               for sign in tmp_list:
                  letter_t = letter + sign 
                  for sign in self.VOWEL_DIACRITICS:
                     letter_s = letter_t + sign 
                     #self.dbg(letter_s, "check_letter")#DEBUG INFO
                     for sign in tmp_list2:
                        letter_r = letter_s + sign 
                        pos = 0
                        for let in letter_list:
                           if re.match(let, letter_r):
                              self.correct_letters[pos] = let
                              correct = True
                           else:
                              self.wrong_letters.append(let)
                           pos += 1
            elif self.LANGUAGE == "TAMIL":
               for sign in self.VOWEL_DIACRITICS:
                  letter_r = letter + sign 
                  #self.dbg(letter_r, "check_letter")#DEBUG INFO
                  pos = 0
                  for let in letter_list:
                     if re.match(let, letter_r):
                        self.correct_letters[pos] = let
                        correct = True
                     else:
                        self.wrong_letters.append(let)
                     pos += 1
				
         else:
            '''
            For experts complete letter should be entered
            ''' 
            for let in letter_list:
               if re.match(let, letter):
                  self.correct_letters[pos] = let
                  correct = True
               else:
                  self.wrong_letters.append(let)
               pos += 1
      
      if correct == False or not letter:
         self.chances += 1 #If the letter is incorrect reduce a chance
         self.chance_label.SetLabel(str(self.NO_OF_CHANSES - self.chances))
         self.set_image(self.chances)
            
      '''
      Generate complete word
      '''
      word = "" 
      for let in self.correct_letters:
         if let != "":
            word += let
            
      '''
      Display  game status
      '''
      if word == self.CHALLENGE_WORD:
         self.textArea.SetValue(word)
         dlg = wx.MessageDialog(self,
            self.LANG_DICT["HELP"] + ":" + str(self.cheat_count) + u"\n\n" + self.LANG_DICT["YOU_WON"] + "!",
            self.LANG_DICT["RESULTS"],
            wx.OK | wx.ICON_INFORMATION)

         dlg.SetFont(self.DEFAULT_FONT)
         dlg.ShowModal()
         dlg.Destroy()
      
      if self.NO_OF_CHANSES == self.chances:
         word = self.CHALLENGE_WORD
         #self.textArea.SetValue(word)
         dlg = wx.MessageDialog(self,
            self.LANG_DICT["YOU_LOST"] + "!",
            self.LANG_DICT["RESULTS"],
            wx.OK | wx.ICON_INFORMATION)

         dlg.SetFont(self.DEFAULT_FONT)
         dlg.ShowModal()
         dlg.Destroy()
         
      '''
      Display the word in textarea
      '''
      self.textArea.SetValue(word)
      return correct
      
         
   '''
   If the letter is completed it will included in textarea
   ''' 
   def finish_letter(self, event):
      self.check_letter(self.FINISHED_LETTER, False, False)
      self.finish_button.Disable()
      
      
   '''
   Set letter in left button to be etered to the textarea
   ''' 
   def set_letter(self, letter):
      is_sign = False
      if letter in self.VOWEL_DIACRITICS:
         is_sign = True


      #if is_sign or re.match(letter, self.VOWEL_DIACRITICS_2[0]) or re.match(letter, self.VOWEL_DIACRITICS_2[1]):
      if is_sign :
         self.FINISHED_LETTER += letter
      else:
         self.FINISHED_LETTER = letter
         
      self.finish_button.SetLabel(self.FINISHED_LETTER)
      self.finish_button.Enable()
      
   '''
   When a vowel is clicked this function will be executed
   ''' 
   def vowel_click(self, event):
      event_id = event.GetId()
      #self.set_letter(self.VOWELS[event_id])
      self.check_letter(self.VOWELS[event_id], False, False)
      for btn in self.vowel_button_list:
         if btn.GetId() == event_id:
            btn.Disable()
         
   '''
   when a consonent is clicked this function will be executed
   '''
   current_consonent = 0
   def consonent_click(self, event):
      event_id = event.GetId()
      self.current_consonent = event_id
      if self.LEVEL == 1 or self.LEVEL == 2:
         self.check_letter(self.CONSONENTS[event_id - (self.vowels_length)], False, False)
         for btn in self.consonent_button_list:
            if btn.GetId() == self.current_consonent:
               btn.Disable()
      else:
         self.set_letter(self.CONSONENTS[event_id - (self.vowels_length)])
         self.gen_vowel_dicretics(self.CONSONENTS[event_id - (self.vowels_length)])
      
   def vowel_dicretic_click(self, event):
      event_id = event.GetId()
      vowel_dicretic_id = event_id - (self.vowels_length + self.consonents_length)
      if  vowel_dicretic_id >= self.vowel_diacritics_2_length:
         vowel_dicretic_id -= self.vowel_diacritics_2_length
         #self.check_letter(self.vowel_dicretics_list[vowel_dicretic_id])
         self.set_letter(self.vowel_dicretics_list[vowel_dicretic_id])
         btn_id = 0
         
         if self.LANGUAGE == "SINHALA":
            for btn in self.vowel_dicretics_button_list:
           #exception in sinhala 
               if not btn_id >= (len(self.vowel_dicretics_button_list) - 2):
                  btn.Disable() #disable other than of last two buttons 
               btn_id += 1
           #exception in sinhala 
            for btn in self.vowel_dicretics_button_2_list:
               btn.Disable()
               
         elif self.LANGUAGE == "TAMIL":
            for btn in self.vowel_dicretics_button_list:
               btn.Disable() 
               btn_id += 1
      else:
         #self.check_letter(self.vowel_dicretics_2_list[vowel_dicretic_id])
         self.set_letter(self.vowel_dicretics_2_list[vowel_dicretic_id])
         for btn in self.vowel_dicretics_button_2_list:
            btn.Disable()
      
      
      

   '''
   To generate the list of vowel dicretics buttons
   '''
   buttons_added = False
   vowel_dicretics_button_list = []
   vowel_dicretics_2_button_list = []
   vowel_dicretics_list = []
   vowel_dicretics_2_list = []
   def gen_vowel_dicretics(self, consonent):
      button_width = self.FONT_SIZE + 42
      button_height = self.FONT_SIZE + 28
      buttons_per_line = 5
      initial_button_x = self.FONT_SIZE * 28 
      initial_button_y = 210
      starting_event_id = (self.vowels_length + self.consonents_length)
      current_sign = 0

      """
      For Sinhala only
      """
      if self.LANGUAGE == "SINHALA":
         if self.buttons_added == False:
            self.vowel_dicretics_button_2_list = self.gen_button_array(self.
               VOWEL_DIACRITICS_2,
               self.vowel_dicretic_click,
               buttons_per_line,
               initial_button_x,
               initial_button_y,
               starting_event_id,
               button_width,
               button_height)    

         for sign in self.VOWEL_DIACRITICS_2:
            self.vowel_dicretics_2_list.append(sign)
            vd_button = self.vowel_dicretics_button_2_list[current_sign]
            vd_button.SetLabel(consonent + sign)
            vd_button.Enable()
            current_sign += 1
         
         initial_button_x = self.FONT_SIZE * 28
         initial_button_y = 270
         current_sign = 0
         starting_event_id = (self.vowels_length + self.consonents_length) + 2
      
      if self.buttons_added == False:
         self.vowel_dicretics_button_list = self.gen_button_array(self.
            VOWEL_DIACRITICS ,
            self.vowel_dicretic_click ,
            buttons_per_line,
            initial_button_x,
            initial_button_y,
            starting_event_id,
            button_width,
            button_height)    

      for sign in self.VOWEL_DIACRITICS:
         self.vowel_dicretics_list.append(sign)
         vd_button = self.vowel_dicretics_button_list[current_sign]
         vd_button.SetLabel(consonent + sign)
         vd_button.Enable()
         current_sign += 1
         
      self.buttons_added = True
      
     

if __name__ == "__main__":
   app = wx.PySimpleApp(0)
   wx.InitAllImageHandlers()
   frame_2 = Hangman(None, -1, "")
   app.SetTopWindow(frame_2)
   frame_2.Show()
   app.MainLoop()

