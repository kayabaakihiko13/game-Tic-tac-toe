import pygame as pg
import numpy as np
from aset import *

# papan bermain

WINDOW.fill(BLACK)

def garis():
    # vertical
    pg.draw.line(WINDOW,LINE_COLOR,(0,SIZE_SQUARE),(HEIGHT,SIZE_SQUARE),LINE_WIDTH)
    # make horizontal 1
    pg.draw.line(WINDOW,LINE_COLOR,(0,SIZE_SQUARE+200),(WIDTH,SIZE_SQUARE+200),LINE_WIDTH)

    # vertical 
    pg.draw.line(WINDOW,LINE_COLOR,(SIZE_SQUARE,0),(SIZE_SQUARE,HEIGHT),LINE_WIDTH)
    pg.draw.line(WINDOW,LINE_COLOR,(SIZE_SQUARE+200,0),(SIZE_SQUARE+200,HEIGHT),LINE_WIDTH)

def draw_figure():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if BOARD[row][col]==1:
                pg.draw.circle(WINDOW,CIRCLE_COLOR,(int(col*200+200/2),int(row*200+100)),radius=CIRCLE_RADIUS,width=CIRCLE_WIDTH)
            elif BOARD[row][col]==2:
                pg.draw.line(WINDOW,CROOS_COLOR,(col*200+SPACE,row*200+200-SPACE),(col*200+200-SPACE,row*200+SPACE),CROSS_WIDTH)
                pg.draw.line(WINDOW,CROOS_COLOR,(col*200+SPACE,row*200+SPACE),(col*200+200-SPACE,row*200+200-SPACE),CROSS_WIDTH)


def mark_kontak(baris,kolom,player):
    BOARD[baris][kolom]=player

def kotak_tersedia(baris,kolom):
    return BOARD[baris][kolom]==0

def is_kotak_penuh():
    for baris in range(BOARD_ROWS):
        for kolom in range(BOARD_COLS):
            if BOARD[baris][kolom]==0:
                return False
    return True
    
def check_winner(player):
    for kolom in range(BOARD_COLS):
        if BOARD[0][kolom]==player and BOARD[1][kolom]==player and BOARD[2][kolom]==player:
            draw_vertical_win_line(kolom,player)
            return True
    #  for horizontal win check
    for row in range(BOARD_ROWS):
        if BOARD[row][0]==player and BOARD[row][1]==player and BOARD[row][2]==player:
            draw_horizontal_win_line(row,player)
            return True
    # asc diagonal win check 
    if BOARD[2][0] ==player and BOARD[1][1] ==player and BOARD[0][2]==player:
        draw_asc_diagonal(player)
        return True
    # desc diagonal win check
    if BOARD[0][0] == player and BOARD[1][1] ==player and BOARD[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False

def garis_vertikal_winner(kolom,player):
    posX=kolom*200+100
    if player == 1:
        color=RED
    if player ==2:
        color = RED
    pg.draw.line(WINDOW,color,(posX,15),(posX,HEIGHT-15),15)

def draw_horizontal_win_line(row,player):
    posY=row *200+100

    if player ==1:
        color=RED
    elif player ==2:
        color=RED
    pg.draw.line(WINDOW,color,(15,posY),(HEIGHT-15,posY),15)  
def draw_vertical_win_line(col,player):
    posX=col *200+100

    if player ==1:
        color=RED
    elif player ==2:
        color=RED
    pg.draw.line(WINDOW,color,(posX,15),(posX,HEIGHT-15),15)


def draw_asc_diagonal(player):
    if player==1:
        color=RED
    elif player ==2:
        color=RED
    pg.draw.line(WINDOW,color,(15,HEIGHT-15),(WIDTH-15,15),15)

def draw_desc_diagonal(player):
    if player==1:
        color=RED
    elif player ==2:
        color=RED
    pg.draw.line(WINDOW,color,(15,15),(WIDTH-15,HEIGHT-15),15)


def restart():
    WINDOW.fill(BLACK)
    garis()
    player=1

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            BOARD[row][col]=0




