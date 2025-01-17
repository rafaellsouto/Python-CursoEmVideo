import pygame
pygame.init()

pygame.mixer.music.load('Johnny Cash - Hurt.mp3')
pygame.mixer.music.play()
pygame.event.wait()