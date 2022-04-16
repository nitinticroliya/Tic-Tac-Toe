from tkinter import *
import tkinter.messagebox
import random

tk = Tk()
tk.title("Tic-Tac-Toe")


def isHumanIsWinner():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text '] == 'X'):
        tkinter.messagebox.showinfo("Player Human", "Human is Winner !!!")
        exit()


def isItTie():
    if ((button1['text'] == 'X' or button1['text'] == 'O') and
            (button2['text'] == 'X' or button2['text'] == 'O') and
            (button3['text'] == 'X' or button3['text'] == 'O') and
            (button4['text'] == 'X' or button4['text'] == 'O') and
            (button5['text'] == 'X' or button5['text'] == 'O') and
            (button6['text'] == 'X' or button6['text'] == 'O') and
            (button7['text'] == 'X' or button7['text'] == 'O') and
            (button8['text'] == 'X' or button8['text'] == 'O') and
            (button9['text'] == 'X' or button9['text'] == 'O')):
        tkinter.messagebox.showinfo("Match Draw", "No one is Winner !!!")
        exit()


def isBotIsWinner():
    if (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
            button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
            button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
            button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
            button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
            button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
            button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
            button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        tkinter.messagebox.showinfo("Player Bot", 'Bot is Winner !!!!')
        exit()


def botTurn():
    for x, y, z in win_combo:
        if x['text'] == "O" and y['text'] == "O" and z['text'] == " ":
            return z

        if z['text'] == "O" and y['text'] == "O" and x['text'] == " ":
            return x

        if x['text'] == "O" and z['text'] == "O" and y['text'] == " ":
            return y

    for x, y, z in win_combo:
        if x['text'] == "X" and y['text'] == "X" and z['text'] == " ":
            return z

        if z['text'] == "X" and y['text'] == "X" and x['text'] == " ":
            return x

        if z['text'] == "X" and x['text'] == "X" and y['text'] == " ":
            return y

    if bot_move == 0:
        if button5['text'] == " ":
            return button5

    if bot_move == 0:
        if button5['text'] == "X":
            return random.choice([button1, button3, button7, button9])

    if bot_move == 1:
        if button1['text'] == button9['text'] == "X" \
                or button3['text'] == button7['text'] == "X":
            return random.choice([button2, button4, button6, button8])

    else:
        to_go = []
        for i in index:
            if i['text'] == " ":
                to_go.append(i)
        return random.choice(to_go)


def putMarker(buttons):
    if buttons["text"] == " ":
        buttons["text"] = "O"


def ttt(buttons):
    if buttons["text"] == " ":
        buttons["text"] = "X"
    isHumanIsWinner()
    isItTie()
    botMarker = botTurn()
    putMarker(botMarker)
    isBotIsWinner()
    isItTie()


buttons = StringVar()

button1 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white',
                 height=4, width=8, command=lambda: ttt(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white',
                 height=4, width=8, command=lambda: ttt(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

index = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
win_combo = [[button1, button2, button3], [button4, button5, button6],
             [button7, button8, button9], [button1, button4, button7],
             [button2, button5, button8], [button3, button6, button9],
             [button1, button5, button9], [button3, button5, button7]]
bot_move = 0

tk.mainloop()
