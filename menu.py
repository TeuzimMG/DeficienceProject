import pyttsx3 # importamos o modúlo
import speec as sp
import time
import speech_recognition as sr #importamos o modúlo

def menu(quant):
    if quant == 1:
        return """
        ██████╗ ███████╗███████╗███████╗██╗     ██████╗ 
        ██╔══██╗██╔════╝██╔════╝██╔════╝██║     ██╔══██╗
        ██║  ██║█████╗  █████╗  █████╗  ██║     ██████╔╝
        ██║  ██║██╔══╝  ██╔══╝  ██╔══╝  ██║     ██╔═══╝ 
        ██████╔╝███████╗██║     ███████╗███████╗██║     
        ╚═════╝ ╚══════╝╚═╝     ╚══════╝╚══════╝╚═╝"""
    if quant == 2:
        return """
            | 0 |         Exit        | 0 |     | 4 |     View E-mail     | 4 |     | 8 |     Credits    | 8 |
            | 1 |     Search Google   | 1 |     | 5 |      Instagram      | 5 |     | 9 |     Opction    | 9 |
            | 2 |     Search Yahoo    | 2 |     | 6 |     Enter Sites     | 6 |
            | 3 |     Send E-mail     | 3 |     | 7 |     Read Archive    | 7 |
            """
    if quant == 3:
        return """
        ██████╗ ███████╗███████╗███████╗██╗     ██████╗ 
        ██╔══██╗██╔════╝██╔════╝██╔════╝██║     ██╔══██╗
        ██║  ██║█████╗  █████╗  █████╗  ██║     ██████╔╝
        ██║  ██║██╔══╝  ██╔══╝  ██╔══╝  ██║     ██╔═══╝ 
        ██████╔╝███████╗██║     ███████╗███████╗██║     
        ╚═════╝ ╚══════╝╚═╝     ╚══════╝╚══════╝╚═╝
        
            | 0 |         Exit        | 0 |     | 4 |     View E-mail     | 4 |     | 8 |     Credits    | 8 |
            | 1 |     Search Google   | 1 |     | 5 |      Instagram      | 5 |     | 9 |     Octions    | 9 |
            | 2 |     Search Yahoo    | 2 |     | 6 |     Enter Sites     | 6 |
            | 3 |     Send E-mail     | 3 |     | 7 |     Read Archive    | 7 |"""
    if quant == 4:
        return """
##      ## #### ##    ## #### ########  ######## ########  ####    ###    
##  ##  ##  ##  ##   ##   ##  ##     ## ##       ##     ##  ##    ## ##   
##  ##  ##  ##  ##  ##    ##  ##     ## ##       ##     ##  ##   ##   ##  
##  ##  ##  ##  #####     ##  ########  ######   ##     ##  ##  ##     ## 
##  ##  ##  ##  ##  ##    ##  ##        ##       ##     ##  ##  ######### 
##  ##  ##  ##  ##   ##   ##  ##        ##       ##     ##  ##  ##     ## 
 ###  ###  #### ##    ## #### ##        ######## ########  #### ##     ## """