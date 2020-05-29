# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:37:19 2020

@author: khushboo
"""

from tkinter import *

def callback(r,c):
    global player
    print(player)
    
    
    if player=='x' and states[r][c]==0 and stop_game==False:
        print('x')
        print(b[r][c])
        b[r][c].configure(text='x',fg='blue',bg='white')        
        states[r][c]='1'
        player='0'

    if player=='0' and states[r][c]==0 and stop_game==False:
        print('0')
        b[r][c].configure(text='0',fg='orange',bg='black')        
        states[r][c]='2'
        player='x'
        
    check_for_winner()
    
def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].config(bg='grey')
            b[i][1].config(bg='grey')
            b[i][2].config(bg='grey')
            stop_game=True

    for i in range(3):
        if states[0][i]==states[1][i]==states[2][i]!=0:
            b[0][i].config(bg='grey')
            b[1][i].config(bg='grey')
            b[2][i].config(bg='grey')
            stop_game=True

        if states[0][0]==states[1][1]==states[2][2]!=0:
            b[0][0].config(bg='grey')
            b[1][1].config(bg='grey')
            b[2][2].config(bg='grey')
            stop_game=True

        if states[0][0]==states[1][1]==states[2][2]!=0:
            b[2][0].config(bg='grey')
            b[1][1].config(bg='grey')
            b[0][2].config(bg='grey')
            stop_game=True
        

root=Tk()
root.title("TIC TAC TOE")

b=[[0,0,0], [0,0,0], [0,0,0]]

states=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        print(b[i][j])
        b[i][j]=Button(root,font=('Arial',60),width=4,bg='powder blue',command= lambda r=i,c=j: callback(r,c))

        b[i][j].grid(row=i,column=j)
        print(b[i][j])
        
player='x'
stop_game=False


mainloop()

















        