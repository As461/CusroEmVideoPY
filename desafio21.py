'''
Modulo para jogos, serve para importar, musica, videos e outros..

'''


import pygame
pygame.init()
pygame.mixer.music.load('ex.21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
