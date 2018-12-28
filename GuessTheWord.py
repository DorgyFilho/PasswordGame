#GUESS THE WORD

import random
from tkinter import *

Words = [('Snake Language','PYTHON'), ('Opposite to Dark' ,'LIGHT'), ('Main Character of Final Fantasy XIII Game', 'LIGHTNING'),
('Wrestler Known as Deadman', 'The Undertaker')]
SortedWord = random.choice(Words)

def Check():
    global Words
    global SortedWord
    Ask = SortedWord[0]
    TipRes['text'] = Ask

def Guess():
    global SortedWord
    Answer = SortedWord[1]
    Input = Word.get().upper()
    if Input == Answer:
        msg = 'You Win!'
        AnsRes['text'] = Answer
        LblRes['text'] = msg
    else:
        msg = 'You Lose. The Right Answer is {}'.format(Answer)
        AnsRes['text'] = Answer
        LblRes['text'] = msg
        Check()

Game = Tk()
Game.title('Guess The Word --- Concept By Dorgival Filho')
Game.geometry('480x360')

LblTitle = Label(Game, text='Welcome to the Guess The Word Game!!!')
LblTitle.pack()

AnsDir = Label(Game, text='Click here to see a tip')
AnsDir.pack()

BtnVerify = Button(Game, text='Verify Tip', fg='black', bg='white', command=Check)
BtnVerify.pack()

TipRes = Label(Game, text='Tip')
TipRes.pack()

LetDir = Label(Game, text='Input Your Answer Here')
LetDir.pack()

Word = Entry(Game, width=20, bg='white', fg='black')
Word.pack()

BtnResult = Button(Game, text='Result', fg='black', bg='white', command=Guess)
BtnResult.pack()

AnsRes = Label(Game, text='Answer')
AnsRes.pack()

LblRes = Label(Game, text='Good Luck, Player!')
LblRes.pack()

Game.mainloop()  