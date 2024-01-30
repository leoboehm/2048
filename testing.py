import pygame

pygame.init()
 
surface = pygame.display.set_mode((400,500),0,32)
pygame.display.set_caption("2048 Game by DataFlair")
 
font = pygame.font.SysFont("monospace",40)
fontofscore = pygame.font.SysFont("monospace",30)
 
tileofmatrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
undomatrix = []