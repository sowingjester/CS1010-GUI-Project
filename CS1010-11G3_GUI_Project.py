'''

CS1010-11 Group 3 GUI Project
'Blackjack Casino simulator'
Group Members:
    Rigo Castro
    Alan Garrido
    Kenai Lozada
    Connor Moy

'''

import tkinter as tk
from random import randint

mWin = tk.Tk() # Main Window
mWin.geometry('500x500') # Size of the screen might need to change
mWin.title("'Blackjack Casino simulator'") # Needs a different title
mWin.configure(bg='#243b5e') # theme not important rn, current colour temporary

menuFrm = tk.Frame(mWin, bg='#22552d') # Menu Frame
bljFrm = tk.Frame(mWin, bg='#0c3b16') # Blackjack game frame

cardList = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] # List of all usable cards
cT = 0 # total of cards added up
cards = [] # list with cards given

def cardSel():
    global cT
    global cards
    
    cNum = randint(0, 12) # Card number value
    cFace = cardList[cNum] # gets face from list
    cards += [cFace] # Adds new cards to list
    
    if cFace.isnumeric(): # If its a number card it just uses that value
        cT += int(cFace)
    elif cFace == 'J' or cFace == 'Q' or cFace == 'K': # If its a face card it gives it the value 10
        cT += 10
    elif cFace == 'A': # Ace can be 1 or 11 (...but its not properly implimented rn)
        if cT < 11:
            cT += 11
        else:
            cT += 1
    
    if cT > 21: # If the cards add up to more than 21 you lose
        totalLbl.config(text='Bust!')
        cardLbl.config(text=('Cards:', cards))
        winLbl.config(text='You Lost.')
    else:
        totalLbl.config(text=f'Total: {cT}')
        cardLbl.config(text=('Cards:', cards))
        if cT == 21: # If the cards add up to 21 its a win
            winLbl.config(text='You Win!')

tLbl = tk.Label(menuFrm, text="'Blackjack Casino Sim!'", bg='#22552d', fg='White') # Title label
helpLbl = tk.Label(menuFrm, text='To win get as close to 21 without going over.', bg='#22552d', fg='White')
startBtn = tk.Button(menuFrm, text='Start', bg='#22552d', activebackground='#0c3b16', fg='White', activeforeground='White')

hitBtn = tk.Button(bljFrm, text='Hit', command=cardSel, bg='#0c3b16', activebackground='#22552d', fg='White') # Hit button (currently doesnt work properly)
totalLbl = tk.Label(bljFrm, text='Total: 0', bg='#0c3b16', fg='White') # Label that displays card total
cardLbl = tk.Label(bljFrm, text='Cards:', bg='#0c3b16', fg='White') # Displays cards
winLbl = tk.Label(bljFrm, text='', bg='#0c3b16', fg='White') # Win/Lose Label


# Label and button placements (Visuals are all temporary right now)
menuFrm.place(x=0, y=0, relheight=0.98, relwidth=0.98)
tLbl.place(x=0, y=0) 
helpLbl.place(x=0, y=50)
startBtn.place(x=0, y=25)

bljFrm.place(x=0, y=100, relheight=0.25, relwidth=0.25)
hitBtn.place(x=0, y=0)
totalLbl.place(x=0, y=50)
cardLbl.place(x=50, y=50)
winLbl.place(x=50, y=0)



mWin.mainloop()


''' 
To do (feel free to add stuff):
* Make it look good (important):
    * Fix Placements
    * Fix frames and positions
* Make it so you can play multiple rounds
* Fix Button giving infinite cards
* Add dealer to play against
* Add bet mechanic
* Fix Ace not turning to 1 if over 21
* Fix you can get more than 4 of the same card
* Change colours
* 
* 
* 

Other stuff (maybe):
* Add Slots 
* Add Crash 
* Add Poker?
* 
*
*

'''