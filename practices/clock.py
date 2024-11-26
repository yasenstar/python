#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:58:57 2020

@author: yasen
"""
from tkinter import *
from math import *
import time

def showTime():
    time1 = '12-00-00'
    time2 = time.strftime('%H-%M-%S')
    t = time2.split('-')
    if time2 != time1:
        time1 = time2
    for i in c.find_withtag('xiaoqi'):
        c.delete(i)
        draw(t)
        c.create_test((246,475), text=time2, tags='xiaoqi', anchor=N)
        c.after(500,showTime())

def win():
    global c
    root = Tk()
    c = Canvas(root, bg='white', width=500, height=500)
    c.pack()
    t = time.strftime("%H-%M-%S")
    t = t.split('-')
    for i in range(1,61):
        x1 = 250 + 200 * cos(pi*i/30)
        y1 = 250 + 200 * sin(pi*i/30)
        x2 = 250 + 185 * cos(pi*i/30)
        y2 = 250 + 185 * sin(pi*i/30)
        if i % 5 == 0:
            x2 = 250 + 175 * cos(pi*i/30)
            y2 = 250 + 175 * sin(pi*i/30)
            c.create_line(x1, y1, x2, y2, fill='red', width=3)
        else:
            c.create_line(x1, y2, x2, y2, fill='black', width=2)
        showTime()
        c.create_oval(50, 50, 450, 450, outline='blue', width=2)
        c.create_oval(240, 240, 260, 260, fill='red', outline='red')
        c.create_oval(243, 243, 257, 257, fill='green', outline='green')
    root.mainloop()

def draw(t):
    S1 = 250 + 165*cos(pi*(int(t[2]) + 45) / 30)
    S2 = 250 + 165*sin(pi*(int(t[2]) + 45) / 30)
    c.create_line(S1, S2, 250, 250, fill='red', width=5, arrow=FIRST, tags='xiaoqi')
    c.create_oval(243, 243, 257, 257, fill='green', outline='green')
    M1 = 250 + 135*cos(pi*(int(t[1]) + float(t[2])/60 + 45) / 30)
    M2 = 250 + 135*sin(pi*(int(t[1]) + float(t[2])/60 + 45) / 30)
    c.create_line(M1, M2, 250, 250, fill='green', width=5, arrow=FIRST, tags='xiaoqi')
    c.create_oval(247, 247, 253, 253, fill='black', outline='black')
    H1 = 250 + 95*cos(pi*(int(t[0]) + float(t[1])/60 + 9) / 6)
    H2 = 250 + 95*sin(pi*(int(t[0]) + float(t[1])/60 + 9) / 6)
    c.create_line(H1, H2, 250, 250, fill='black', width=7, arrow=FIRST, tags='xiaoqi')

if __name__ == '__main__':
    win()