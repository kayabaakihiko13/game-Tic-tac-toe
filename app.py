# import pakage
import pygame as pg
import numpy as np
import sys
from aset import *
from display import *


# init pygame
pg.init()

# make windows

pg.display.set_caption("Just Tic Tac Toe")
garis()
player=1
game_over=False


# main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type ==pg.MOUSEBUTTONDOWN and not game_over:
            X=event.pos[0]
            Y=event.pos[1]
            klik_baris=int(Y//200)
            klik_kolom=int(X//200)
            if kotak_tersedia(klik_baris,klik_kolom):
                mark_kontak(klik_baris,klik_kolom,player)
                if check_winner(player):
                    game_over=True
                player = player % 2 + 1
                draw_figure()
        if event.type==pg.KEYDOWN :
            if event.key==pg.K_r:
                restart()
                game_over=False
    pg.display.update() 



