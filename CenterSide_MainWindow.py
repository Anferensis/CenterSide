#!/usr/bin/python3

#####################################################################################
#
# CenterSide: a board game
# Written in PyQt5
# Created by Albert "Anferensis" Ong
#
#####################################################################################

import sys 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


from CenterSide_Game import CenterSideGame
from CenterSide_Session import CenterSideSession
from CenterSide_StyleSheets import StyleSheets

import os

#====================================================================================


class CenterSideWindow(QMainWindow):
    """
    The outer most shell of the CenterSide programs. 
    Creates a CenterSideWindow given a theme.
    
    A CenterSideWindow combines a CenterSideSession object and
    a CenterSideGame object to create a whole program.
    """
    def __init__(self, theme = "Default"):
        super().__init__()
        
        self.sound_on =             True
        self.language =             "English"
        self.default_names =        ["Player 1", "Player 2"]
        self.player_names =         ["", ""]
        self.theme =                theme
        self.stylesheets =          StyleSheets(theme)
        self.AI_player =            "Player 1"
        
        self.background = QLabel(self)
        self.build_assets()
        
                    #=========================================#       
        
        session = CenterSideSession(self)
        self.setCentralWidget(session)
        
                    #=========================================#
        
        self.setWindowTitle("CenterSide")
        # ~ self.setWindowIcon(self.logo)
        self.setFixedSize(800,600)
        self.show()
        
        
        
    def build_assets(self):
        """
        Assembles all of the images,icons,and sounds that will be 
        used in an instance of CenterSide.
        """
        theme = self.theme
            
        cwd = os.getcwd()
        # ~ self.assets_dir = cwd + "/CenterSide_Themes/" + theme + "/"
        # ~ os.chdir(self.assets_dir)
        
        # ~ self.background.setPixmap(QPixmap("background.png"))
        # ~ self.background.resize(800,600)
        
        # ~ self.grid = QLabel(self)
        # ~ self.grid.setPixmap(QPixmap("grid.svg"))
        # ~ self.grid.setAlignment(Qt.AlignCenter)
        # ~ self.grid.resize(800,600)
        # ~ self.grid.hide()
        
        # ~ self.logo =                 QIcon("CenterSide_Logo.svg")
        
        # ~ self.blank_langmssg =       QPixmap("blank_langmssg.svg")
        # ~ self.blank_thememssg =      QPixmap("blank_thememssg.svg")
        
        # ~ self.blank_piece =          QIcon("Pieces/blank.svg")
        # ~ self.p1_piece =             QIcon("Pieces/color1.svg")
        # ~ self.p2_piece =             QIcon("Pieces/color2.svg")
        # ~ self.p1_piece_opaque =      QIcon("Pieces/color1_opaque.svg")
        # ~ self.p2_piece_opaque =      QIcon("Pieces/color2_opaque.svg")
        # ~ self.deny =                 QIcon("Pieces/deny.svg")
        # ~ self.deny_opaque =          QIcon("Pieces/deny_opaque.svg")
        
        # ~ self.p1_deny =              QPixmap("Pieces/color1_deny.svg")
        # ~ self.p2_deny =              QPixmap("Pieces/color2_deny.svg")
        # ~ self.p1_deny_opaque =       QPixmap("Pieces/color1_deny_opaque.svg")
        # ~ self.p2_deny_opaque =       QPixmap("Pieces/color2_deny_opaque.svg")
        
        # ~ self.icon_AI_lvl1 =         QIcon("Icons/AI_lvl1.svg")
        # ~ self.icon_AI_lvl2 =         QIcon("Icons/AI_lvl2.svg")
        # ~ self.icon_AI_lvl3 =         QIcon("Icons/AI_lvl3.svg")
        # ~ self.icon_chat =            QIcon("Icons/chat.svg")
        # ~ self.icon_info =            QIcon("Icons/info.svg")
        # ~ self.icon_intructions =     QIcon("Icons/instructions.svg")
        # ~ self.icon_internet =        QIcon("Icons/internet.svg")
        # ~ self.icon_invite =          QIcon("Icons/invite.svg")
        # ~ self.icon_languages =       QIcon("Icons/languages.svg")
        # ~ self.icon_local =           QIcon("Icons/local.svg")
        # ~ self.icon_message =         QIcon("Icons/message.svg")
        # ~ self.icon_name =            QIcon("Icons/name.svg")
        # ~ self.icon_options =         QIcon("Icons/options.svg")
        # ~ self.icon_palettes =        QIcon("Icons/palettes.svg")
        # ~ self.icon_play =            QIcon("Icons/play.svg")
        # ~ self.icon_quit =            QIcon("Icons/quit.svg")
        # ~ self.icon_refresh =         QIcon("Icons/refresh.svg")
        # ~ self.icon_shop =            QIcon("Icons/shop.svg")
        # ~ self.icon_soundon =         QIcon("Icons/soundon.svg")
        # ~ self.icon_soundoff =        QIcon("Icons/soundoff.svg")
        # ~ self.icon_vsAI =            QIcon("Icons/vsAI.svg")
        
        os.chdir(cwd)
        
        
        
    def local_game(self):
        gamewindow = CenterSideGame(self, "Local")
        self.setCentralWidget(gamewindow)
        
        
        
    def vsAI_game(self, level):
        
        if level == "level1":
            gamewindow = CenterSideGame(self, "vsAI_lvl1")
        elif level == "level2":
            gamewindow = CenterSideGame(self, "vsAI_lvl2")
        elif level == "level3":
            gamewindow = CenterSideGame(self, "vsAI_lvl3")
            
        self.setCentralWidget(gamewindow)
        
    
    
    def internet_game(self):
        pass
        
        
        
    def invite_game(self):
        pass
            
            
    
    def change_theme(self, theme):
        
        self.theme =            theme
        self.stylesheets =      StyleSheets(theme)
        self.build_assets()
        self.setWindowIcon(self.logo)
        
        session = CenterSideSession(self)
        self.setCentralWidget(session)
        
        
        
    def return_to_titlemenu(self):
        session = CenterSideSession(self)
        self.setCentralWidget(session)



#====================================================================================       
        
def main():
    app = QApplication(sys.argv)
    mainwindow = CenterSideWindow()
    sys.exit(app.exec_())
  
if __name__ == "__main__": 
    main()  
    
    
    
