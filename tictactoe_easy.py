import tkinter as tk
from tkinter import messagebox
from functools import partial
import tkinter.font as tkFont
import numpy as np
import random
import time
import sys
import os
player = 'X'
board = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
changeFlag = True
window = tk.Tk()
window.title("Tic-Tac_Toe")
#window.geometry("230x280")

def changeTurn():
    global player
    global turn
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
    turn = tk.Label(window, text="Turn: {}".format(player))
    turn.grid(row=4,columnspan=2)

def restart():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
def WinnerCheck():
    winFlag = False
    canvas = tk.Canvas(window)
    canvas.create_line(15, 25, 200, 25)
    #checking horizontally
    if board[0, 0] == board[0, 1] and board[0, 0] == board[0, 2]:
        winFlag=True
    if board[1, 0] == board[1, 1] and board[1, 0] == board[1, 2]:
        winFlag=True
    if board[2, 0] == board[2, 1] and board[2, 0] == board[2, 2]:
        winFlag=True
    #checking vertically
    if board[0, 0] == board[1, 0] and board[0, 0] == board[2, 0]:
        winFlag=True
    if board[0, 1] == board[1, 1] and board[0, 1] == board[2, 1]:
        winFlag=True
    if board[0, 2] == board[1, 2] and board[0, 2] == board[2, 2]:
        winFlag = True
    #checking diagonally
    if board[0, 0] == board[1, 1] and board[0, 0] == board[2, 2]:
            winFlag = True
    if board[0, 2] == board[1, 1] and board[0, 2] == board[2, 0]:
            winFlag = True
    print(board)
    if winFlag:
        global changeFlag
        changeFlag = False
        global turn
        turn.configure(text="Player {} won".format(player))
        replay = tk.Button(window,text="Play Again", command=restart, height=1, width=20,fg="green",activebackground='red')
        replay.grid(row=5, column=0,columnspan=3)



def aiPlay():
    while True:
        randRow = random.randrange(0,3)
        randCol = random.randrange(0,3)
        if board[randRow, randCol] != 'X' and board[randRow, randCol] != 'O':
            fontStyle = tkFont.Font(family="Lucida Grande", size=60)
            label = tk.Label(window, text=player, font=fontStyle)
            label.grid(row=randRow, column=randCol)
            board[randRow, randCol] = player
            WinnerCheck()
            if changeFlag:
                changeTurn()
            break

def button_clicked(r, c):
    fontStyle = tkFont.Font(family="Lucida Grande", size=60)
    label = tk.Label(window, text=player, font=fontStyle)
    label.grid(row=r, column=c)
    board[r, c] = player
    WinnerCheck()
    if changeFlag:
        changeTurn()
    if player=='O':
        aiPlay()

b00 = tk.Button(window, command=partial(button_clicked, 0, 0), height=5, width=8)
b01 = tk.Button(window, command=partial(button_clicked, 0, 1), height=5, width=8)
b02 = tk.Button(window, command=partial(button_clicked, 0, 2), height=5, width=8)
b01.flash()
b00.grid(row=0, column=0)
b01.grid(row=0, column=1)
b02.grid(row=0, column=2)
b10 = tk.Button(window, command=partial(button_clicked, 1, 0), height=5, width=8)
b11 = tk.Button(window, command=partial(button_clicked, 1, 1), height=5, width=8)
b12 = tk.Button(window, command=partial(button_clicked, 1, 2), height=5, width=8)
b10.grid(row=1, column=0)
b11.grid(row=1, column=1)
b12.grid(row=1, column=2)
b20 = tk.Button(window, command=partial(button_clicked, 2, 0), height=5, width=8)
b21 = tk.Button(window, command=partial(button_clicked, 2, 1), height=5, width=8)
b22 = tk.Button(window, command=partial(button_clicked, 2, 2), height=5, width=8)
b20.grid(row=2, column=0)
b21.grid(row=2, column=1)
b22.grid(row=2, column=2)
turn = tk.Label(window, text="Turn: {}".format(player))
turn.grid(row=4,columnspan=2)

window.mainloop()
