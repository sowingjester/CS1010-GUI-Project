#CS1010-GUI-Project

#Experimental Branch

#Feel free to break it as much as you want 

'
dT = 0 # Dealer's Total

chips = tk.IntVar # Total money player put in

def gC(): # gets 1 card and puts it into the cards list
    global cards
    global cT

    cNum = randint(0, 12) # Card number value
    cFace = cardList[cNum] # gets face from list
    cards += [cFace] # Adds new cards to list

    if cFace.isnumeric(): # If its a number card it just uses that value
        cT += int(cFace)
    elif cFace == 'J' or cFace == 'Q' or cFace == 'K': # If its a face card it gives it the value 10
         cT += 10
    elif cFace == 'A': # Ace can be 1 or 11 (currently doesnt work properly)
        if cT < 11:
            cT += 11
        else:
            cT += 1

def dlrCard(): # Gives dealer 1 card and puts in hand
    global dCards
    global dT

    cNum = randint(0, 12)
    cFace = cardList[cNum]
    dCards += [cFace] # Adds cards to dealer's hand

    if cFace.isnumeric():
        dT += int(cFace)
    elif cFace == 'J' or cFace == 'Q' or cFace == 'K':
        dT += 10
    elif cFace == 'A':
        if dT < 11:
            dT += 11
        else:
            dT += 1

def stand(): # Ends Round
    global cT
    global dT
    global bet
    global chips

    dealerPlay()
    if cT > 21: # If the cards add up to more than 21 you lose
        totalLbl.config(text='Bust!')
        cardLbl.config(text=(f'Cards: {cards}'))
        winLbl.config(text='You Lost.')
        hitBtn.config(state=tk.DISABLED)
        dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
        dTotalLbl.config(text=(f"Dealer's Total: {dT}"))    
    elif dT == 0: # If the dealer busted you win
        totalLbl.config(text=(f'Total: {cT}'))
        cardLbl.config(text=(f'Cards: {cards}'))
        winLbl.config(text='You Win!')
        hitBtn.config(state=tk.DISABLED)
        dTotalLbl.config(text="Dealer's Total: Bust!")
        chips += bet*2
        monLbl.config(text=(f"'Chips': {chips}"))
    elif cT < dT: # If the dealer has more you lose
        totalLbl.config(text=(f'Total: {cT}'))
        cardLbl.config(text=(f'Cards: {cards}'))
        winLbl.config(text='You Lost.')
        hitBtn.config(state=tk.DISABLED)
        dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
        dTotalLbl.config(text=(f"Dealer's Total: {dT}"))
    else:
        totalLbl.config(text=(f'Total: {cT}'))
        cardLbl.config(text=(f'Cards: {cards}'))
        dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
        dTotalLbl.config(text=(f"Dealer's Total: {dT}"))
        hitBtn.config(state=tk.DISABLED)
        if cT == 21: # If the cards add up to 21 its a win
            winLbl.config(text='You Win!')
            chips += bet*2
            monLbl.config(text=(f"'Chips': {chips}"))
        elif cT > dT: # If your card's are more than the dealer you win
            winLbl.config(text='You Win!')
            chips += bet*2
            monLbl.config(text=(f"'Chips': {chips}"))
        elif cT == dT:
            winLbl.config(text="It's a tie!")
            chips += bet
            monLbl.config(text=(f"'Chips': {chips}"))

def hit(): # Gives dealer and player 2 cards then 1 card to player
    global cards
    global cT
    global chips
    global bet

    if len(cards) == 0: # Gives 2 Cards first hit and takes bet from money
        for i in range(2):
            dlrCard()
            gC()
        bet = int(betBox.get())
        chips -= bet # Takes bet from chips at the start of round
        monLbl.config(text=(f"'Chips': {chips}"))
    else: # Only gives 1 card after first hit
        gC()
  
    cardLbl.config(text=(f"Cards: {cards}")) # Displays cards (currently ugly)
    totalLbl.config(text=f'Total: {cT}')   # Displays cards added up total
    dCardsLbl.config(text=(f"Dealer's Cards: ['{dCards[0]}', '*']"))

    if cT > 21: # If cards go over 21, end round
        hitBtn.config(state=tk.DISABLED)
        stand()
    
    

def dealerPlay(): # Dealer draws cards after player stands
    global cT
    global dT
    global dCards

    while cT > dT: # If you have more than the dealer it'll try to get more than you
        if cT >= 21:
            dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
            break
        elif dT >= cT: # If it has more it'll stop
            dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
            break
        else:
            dlrCard()
            dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))

        if dT > 21: # If the dealer busts you win
            dT = 0
            dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
            break

def rstBlj(): # Resets game
    global cT
    global cards
    global dCards
    global dT

    cT = 0
    cards = []

    dCards = []
    dT = 0

    totalLbl.config(text='Total:')
    cardLbl.config(text='Cards:')
    winLbl.config(text='')
    dCardsLbl.config(text="Dealer's Cards:")
    hitBtn.config(state=tk.NORMAL)
    dTotalLbl.config(text="Dealer's Total:")

def placeGame(): # Places Blackjack frame
    global chips

    bljFrm.place(x=0, y=100, relwidth=1, relheight=1)
    startBtn.config(state=tk.DISABLED)
    helpLbl.config(text='To win get as close to 21 without going over.')

    chips = int(monBox.get())
    monLbl.config(text=(f"'Chips': {chips}"))


tLbl = tk.Label(menuFrm, text="'Blackjack Casino Sim!'", bg='#22552d', fg='White') # Title label
helpLbl = tk.Label(menuFrm, text="To win get as close to 21 without going over.\nEnter 'Chips' below", bg='#22552d', fg='White') # Label explains rules
startBtn = tk.Button(menuFrm, text='Start', bg='#22552d', activebackground='#0c3b16', fg='White', activeforeground='White', command=placeGame) # Button starts blackjack (or other games in the future)
monBox = tk.Entry(menuFrm, bg='#0c3b16', fg='White') # Entry box for chips

hitBtn = tk.Button(bljFrm, text='Hit', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=hit) # Hit button
totalLbl = tk.Label(bljFrm, text='Total: 0', bg='#0c3b16', fg='White') # Label that displays card total
cardLbl = tk.Label(bljFrm, text='Cards:', bg='#0c3b16', fg='White') # Displays cards
winLbl = tk.Label(bljFrm, text='', bg='#0c3b16', fg='White') # Win/Lose Label
standBtn = tk.Button(bljFrm, text='Stand', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=stand) # Stand Button
rstBtn = tk.Button(bljFrm, text='Restart', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=rstBlj) # Restart Button
dCardsLbl = tk.Label(bljFrm, text="Dealer's Cards:", bg='#0c3b16', fg='White') # Dealer's Cards
dTotalLbl = tk.Label(bljFrm, text="Dealer's Total:", bg='#0c3b16', fg='White') # Dealer's Total
betBox = tk.Entry(bljFrm, bg='#22552d', fg='White') # Bet entry box
betLbl = tk.Label(bljFrm, text='Bet:', bg='#0c3b16', fg='White')
monLbl = tk.Label(bljFrm, text="'Chips':", bg='#0c3b16', fg='White')

# Label and button placements (Visuals are all temporary right now)
menuFrm.place(x=0, y=0, relwidth=1, relheight=1)
tLbl.place(x=150, y=20, anchor='c') 
helpLbl.place(x=150, y=80, anchor='c')
startBtn.place(x=150, y=50, anchor='c')
monBox.place(x=150, y=110, anchor='c')

hitBtn.place(x=20, y=120)
totalLbl.place(x=170, y=30)
cardLbl.place(x=20, y=30)
winLbl.place(x=70, y=0)
standBtn.place(x=50, y=120)
rstBtn.place(x=95, y=120)
dCardsLbl.place(x=20, y=60)
dTotalLbl.place(x=20, y=90)
betLbl.place(x=20, y=170)
betBox.place(x=50, y=170)
monLbl.place(x=140, y=170)



def placeGame(): 
    global chips

    entered_chips = monBox.get()
    if entered_chips.isdigit():  
        chips = int(entered_chips)
        monLbl.config(text=(f"'Chips': {chips}"))
        bljFrm.place(x=0, y=100, relwidth=1, relheight=1)
        startBtn.config(state=tk.DISABLED)
        helpLbl.config(text='To win, get as close to 21 without going over.')

    else:
        messagebox.showerror("Invalid Input", "Please enter a valid non-negative integer for chips.")


def hit():
    global cards
    global cT
    global chips
    global bet

    if len(cards) == 0: 
        for i in range(2):
            dlrCard()
            gC()
        entered_bet = betBox.get()
        if entered_bet.isdigit() and int(entered_bet) <= chips:  # Check if the entered bet is a non-negative integer and less than or equal to available chips
            bet = int(entered_bet)
            chips -= bet 
            monLbl.config(text=(f"'Chips': {chips}"))
        else:
            messagebox.showerror("Invalid Bet", "Please enter a valid non-negative integer for the bet and ensure it is not more than your available chips.")
            return
    else:
        gC()

    cardLbl.config(text=(f"Cards: {cards}")) 
    totalLbl.config(text=f'Total: {cT}')   
    dCardsLbl.config(text=(f"Dealer's Cards: ['{dCards[0]}', '*']"))

    if cT > 21: 
        hitBtn.config(state=tk.DISABLED)
        stand()
    


mWin.mainloop()


''' 

To do (feel free to add stuff):
* Fix really bad bugs
* Boot the player to menu if they run out of chips
* Double down
* Two hands
* Multiplayer
* 
* 
* 

Make it look good (important):
* Change the title
* Fix Placements
* Fix frames and positions
* Change colours
* 
* 
* 

Bugs(If you find any put here):
* (Really bad) If either boxes are empty it crashes
* (Really bad) If a string is entered in boxes it crashes
* You can bet more than what you have
* You can go into the negatives with chips
* If player and dealer have 21 player always wins (should be tie)
* If you have an Ace and you hit, and go over 21, it wont turn to 1
* You can get more than 4 of the same card 
* Dealer doesn't stop if it's close to busting (It will try it's hardest to beat the player at least)
*
* 
* 

'''

