import pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('Roddy Ricch - The Box.mp3')
pygame.mixer.music.play()
pygame.event.wait()
