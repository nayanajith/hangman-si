# -*- coding: utf-8 -*-
'''
Created on Dec 21, 2009

@author: nayanajith
අආඇඈඉඊඋඌඍඎඑඒඓඔඕඖඅංඅඃකඛගඝඞඟචඡජඣඤඥටඨඩඪණඬතථදධනඳපඵබභමඹයරලවශෂසහළෆ
'''
import  wx

class keyboard_si(wx.Frame):
 
   def __init__(self, *args, **kwds):
      kwds["style"] = wx.DEFAULT_FRAME_STYLE
      wx.Frame.__init__(self, *args, **kwds)
      self.SetFont(wx.Font(16, wx.TELETYPE, wx.NORMAL, wx.NORMAL, 0, "Iskoola Pota"))
      self.SetSize(size=(900, 500))
      self.init_keyboard()


   def init_keyboard(self):
      self.VOWELS = (u"අ", u"ආ", u"ඇ", u"ඈ", u"ඉ", u"ඊ", u"උ", u"ඌ", u"ඍ", u"ඎ", u"එ", u"ඒ", u"ඓ", u"ඔ", u"ඕ", u"ඖ", u"අං ", u"අඃ", u"ං", u"ඃ")
      self.CONSONENTS = u"කඛගඝඞඟචඡජඣඤඥටඨඩඪණඬතථදධනඳපඵබභමඹයරලවශෂසහළෆ"
      self.VOWEL_DIACRITICS = u"්ාැෑිීුූෙේොෝෞෟෘෛංඃ"
      self.VOWEL_DIACRITICS_2 = (u"්‍ර", u"්‍ය")

      self.CHALLENGE_WORD = "ආයු‍බෝවන්"
      
      self.vowels_length = len(self.VOWELS) 
      self.consonents_length = len(self.CONSONENTS)
      self.vowel_diacritics_2_length = len(self.VOWEL_DIACRITICS_2)
      self.vowel_diacritics_1_length = len(self.VOWEL_DIACRITICS)
      self.vowel_diacritics_length = self.vowel_diacritics_1_length + self.vowel_diacritics_2_length
      
      button_width = 46
      button_height = 46
      
      buttons_per_line = 10

      initial_button_x = 100
      initial_button_y = 100

      
      starting_event_id = 0
      current_sign = 0
      
      vowel_button_list = self.gen_button_array(self,self.VOWELS, self.vowel_click , buttons_per_line, initial_button_x, initial_button_y, starting_event_id, button_width, button_height)    
      for sign in self.VOWELS:
         vd_button = vowel_button_list[current_sign]
         vd_button.SetLabel(sign)
         current_sign += 1
         
      initial_button_y = 210
      current_sign = 0
      starting_event_id = self.vowels_length
      consonents_button_list = self.gen_button_array(self,self.CONSONENTS, self.consonent_click , buttons_per_line, initial_button_x, initial_button_y, starting_event_id, button_width, button_height)    
      for sign in self.CONSONENTS:
         vd_button = consonents_button_list[current_sign]
         vd_button.SetLabel(sign)
         current_sign += 1
      
      self.textArea = wx.TextCtrl(self, pos=(20, 20), size=(600, 65), style=wx.TE_MULTILINE)
      self.textArea.Multiline = True
      self.textArea.WordWrap = True
      
   def gen_button_array(self, resizer, label_list, onclick_function, buttons_per_line, initial_button_x, initial_button_y, starting_event_id, button_width, button_height):    
      current_button_x = initial_button_x 
      current_button_y = initial_button_y
      current_sign = 0
      event_id = starting_event_id
      self.vowel_dicretics_2_button_list = []
      
      for sign in label_list:
         vd_button = wx.Button(resizer, event_id, label=sign, pos=(current_button_x - 60 - 15, current_button_y), size=(button_width, button_height))
         print event_id
         self.vowel_dicretics_2_button_list.append(vd_button)
         wx.EVT_BUTTON(self, event_id, onclick_function)
         current_button_x += button_width
         current_sign += 1
         event_id += 1
         if  current_sign % buttons_per_line == 0:
            current_button_y += button_height
            current_button_x = initial_button_x
      return self.vowel_dicretics_2_button_list 
   
   
   def vowel_click(self, event):
      event_id = event.GetId()
      self.textArea.AppendText(self.VOWELS[event_id])
         
   def consonent_click(self, event):
      event_id = event.GetId()
      print event_id
      self.textArea.AppendText(self.CONSONENTS[event_id - (self.vowels_length)])
      self.gen_vowel_dicretics(self.CONSONENTS[event_id - (self.vowels_length)])
      
   def vowel_dicretic_click(self, event):
      event_id = event.GetId()
      print event_id
      vowel_dicretic_id = event_id - (self.vowels_length + self.consonents_length)
      print   vowel_dicretic_id
      
      if  vowel_dicretic_id >= self.vowel_diacritics_2_length:
         vowel_dicretic_id -= self.vowel_diacritics_2_length
         self.textArea.AppendText(self.vowel_dicretics_list[vowel_dicretic_id])

         for btn in self.vowel_dicretics_button_list:
            btn.Disable()
         for btn in self.vowel_dicretics_button_2_list:
            btn.Disable()
      else:
         self.textArea.AppendText(self.vowel_dicretics_2_list[vowel_dicretic_id])
         for btn in self.vowel_dicretics_button_2_list:
            btn.Disable()
         
         
      

   buttons_added = False
   vowel_dicretics_button_list = []
   vowel_dicretics_2_button_list = []
   vowel_dicretics_list = []
   vowel_dicretics_2_list = []
   
   def gen_vowel_dicretics(self, consonent):
      button_width = 60
      button_height = 46
      buttons_per_line = 5
      initial_button_x = 600
      initial_button_y = 100
      starting_event_id = (self.vowels_length + self.consonents_length)
      current_sign = 0
      
      if self.buttons_added == False:
         self.vowel_dicretics_button_2_list = self.gen_button_array(self,self.VOWEL_DIACRITICS_2, self.vowel_dicretic_click , buttons_per_line, initial_button_x, initial_button_y, starting_event_id, button_width, button_height)    
      for sign in self.VOWEL_DIACRITICS_2:
         self.vowel_dicretics_2_list.append(sign)
         vd_button = self.vowel_dicretics_button_2_list[current_sign]
         vd_button.SetLabel(consonent + sign)
         vd_button.Enable()
         current_sign += 1
         
      initial_button_x = 600
      initial_button_y = 160
      current_sign = 0
      starting_event_id = (self.vowels_length + self.consonents_length) + 2
      
      if self.buttons_added == False:
         self.vowel_dicretics_button_list = self.gen_button_array(self,self.VOWEL_DIACRITICS , self.vowel_dicretic_click , buttons_per_line, initial_button_x, initial_button_y, starting_event_id, button_width, button_height)    
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
   frame_2 = keyboard_si(None, -1, "")
   app.SetTopWindow(frame_2)
   frame_2.Show()
   app.MainLoop()

