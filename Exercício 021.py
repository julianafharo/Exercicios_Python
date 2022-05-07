#Tocando um MP3: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.mixer.music.set_volume(0.5) #0 a 1, float, decimal
pygame.event.wait()
