#!/usr/bin/python3

#####################################################################################
#
# CenterSide: a board game
# Written in PyQt5
# Created by Albert "Anferensis" Ong
#
#####################################################################################

import sys 
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QPixmap
# ~ from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, \
                            QPushButton, QLabel, QMessageBox


from CenterSide_StyleSheets import StyleSheets
# ~ import CenterSide_AI_level1 
# ~ import CenterSide_AI_level2 
# ~ import CenterSide_AI_level3

from itertools import cycle

#====================================================================================

class CenterSideGame(QWidget):
    """
    Creates a game of CenterSide given a CenterSideWindow and a mode.
    """
    def __init__(self, mainwindow, mode):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)
        self.grabKeyboard()
        
        self.mainwindow = mainwindow
        self.mode = mode
        
        self.color_cycle = cycle(("color1","color2"))
        self.current_color = next(self.color_cycle)
        self.turn_count = 0
        self.gameover = False
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0,0,0,3)
        self.main_layout.setSpacing(0)
        
        
        if mode == "Local":
            self.player_names = self.mainwindow.default_names
            
        elif mode.startswith("vsAI"):
            
            player_1 = self.mainwindow.player_names[0]
            if player_1 == "":
                player_1 = "Player 1"
            self.player_names = [player_1, "Computer"]
            
        else:
            self.player_names = self.mainwindow.player_names
            
        
        self.import_art_assets()
        self.import_sounds()
        self.create_main_buttons()
        self.create_board()
        self.create_main_text()
        

            
        if mode.startswith("vsAI") and self.mainwindow.AI_player == "Player 1":
            self.change_playertext_colors()
            self.current_color = next(self.color_cycle)
            self.AI_turn()
        
        
        
    #================================================================================
    #   All of the functions used in init.
    #================================================================================
    
    def import_art_assets(self):

        self.sound_on =             self.mainwindow.sound_on
        self.stylesheets =          self.mainwindow.stylesheets
        
        self.blank_piece =          self.mainwindow.blank_piece
        self.p1_piece =             self.mainwindow.p1_piece
        self.p2_piece =             self.mainwindow.p2_piece
        self.p1_piece_opaque =      self.mainwindow.p1_piece_opaque
        self.p2_piece_opaque =      self.mainwindow.p2_piece_opaque
        self.p1_deny =              self.mainwindow.p1_deny
        self.p2_deny =              self.mainwindow.p2_deny
        self.p1_deny_opaque =       self.mainwindow.p1_deny_opaque
        self.p2_deny_opaque =       self.mainwindow.p2_deny_opaque
        self.deny =                 self.mainwindow.deny
        self.deny_opaque =          self.mainwindow.deny_opaque
        
        self.icon_chat =            self.mainwindow.icon_chat
        self.icon_refresh =         self.mainwindow.icon_refresh
        self.icon_quit =            self.mainwindow.icon_quit
        
        
        
    def import_sounds(self):
        
        assets_dir = self.mainwindow.assets_dir
        self.sound_playpiece =   QSound(assets_dir + "SFX/play_piece.wav")
        self.sound_denypiece =   QSound(assets_dir + "SFX/deny_piece.wav")
        self.sound_restart =     QSound(assets_dir + "SFX/restart.wav")
        self.sound_winbell =     QSound(assets_dir + "SFX/win_bell.wav")
        
    
    
    def create_main_buttons(self):
        """
        Creates the chat, refresh and quit buttons.
        Note: These buttons are not placed in the main layout.
              This is mainly due to design impracticality.
        """
        self.main_buttons = []
        
        for num, icon, func in ((0, self.icon_chat, self.chat_mssg), \
                                (1, self.icon_refresh, self.restart_mssg), \
                                (2, self.icon_quit, self.quit_mssg)):
            
            button = QPushButton(self)
            button.setIcon(icon)
            button.setIconSize(QSize(75,40))
            button.resize(75,40)
            button.move(700, 450 + 45 * num)
            button.setStyleSheet(self.stylesheets.clear_background)
            button.clicked.connect(func)
            self.main_buttons.append(button)

        if self.mode in ("Local", "vsAI_lvl1", "vsAI_lvl2", "vsAI_lvl3"):
            self.main_buttons[0].hide()
    
    
    def create_board(self):
        """
        Builds a 10x10 grid of tile buttons represented as a list of lists.
        Deletes the center 2x2 block and replaces them with Nones.
        """
        
        self.mainwindow.grid.show()
        
        self.board_layout = QGridLayout()
        self.board_layout.setContentsMargins(172,32,170,0)
        self.board_layout.setColumnStretch(9,0)
        self.board_layout.setRowStretch(9,0)
        self.board_layout.setSpacing(2)
        self.main_layout.addLayout(self.board_layout)
        
        self.board = []
        for height in range(10):
            row = []
            for width in range(10):
                button = QPushButton(self)
                button.setIcon(self.blank_piece)
                button.setIconSize(QSize(35,35))
                button.setStyleSheet(self.stylesheets.clear_background)
                button._color = None
                button._filled = False
                button._denied = False
                button._coordinate = [height + 1,width + 1]
                button.clicked.connect(self.select_button)
                row.append(button)
                self.board_layout.addWidget(button)
            self.board.append(row)
            
        for coord_change in ((0,0),(0,1),(1,0),(1,1)):
            center_coord = [4,4]
            changed_coord = [center_coord[0] + coord_change[0],\
                             center_coord[1] + coord_change[1]]
            button = self.board[changed_coord[0]][changed_coord[1]]
            button.deleteLater()
            self.board[changed_coord[0]][changed_coord[1]] = None
            
        blanks = ["blank"] * 12
        self.board = [blanks] + \
                    [["blank"] + row + ["blank"] for row in self.board] + \
                    [blanks]
    
    
    
    def create_main_text(self):
        """
        Creates the win counts, deny counts, and player name objects.
        """
        self.text_layout = QHBoxLayout()
        self.text_layout.setContentsMargins(0,25,0,0)
        self.text_layout.setAlignment(Qt.AlignHCenter)
        self.text_layout.setSpacing(5)
        self.main_layout.addLayout(self.text_layout)
        
        self.p1_wincount = QLabel("0",self)
        self.p2_wincount = QLabel("0",self)
        
        self.player1_text = QLabel(self.player_names[0],self)
        self.player2_text = QLabel(self.player_names[1],self)
        
        for label, stylesheet, size in \
                ((self.p1_wincount,   self.stylesheets.p1_wincount, (100,70)), \
                 (self.p2_wincount,   self.stylesheets.p2_wincount, (100,70)), \
                 (self.player1_text,  self.stylesheets.p1_solid,    (160,30)), \
                 (self.player2_text,  self.stylesheets.p2_opaque,   (160,30))):
                                        
            label.setStyleSheet(stylesheet)
            label.setAlignment(Qt.AlignCenter)
            label.setFixedSize(size[0], size[1])
            
            if label == self.p1_wincount or self.p2_wincount:
                label._count = 0
                
        
        self.p1_name_denies = QVBoxLayout()
        self.p2_name_denies = QVBoxLayout()
        
        for layout, label in ((self.p1_name_denies, self.player1_text), \
                              (self.p2_name_denies, self.player2_text)):
            layout.setAlignment(Qt.AlignTop)
            layout.setSpacing(5)
            layout.addWidget(label)
        
        self.p1_denies = []
        self.p2_denies = []
        self.p1_denies_layout = QGridLayout()
        self.p2_denies_layout = QGridLayout()
        
        for par_layout, chl_layout, denies_list, pixmap in \
                ((self.p1_name_denies, self.p1_denies_layout, self.p1_denies, self.p1_deny), \
                 (self.p2_name_denies, self.p2_denies_layout, self.p2_denies, self.p2_deny_opaque)):
            
            chl_layout.setAlignment(Qt.AlignHCenter)
            chl_layout.setSpacing(5)
            chl_layout.setColumnStretch(2,0)
        
            for num in range(3):
                deny = QLabel(self)
                deny.setPixmap(pixmap)
                chl_layout.addWidget(deny)
                denies_list.append(deny)
            par_layout.addLayout(chl_layout)
        
        
        for item in (self.p1_name_denies, self.p1_wincount, \
                     self.p2_wincount, self.p2_name_denies):
                         
            if type(item) == QLabel:
                self.text_layout.addWidget(item)
            else:
                self.text_layout.addLayout(item)
                
        
        
    #================================================================================
    #   Game logic handled below
    #================================================================================
    
    
    
    def select_button(self):
        button = self.sender()
            
        icon = self.p1_piece if self.current_color == "color1" \
          else self.p2_piece
        
        if button._coordinate in self.viable_coordinates():
            
            button.setIcon(icon)
            button.setIconSize(QSize(35,35))
            button._filled = True
            button._color = self.current_color
            
            if self.sound_on:
                self.sound_playpiece.play()
            
            self.turn_count += 1
            self.game_over_check()
            self.tie_check()
            self.change_playertext_colors()
            self.current_color = next(self.color_cycle)
            
            
        elif button._coordinate in self.deniable_coordinates():
            
            button.setIcon(self.deny)
            button.setIconSize(QSize(35,35))
            button._color = None
            button._denied = True
                
            player_denies = self.p1_denies if self.current_color == "color1" \
                       else self.p2_denies
                
            for label in player_denies:
                if label.isHidden():
                    pass
                else:
                    label.hide()
                    break
            
            if self.sound_on:
                self.sound_denypiece.play()
            
            self.turn_count += 1
            self.change_playertext_colors()
            self.current_color = next(self.color_cycle)
            
        if self.mode.startswith("vsAI") and not self.gameover:
            self.AI_turn()
        

    
    def viable_coordinates(self):
        """
        Returns a list of all the viable coordinates on a board.
        """
        coordinates = []
        
        for row in self.board:
            for tile in row:
                
                if any([tile == "blank", tile == None, \
                        type(tile) == QPushButton and tile._filled]):
                    pass
                    
                else:
                    viable_check = []
                    coord = tile._coordinate
                    
                    for coord_change in ((0,1),(-1,0),(0,-1),(1,0)):
                        changed_coord = [coord[0] + coord_change[0],\
                                         coord[1] + coord_change[1]]
                        check = self.board[changed_coord[0]][changed_coord[1]]
                        
                        if check == "blank":
                            pass
                        elif check == None:
                            viable_check.append(True)
                        elif type(check) == QPushButton and check._filled:
                            viable_check.append(True)
                            
                    if any(viable_check):
                        coordinates.append(coord)
                        
        return coordinates
    
    
    
    def deniable_coordinates(self):
        
        opposite_color = "color2" if self.current_color == "color1" \
                    else "color1"
                    
        player_denies = self.p1_denies if self.current_color == "color1" \
                       else self.p2_denies
        
        coordinates = []
        
        if all([label.isHidden() for label in player_denies]):
            pass
        else:
            for row in self.board:
                for tile in row:
                    
                    if tile == "blank" or tile == None:
                        pass
                        
                    elif tile._color == opposite_color:
                        coordinates.append(tile._coordinate)
        return coordinates
        
        
        
    def all_segments(self):
        """
        Returns a list of all the 4x1 horizontal, vertical, and diagonal
        segments on the CenterSide board.
        """
        clmns = clmns = [clmn for clmn in list(zip(*self.board))[1:11]]
        
        row_segs = [row[num:num + 4] for num in range(1,8) for row in self.board[1:11]]
        clmn_segs = [clmn[num:num + 4] for num in range(1,8) for clmn in clmns]
        diag_segs = self.diagonal_segments()
        
        segments = row_segs + clmn_segs + diag_segs
        segs_minus_nones = [seg for seg in segments if None not in seg]
        
        return segs_minus_nones
        
    
    
    def diagonal_segments(self):
        """
        Takes the CenterSide board and returns all the diagonal 4x1 segments.
        This is used specifically in all_segments
        """
        sw_diag_coords = [[num,1] for num in range(1,8)] + \
                         [[1,num] for num in range(2,8)]
        nw_diag_coords = [[10 - num, 1] for num in range(7)] + \
                         [[10,num] for num in range(2,8)]
        
        diags = []
        for diag_coords in (sw_diag_coords, nw_diag_coords):
            for coord in diag_coords:
                
                diag = []
                tile = self.board[coord[0]][coord[1]]
                
                while tile != "blank":
                    diag.append(tile)
                    
                    if diag_coords == sw_diag_coords:
                        coord[0] += 1
                    else:
                        coord[0] -= 1
                        
                    coord[1] += 1
                    tile = self.board[coord[0]][coord[1]]
                    
                diags.append(diag)
            
        segments = []
        for diag in diags:
            for num in range(1 + len(diag) - 4):
                seg = diag[num:num + 4]
                segments.append(seg)
        
        return segments
        
        
        
    def game_over_check(self):
        """
        Checks all the 4x1 veritcal, horizontal, and diagonal segments on the CenterSide board.
        Runs game_over if all tiles in a segment are the same color.
        """
    
        p1_win = ["color1"] * 4
        p2_win = ["color2"] * 4
        
        for seg in self.all_segments():
            seg_colors = [tile._color for tile in seg if tile != None]
            
            if seg_colors == p1_win:
                self.game_over("Player 1", seg)
                
            elif seg_colors == p2_win:
                self.game_over("Player 2", seg)
                
                
                
    def game_over(self, winner, winning_segment):
        """
        Runs the game over scenario.
        """
        self.gameover = True
        
        if self.sound_on:
            self.sound_winbell.play()
        
        if winner == "Player 1":
            
            wincount = self.p1_wincount
            player_name = self.player_names[0]
            
        elif winner == "Player 2":
            
            wincount = self.p2_wincount
            player_name = self.player_names[1]
        
        wincount._count += 1
        wincount.setText(str(wincount._count))
        
        if wincount._count > 99:
            for wincount in (self.p1_wincount, self.p2_wincount):
                wincount._count = 0
                wincount.setText(str(wincount._count))
        
        win_mssg = QMessageBox(self)
        win_mssg.setWindowTitle(" ")
        win_mssg.setText(player_name + " wins!")
        win_mssg.setStyleSheet(self.stylesheets.text_CSS) 
        win_mssg.show()
        
        ok_button = win_mssg.children()[3].children()[1]
        ok_button.clicked.connect(self.replay_mssg)
        
        for row in self.board:
            for tile in row:
                
                if type(tile) == QPushButton and tile not in winning_segment:
                    icon = False
                    
                    if tile._color == "color1":
                        icon = self.p1_piece_opaque
                        
                    elif tile._color == "color2":
                        icon = self.p2_piece_opaque
                        
                    elif tile._denied:
                        icon = self.deny_opaque
                    
                    if icon:
                        tile.setIcon(icon)
                        tile.setIconSize(QSize(35,35))
            
            
            
    def tie_check(self):
        
        check = []
        
        for row in self.board:
            for tile in row:
                if type(tile) == QPushButton:
                    check.append(tile._filled)
                    
        is_tie = all(check)
        if is_tie:
            self.tie_game()
            
            
            
    def tie_game(self):
        
        tie_mssg = QMessageBox(self)
        tie_mssg.setWindowTitle(" ")
        tie_mssg.setText("Tie Game!")
        tie_mssg.setStyleSheet(self.stylesheets.text_CSS)
        tie_mssg.show()
        
        button = tie_mssg.children()[3].children()[1]
        button.clicked.connect(self.replay_mssg)
    
    
                        
    def replay_mssg(self):
        """
        Lets the user choose to either play again or leave the game.
        """
        replay_mssg = QMessageBox(self)
        replay_mssg.setWindowTitle(" ")
        replay_mssg.setText("Play again?")
        replay_mssg.setStyleSheet(self.stylesheets.text_CSS)
        replay_mssg.setStandardButtons(QMessageBox.Yes|QMessageBox.No) 
        replay_mssg.show()
        
        yes_button = replay_mssg.children()[3].children()[1]
        no_button = replay_mssg.children()[3].children()[2]
        
        yes_button.clicked.connect(self.restart_game)
        no_button.clicked.connect(self.leave_game)
        
        
        
    #================================================================================
    #   All of the functions for the main buttons are defined below.
    #================================================================================
    
    def chat_mssg(self):
        
        mssg = QMessageBox(self)
        mssg.setWindowTitle(" ")
        mssg.setText("(Displays chat)")
        mssg.setStyleSheet(self.stylesheets.text_CSS)
        mssg.show()
        
        
    
    def restart_mssg(self):
        """
        Gives the user the option to restart a game.
        Will not allow the user to restart for the first 6 turns.
        """
        if self.turn_count == 0:
            pass
            
        restart_mssg = QMessageBox(self)
        restart_mssg.setWindowTitle(" ")
        restart_mssg.setText("Restart game?")
        restart_mssg.setStyleSheet(self.stylesheets.text_CSS)
        restart_mssg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)  
        restart_mssg.show()
        
        yes_button = restart_mssg.children()[3].children()[1]
        yes_button.clicked.connect(self.restart_game)
                
                
                
    def restart_game(self):
        
        for row in self.board:
            for tile in row:
                if type(tile) == QPushButton:
                    button = tile
                    button.setIcon(self.blank_piece)
                    button._color = None
                    button._filled = False
                    button._denied = False
            
        for label in self.p1_denies + self.p2_denies:
            label.show()
            
        if self.sound_on:
            self.sound_restart.play()
            
        self.turn_count = 0
        self.gameover = False
        
        if self.mode.startswith("vsAI") and self.current_color == "color2":
            self.AI_turn()
    
    
    
    def quit_mssg(self):
        """
        Displays a message which allows the user to choose to leave the game.
        """
        quit_mssg = QMessageBox(self)
        quit_mssg.setWindowTitle(" ")
        quit_mssg.setText("Do you want to quit?")
        quit_mssg.setStyleSheet(self.stylesheets.text_CSS)  
        quit_mssg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)  
        quit_mssg.show()
        
        yes_button = quit_mssg.children()[3].children()[1]
        yes_button.clicked.connect(self.leave_game)
        
        
        
    def leave_game(self):
        """
        Returns the user to the title screen
        """
        self.mainwindow.grid.hide()
        self.close()
        self.mainwindow.return_to_titlemenu()
        
        
    #================================================================================
    #   Other miscellaneous functions.
    #================================================================================
    
    def change_playertext_colors(self):
        """
        Changes the appearance of the player names and player denies such that 
        the previous player's text is opaque and the current player's text
        is solid.
        """
        if self.current_color == "color1": 
            
            p1_CSS = self.stylesheets.p1_opaque
            p2_CSS = self.stylesheets.p2_solid
            
            p1_deny = self.p1_deny_opaque
            p2_deny = self.p2_deny
            
        else:
            p1_CSS = self.stylesheets.p1_solid
            p2_CSS = self.stylesheets.p2_opaque
            
            p1_deny = self.p1_deny
            p2_deny = self.p2_deny_opaque
            
        for label, stylesheet in ((self.player1_text, p1_CSS), \
                                  (self.player2_text, p2_CSS)):
            label.setStyleSheet(stylesheet)
    
        for _set, pixmap in ((self.p1_denies, p1_deny), \
                            (self.p2_denies, p2_deny)):
                                
            for label in _set:
                label.setPixmap(pixmap)
                
                
                
    #================================================================================
    #   AI implementation created below
    #================================================================================
                
                
    def AI_turn(self):
        self.grabMouse()
        timer = QTimer(self)
        timer.singleShot(1000, self.AI_turn2)
        
    def AI_turn2(self):
        self.releaseMouse()
        
        if self.mode == "vsAI_lvl1":
            coord = CenterSide_AI_level1.next_move(self)
        elif self.mode == "vsAI_lvl2":
            coord = CenterSide_AI_level2.next_move(self)
        elif self.mode == "vsAI_lvl3":
            coord = CenterSide_AI_level3.next_move(self)
            

        button = self.board[coord[0]][coord[1]]
                
        icon = self.p1_piece if self.current_color == "color1" \
          else self.p2_piece
        
        if button._coordinate in self.viable_coordinates():
            
            button.setIcon(icon)
            button.setIconSize(QSize(35,35))
            button._filled = True
            button._color = self.current_color
            
            if self.sound_on:
                self.sound_playpiece.play()
            
            self.turn_count += 1
            self.game_over_check()
            self.change_playertext_colors()
            self.current_color = next(self.color_cycle)
            
            
        elif button._coordinate in self.deniable_coordinates():
            
            button.setIcon(self.deny)
            button.setIconSize(QSize(35,35))
            button._color = None
            button._denied = True
                
            player_denies = self.p1_denies if self.current_color == "color1" \
                       else self.p2_denies
                
            for label in player_denies:
                if label.isHidden():
                    pass
                else:
                    label.hide()
                    break
            
            if self.sound_on:
                self.sound_denypiece.play()
            
            self.turn_count += 1
            self.change_playertext_colors()
            self.current_color = next(self.color_cycle)

                
            
        
#====================================================================================
    
if __name__ == "__main__":
    pass
    


