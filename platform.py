import pygame
from constants import *

# Length of block
IMAGE_LEN = 35

class Platform(pygame.sprite.Sprite):
	
	def __init__(self, width, height):
		# Call parent constructor: Sprite
		pygame.sprite.Sprite.__init__(self)
		
		# Set platform attributes
		self.width = width
		self.height = height
		self.image = pygame.Surface([width, height]).convert()
		
		# Build the length of the platform with the stone blocks
		for x in range(0, width, IMAGE_LEN):
			self.image.blit(pygame.image.load("stone-test.png"), (x,0), (0,0,width,height))
			
		# Set the colorkey so the background is transparent
		self.image.set_colorkey(WHITE)
		
		# Get the rect of the platform image
		self.rect = self.image.get_rect()
