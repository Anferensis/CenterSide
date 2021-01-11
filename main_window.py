#!/usr/bin/python3

"""
CenterSide: a board game

Created by Albert "Anferensis" Ong
"""


import os
import sys 

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtSvg import *

from game_window import GameWindow
from menu_window import MenuWindow
from stylesheets import StyleSheets


#====================================================================================


class MainWindow(QMainWindow):
    """
    The outer most shell of the CenterSide programs. 
    Creates a Menu given a theme.
    
    A MainWindow combines a MenuWindow object and
    a GameWindow object to create a whole program.
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
        
        self.setWindowTitle("CenterSide")
        
        self.width = 1280
        self.height = 720
        
        self.setFixedSize(self.width, self.height )
        
        os.chdir("assets")
        
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("background.png"))
        self.background.resize(self.width, self.height)
        
        self.grid = QLabel(self)
        self.grid.setPixmap(QPixmap("SVG/grid.svg"))
        self.grid.setAlignment(Qt.AlignCenter)
        self.grid.resize(self.width, self.height)
        self.grid.hide()
        
        self.icon_play = QIcon("play_button.png")
        self.icon_options = QIcon("options_button.png")
        self.icon_help = QIcon("help_button.png")
        self.icon_quit = QIcon("quit_button.png")
        
        self.blank_piece =          QIcon("SVG/blank.svg")
        self.p1_piece =             QIcon("SVG/color1.svg")
        self.p2_piece =             QIcon("SVG/color2.svg")
        self.p1_piece_opaque =      QIcon("SVG/color1_opaque.svg")
        self.p2_piece_opaque =      QIcon("SVG/color2_opaque.svg")
        self.deny =                 QIcon("SVG/deny.svg")
        self.deny_opaque =          QIcon("SVG/deny_opaque.svg")
        
        self.p1_deny =              QPixmap("SVG/color1_deny.svg")
        self.p2_deny =              QPixmap("SVG/color2_deny.svg")
        self.p1_deny_opaque =       QPixmap("SVG/color1_deny_opaque.svg")
        self.p2_deny_opaque =       QPixmap("SVG/color2_deny_opaque.svg")
        
        self.logo = QIcon("SVG/CenterSide_icon.svg")
        self.setWindowIcon(self.logo)
        
        self.build_assets()
        
        self.menu_window = MenuWindow(self)
        self.setCentralWidget(GameWindow(self, "local"))
                            
        self.show()
        
        
        
    def build_assets(self):
        """
        Assembles all of the images,icons,and sounds that will be 
        used in an instance of CenterSide.
        """
        theme = self.theme
            
        # ~ self.assets_dir = cwd + "/CenterSide_Themes/" + theme + "/"
        
        
        
        
        
        
        # ~ self.blank_langmssg =       QPixmap("blank_langmssg.svg")
        # ~ self.blank_thememssg =      QPixmap("blank_thememssg.svg")
        
        
        
        
        
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
        
        # ~ self.icon_quit =            QIcon("Icons/quit.svg")
        # ~ self.icon_refresh =         QIcon("Icons/refresh.svg")
        # ~ self.icon_shop =            QIcon("Icons/shop.svg")
        # ~ self.icon_soundon =         QIcon("Icons/soundon.svg")
        # ~ self.icon_soundoff =        QIcon("Icons/soundoff.svg")
        # ~ self.icon_vsAI =            QIcon("Icons/vsAI.svg")
        
        
        
    def local_game(self):
        gamewindow = CenterSideGame(self, "Local")
        self.setCentralWidget(gamewindow)
            
    
    def change_theme(self, theme):
        
        self.theme =            theme
        self.stylesheets =      StyleSheets(theme)
        self.build_assets()
        self.setWindowIcon(self.logo)
        
        session = CenterSideSession(self)
        self.setCentralWidget(session)
        
        
        
    def return_to_titlemenu(self):
        self.setCentralWidget(self.menu_window)



#====================================================================================       
        
def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())
  
if __name__ == "__main__": 
    main()  
    
    
    
