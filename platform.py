import pygame
from constants import *

class Platform(pygame.sprite.Sprite):
	
	def __init__(self, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.width = width
		self.height = height
		
		# Init left side of platform
		self.image = pygame.Surface([width, height])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
