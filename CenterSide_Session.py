#!/usr/bin/python3

#####################################################################################
#
# CenterSide: a board game
# Written in PyQt5
# Created by Albert "Anferensis" Ong
#
#####################################################################################

import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
                            QVBoxLayout, QHBoxLayout, QGridLayout, \
                            QLabel, QPushButton, QMessageBox, QComboBox, QInputDialog


from CenterSide_StyleSheets import StyleSheets

#====================================================================================

class CenterSideSession(QWidget):
    """
    Creates a session of CenterSide given a CenterSideWindow. 
    A session covers the logic for the title screen and all other out of game options.
    """
    def __init__(self, mainwindow):
        super().__init__()
        
        self.mainwindow =       mainwindow
        self.stylesheets =      self.mainwindow.stylesheets
        
        self.language = mainwindow.language
        
        self.lang_dict = {}
        for num,lang in enumerate(("English","Español","Français",\
                                    "Deutsch","한글","中文","日本語")):
             self.lang_dict[lang] = num
             
        self.theme = mainwindow.theme
        self.theme_dict = {}
        for num,theme in enumerate(("Default", "Art Deco","Cherry Soda",\
                                    "Coffee", "Spring Green", "Victorian")):
             self.theme_dict[theme] = num
             
        self.title_text = QLabel("CenterSide",self)
        self.title_text.setAlignment(Qt.AlignHCenter)
        self.title_text.setStyleSheet(self.stylesheets.title_CSS)
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignHCenter)
        self.main_layout.setContentsMargins(0,40,0,55)
        self.main_layout.setSpacing(0)
        self.main_layout.addWidget(self.title_text)
        
        self.create_title_buttons()
        self.create_play_buttons()
        # ~ self.create_vsAI_buttons()
        # ~ self.create_options_buttons()
        
        
        
    def create_title_buttons(self):
        
        self.title_menu= []
        self.titlebuttons_layout = QVBoxLayout()
        self.titlebuttons_layout.setContentsMargins(0,0,0,0)
        self.titlebuttons_layout.setAlignment(Qt.AlignCenter)
        self.titlebuttons_layout.setSpacing(0)
        self.main_layout.addLayout(self.titlebuttons_layout)
        
        # ~ icon_play =     self.mainwindow.icon_play
        # ~ icon_options =  self.mainwindow.icon_options
        # ~ icon_shop =     self.mainwindow.icon_shop
        # ~ icon_quit =     self.mainwindow.icon_quit
        
        
        # ~ for icon, function in ((icon_play,     self.play_button),
                               # ~ (icon_options,  self.options_button),
                               # ~ (icon_shop,     self.shop_button),
                               # ~ (icon_quit,     self.quit_button)):
                                   
            # ~ button = QPushButton(self)
            # ~ button.setIcon(icon)
            # ~ button.setIconSize(QSize(150,80))
            # ~ button.clicked.connect(function)
            # ~ button.setStyleSheet(self.stylesheets.clear_background)
            
            # ~ self.title_menu.append(button)
            # ~ self.titlebuttons_layout.addWidget(button)
            
            
            
    def create_play_buttons(self):
        
        self.playmenu_layout = QVBoxLayout()
        self.playmenu_layout.setContentsMargins(0,0,0,0)
        self.playmenu_layout.setAlignment(Qt.AlignCenter)
        self.playmenu_layout.setSpacing(100)
        self.main_layout.addLayout(self.playmenu_layout)
        
        self.playoptions_layout = QGridLayout()
        self.playoptions_layout.setColumnStretch(1,0)
        self.playoptions_layout.setHorizontalSpacing(30)
        self.playoptions_layout.setVerticalSpacing(0)
        self.playmenu_layout.addLayout(self.playoptions_layout)
        
        # ~ icon_internet =  self.mainwindow.icon_internet
        # ~ icon_invite =    self.mainwindow.icon_invite
        # ~ icon_local =     self.mainwindow.icon_local
        # ~ icon_vsAI =      self.mainwindow.icon_vsAI
        # ~ icon_quit =      self.mainwindow.icon_quit
        
        # ~ self.play_menu = []
        # ~ for icon, function in ((icon_internet,   self.internet_button),
                               # ~ (icon_invite,     self.invite_button),
                               # ~ (icon_local,     self.local_button),
                               # ~ (icon_vsAI,       self.vsAI_button),
                               # ~ (icon_quit,       self.return_to_titlescreen)):
                                   
            # ~ button = QPushButton(self)
            # ~ button.setIcon(icon)
            # ~ button.setIconSize(QSize(150,80))
            # ~ button.setStyleSheet(self.stylesheets.clear_background)
            # ~ button.clicked.connect(function)
            # ~ button.hide()
            
            # ~ self.play_menu.append(button)
            
            # ~ if icon == icon_quit:
                # ~ self.playmenu_layout.addWidget(button)
            # ~ else:
                # ~ self.playoptions_layout.addWidget(button)
        

        
    def create_vsAI_buttons(self):
        
        self.vsAI_layout = QVBoxLayout()
        self.vsAI_layout.setContentsMargins(0,0,0,0)
        self.vsAI_layout.setAlignment(Qt.AlignCenter)
        self.vsAI_layout.setSpacing(0)
        self.main_layout.addLayout(self.vsAI_layout) 
        
        icon_AI_lvl1 =      self.mainwindow.icon_AI_lvl1
        icon_AI_lvl2 =      self.mainwindow.icon_AI_lvl2
        icon_AI_lvl3 =      self.mainwindow.icon_AI_lvl3
        icon_quit =         self.mainwindow.icon_quit
        
        self.vsAI_menu = []
        for icon, function in ((icon_AI_lvl1,    self.AI_lvl1_button), \
                               (icon_AI_lvl2,    self.AI_lvl2_button), \
                               (icon_AI_lvl3,    self.AI_lvl3_button), \
                               (icon_quit,       self.return_to_playmenu)):
                                   
            button = QPushButton(self)
            button.setIcon(icon)
            button.setIconSize(QSize(150,80))
            button.setStyleSheet(self.stylesheets.clear_background)
            button.clicked.connect(function)
            button.hide()
            
            self.vsAI_menu.append(button)
            self.vsAI_layout.addWidget(button)
                                   
        
            
    def create_options_buttons(self):
        
        self.options_menu_layout = QVBoxLayout()
        self.options_menu_layout.setContentsMargins(0,0,0,0)
        self.options_menu_layout.setSpacing(20)
        self.options_menu_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.addLayout(self.options_menu_layout)
        
        self.options_layout = QGridLayout()
        self.options_layout.setColumnStretch(1,0)
        self.options_layout.setHorizontalSpacing(30)
        self.options_layout.setVerticalSpacing(0)
        self.options_menu_layout.addLayout(self.options_layout)
        
        
        icon_sound =        self.mainwindow.icon_soundon
        icon_name =         self.mainwindow.icon_name
        icon_palettes =     self.mainwindow.icon_palettes
        icon_intructions =  self.mainwindow.icon_intructions
        icon_languages =    self.mainwindow.icon_languages
        icon_info =         self.mainwindow.icon_info
        icon_quit=          self.mainwindow.icon_quit
        
        
        self.options_menu = []
        for icon, function in ((icon_sound,        self.sound_button),
                               (icon_name,         self.name_button),
                               (icon_palettes,     self.themes_button),
                               (icon_intructions,  self.intructions_button),
                               (icon_languages,    self.languages_button),
                               (icon_info,         self.info_button),
                               (icon_quit,         self.return_to_titlescreen)):
                                   
            button = QPushButton(self)
            button.setIcon(icon)
            button.setIconSize(QSize(150,80))
            button.setStyleSheet(self.stylesheets.clear_background)
            button.hide()
            
            if icon == icon_sound:
                button.setCheckable(True)
                button.toggled.connect(function)
            else:
                button.clicked.connect(function)
            
            
            if icon == icon_quit:
                self.options_menu_layout.addWidget(button)
            else:
                self.options_layout.addWidget(button)
            
            
            self.options_menu.append(button)
            
            
        
    #================================================================================
    #   All of the functions for the title menu buttons are defined below.
    #================================================================================
    
    def play_button(self):
        
        for button in self.title_menu:
            button.hide()
        for button in self.play_menu:
            button.show()
        
        
        
    def options_button(self):
        
        for button in self.title_menu:
            button.hide()
        for button in self.options_menu:
            button.show()
    
    
    
    def shop_button(self):
        shop_mssg = QMessageBox(self)
        shop_mssg.setWindowTitle(" ")
        shop_mssg.setFixedSize(QSize(500,500))
        shop_mssg.setStyleSheet(self.stylesheets.text_CSS)
        
        #~ shop_options = QWidget(shop_mssg)
        #~ shop_options.setStyleSheet("background-color: white")
        #~ shop_options.resize(200,200)
        #~ shop_options.show()
    
        shop_mssg.show()
        
    
    def quit_button(self):
        quit_mssg = QMessageBox(self)
        quit_mssg.setWindowTitle(" ")
        quit_mssg.setText("Do you want to quit?")
        quit_mssg.setStyleSheet(self.stylesheets.text_CSS)
        quit_mssg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        quit_mssg.show()
        
        yes_button = quit_mssg.children()[3].children()[1]
        yes_button.clicked.connect(self.close_window)

    def close_window(self):
        self.close()
        self.parent().close()
        
        
    #================================================================================
    #   All of the functions for the play menu buttons are defined below.
    #================================================================================
    
    def internet_button(self):
        mssg = QMessageBox(self)
        mssg.setWindowTitle(" ")
        mssg.setText("(Plays game online)")
        mssg.setStyleSheet(self.stylesheets.text_CSS)
        mssg.show()
        
        
        
    def invite_button(self):
        mssg = QMessageBox(self)
        mssg.setWindowTitle(" ")
        mssg.setText("(Opens friends list)")
        mssg.setStyleSheet(self.stylesheets.text_CSS)
        mssg.show()
        
        
        
    def local_button(self):
        self.hide()
        self.mainwindow.local_game()
        
        
        
    def vsAI_button(self):
        for button in self.play_menu:
            button.hide()
        for button in self.vsAI_menu:
            button.show()
       
       
    def AI_lvl1_button(self):
        self.mainwindow.vsAI_game("level1")
        
    def AI_lvl2_button(self):
        self.mainwindow.vsAI_game("level2")
        
    def AI_lvl3_button(self):
        self.mainwindow.vsAI_game("level3")

        
    
    
    def return_to_playmenu(self):
        for button in self.vsAI_menu:
            button.hide()
        for button in self.play_menu:
            button.show()
        
        
    #================================================================================
    #   All of the functions for the options menu buttons are defined below.
    #================================================================================
    
    
    def sound_button(self):
        button = self.sender()
        
        if button.isChecked():
            icon = self.mainwindow.icon_soundoff
            self.mainwindow.sound_on = False
        else:
            icon = self.mainwindow.icon_soundon
            self.mainwindow.sound_on = True
            
        button.setIcon(icon)
        button.setIconSize(QSize(150,80))
        
        
        
    def languages_button(self):
        lang_mssg = QMessageBox(self)
        lang_mssg.setWindowTitle(" ")
        lang_mssg.setStyleSheet(self.stylesheets.text_CSS)
        lang_mssg.setIconPixmap(self.mainwindow.blank_langmssg)
        lang_mssg.show()
        
        lang_options = QComboBox(lang_mssg)
        lang_options.move(10,10)
        lang_options.resize(160,60)
        
        for option in ("English","Español","Français","Deutsch",\
                        "한글","中文","日本語"):
            lang_options.addItem(option)
            
        lang_options.setCurrentIndex(self.lang_dict[self.language])
        lang_options.activated.connect(self.change_language)
        lang_options.show()
        
    def change_language(self):
        combobox = self.sender()
        self.language = combobox.currentText()
        
        
        
    def themes_button(self):
        themes_mssg = QMessageBox(self)
        themes_mssg.setWindowTitle(" ")
        themes_mssg.setStyleSheet(self.stylesheets.text_CSS)
        themes_mssg.setIconPixmap(self.mainwindow.blank_thememssg)
        themes_mssg.show()
        
        
        themes_options = QComboBox(themes_mssg)
        themes_options.move(10,10)
        themes_options.resize(220,60)
        
        for option in ("Default", "Art Deco", "Cherry Soda", "Coffee", \
                        "Spring Green", "Victorian"):
            themes_options.addItem(option)

        themes_options.setCurrentIndex(self.theme_dict[self.theme])
        themes_options.activated.connect(self.change_theme)
        themes_options.show()
        
        ok_button = themes_mssg.children()[2].children()[1]
        ok_button.clicked.connect(self.change_appearance)
        
        
        
    def change_theme(self):
        combobox = self.sender()
        self.theme = combobox.currentText()
        
    def change_appearance(self):
        self.close()
        self.mainwindow.change_theme(self.theme)

        
        
        
    def name_button(self):
        
        self.name_input = QInputDialog(self)
        self.name_input.setWindowTitle(" ")
        self.name_input.setStyleSheet(self.stylesheets.text_CSS)
        self.name_input.show()
        
        title_text = self.name_input.children()[1]
        title_text.setText("Name:")
        
        line_edit = self.name_input.children()[0]
        current_name = self.mainwindow.player_names[0]
        
        if current_name == "":
            line_edit.setPlaceholderText("Player 1")
        else:
            line_edit.setText(current_name)
        
        ok_button = self.name_input.children()[2].children()[1]
        ok_button.clicked.connect(self.name_button_end)
        
    def name_button_end(self):
        new_name = self.name_input.textValue()
        self.mainwindow.player_names[0] = new_name
        
        
        
    def intructions_button(self):
        mssg = QMessageBox(self)
        mssg.setWindowTitle(" ")
        mssg.setText("(Explains the rules of the game)")
        mssg.setStyleSheet(self.stylesheets.text_CSS)
        mssg.show()
        
        
        
    def info_button(self):
        
        info_mssg = QMessageBox(self)
        info_mssg.setWindowTitle(" ")
        info_mssg.setStyleSheet(self.stylesheets.credits_CSS)
        
        text = "\n".join(["Created and Produced", \
                          "Albert 'Anferensis' Ong\n", \
                          "Special Thanks", \
                          "John 'Aotus' Ladasky\n", \
                          "© 2015 (company name)"])
        
        info_mssg.setText(text)
        info_mssg.show()
        
        mssg_text = info_mssg.children()[2]
        mssg_text.setAlignment(Qt.AlignCenter)
        
        for child in info_mssg.children():
            if type(child) == QGridLayout:
                child.setContentsMargins(0,10,20,10)
        
        
        
    #================================================================================
    #   Other miscellaneous functions. 
    #================================================================================
    
    def return_to_titlescreen(self):
        
        for button in self.options_menu + self.play_menu:
            if button.isVisible():
                button.hide()
            
        for button in self.title_menu:
            button.show()
            


#====================================================================================

def main():
    pass
    
if __name__ == "__main__":
    main()
    
    
    
    
    



