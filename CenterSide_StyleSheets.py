#!/usr/bin/python3

#####################################################################################
#
# CenterSide: a board game
# Written in PyQt5
# Created by Albert "Anferensis" Ong
#
#####################################################################################

size20 = "font-size: 20px;"
size25 = "font-size: 25px;"
size80 = "font-size: 80px;"
size90 = "font-size: 90px;"


class StyleSheets:
    """
    Assembles all the stylesheets that will be used in an instance of the
    CenterSide programs given a theme.
    """
    def __init__(self, theme = "Default"):
        
        if theme == "Default":
            
            font =              "font-weight: bold; font-family: Sans;"
            background =        "background-color: rgb(240,200,115);"
            text_color =        "color: black;"
            
            color1 =            "color: red;"
            color1_opaque =     "color: rgba(255,0,0,0.25);"
            
            color2 =            "color: black;"
            color2_opaque =     "color: rgba(0,0,0,0.25);"
            
            
        elif theme == "Alternate":
            
            font =              "font-weight: Bold; font-family: Sans;"
            background =        "background-color: rgb(0,60,140);"
            text_color =        "color: rgb(255,130,0);"
            
            color1 =            "color: white;"
            color1_opaque =     "color: rgba(255,255,255,0.25);"
            
            color2 =            "color: rgb(255,130,0);"
            color2_opaque =     "color: rgba(255,130,0,0.25);"
            
            
        elif theme == "Art Deco":
            
            font =              "font-weight: Bold; font-family: Market Deco;"
            background =        "background-color: rgb(30,30,30);"
            text_color =        "color: rgb(255,190,0);"
            
            
            color1 =            "color: rgb(255,40,160);"
            color1_opaque =     "color: rgba(255,40,160,0.5);"
            
            color2 =            "color: rgb(255,190,0);"
            color2_opaque =     "color: rgba(255,190,0,0.5);"
            
            
        elif theme == "Cherry Soda":
            
            font =              "font-weight: Bold; font-family: GeosansLight;"
            background =        "background-color: rgb(70,0,0);"
            text_color =        "color: white;"
            
            color1 =            "color: rgb(255,0,255);"
            color1_opaque =     "color: rgba(255,0,255,0.25);"
            
            color2 =            "color: red;"
            color2_opaque =     "color: rgba(255,0,0,0.25);"
            
            
        elif theme == "Coffee":
            
            font =              "font-weight: bold; font-family: Santana;"
            background =        "background-color: rgb(33,15,6);"
            text_color =        "color: rgb(220,190,140);"
            
            color1 =            "color: rgb(255,102,0);"
            color1_opaque =     "color: rgba(255,102,0,0.25);"
            
            color2 =            "color: rgb(160,44,44)"
            color2_opaque =     "color: rgba(160,44,44,0.25);"
            
            
        elif theme == "Victorian":
            
            font =              "font-weight: bold; font-family: Rochester;"
            background =        "background-color: rgb(0,26,48);"
            text_color =        "color: white;"
            
            color1 =            "color: rgb(150,186,143);"
            color1_opaque =     "color: rgba(159,186,143,0.25);"
            
            color2 =            "color: rgb(85,151,237);"
            color2_opaque =     "color: rgba(85,151,237,0.25);"
            
        elif theme == "Spring Green":
            
            font =              "font-weight: bold; font-family: Sans;"
            background =        "background-color: rgb(58,145,12);"
            text_color =        "color: rgb(255,212,42);"
            
            color1 =            "color: rgb(255,212,42);"
            color1_opaque =     "color: rgba(255,212,42,0.25);"
            
            color2 =            "color: rgb(0,255,0);"
            color2_opaque =     "color: rgba(0,255,0,0,25);"
            
            
            #=========================================================
            
        self.clear_background =     "background-color: rgba(255,255,255,0)"
        self.text_CSS =             font + size25 + text_color + background
        self.credits_CSS =          font + size20 + text_color + background
        self.title_CSS =            font + size90 + text_color
            
        self.p1_solid =             font + size25 + color1
        self.p2_solid =             font + size25 + color2
        
        self.p1_opaque =            font + size25 + color1_opaque
        self.p2_opaque =            font + size25 + color2_opaque
        
        self.p1_wincount =          font + size80 + color1
        self.p2_wincount =          font + size80 + color2
        
    
    
#====================================================================================
        
if __name__ == "__main__":
    pass
            
            
            
            
