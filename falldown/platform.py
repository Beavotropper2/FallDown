import pygame
from constants import *

IMAGE_LEN = 35

class Platform(pygame.sprite.Sprite):
	
	def __init__(self, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.width = width
		self.height = height
		
		# Init left side of platform
		self.image = pygame.Surface([width, height]).convert()
		for x in range(0, width, IMAGE_LEN):
			self.image.blit(pygame.image.load("stone-test.png"), (x,0), (0,0,width,height))
		self.image.set_colorkey(WHITE)
		#self.image.fill(GREEN)
		self.rect = self.image.get_rect()
