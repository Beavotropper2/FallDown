import pygame
from constants import *

class Player(pygame.sprite.Sprite):

	# --- Player Attributes
	# Player speed vectors
	change_x = 0
	change_y = 0
	# Player score
	score = 0
	
	# List of sprites/walls
	game_map = None
	
	# Set alive
	alive = True

	def __init__(self):
		# Call parent constructor
		pygame.sprite.Sprite.__init__(self)

		# Create RED square
		self.width = 20
		self.height = 20
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(RED)

		# Rect reference to image
		self.rect = self.image.get_rect()

	# Move player
	def update(self):
		# Calculate gravity
		self.calc_grav()
		
		# Check horizontal collision
		self.rect.x += self.change_x
		self.check_x_coll()

		# Check vertical collision
		self.rect.y += self.change_y
		self.check_y_coll()
				
		# Check off left screen
		if self.rect.left < 0:
			self.rect.left = 0
		# Check off right screen
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		
		# Check if player has lost
		#print(str(self.rect.x) + "," + str(self.rect.y))
		if self.rect.top <= 0:
			self.alive = False
			
	def check_x_coll(self):
		plat_hit_list = pygame.sprite.spritecollide(self, self.game_map.platform_list, False)
		for block in plat_hit_list:
			if self.change_x > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom
			self.change_x = 0
	
	def check_y_coll(self):
		plat_hit_list = pygame.sprite.spritecollide(self, self.game_map.platform_list, False)
		for block in plat_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom
			self.change_y = 0

	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 15
		else:
			self.change_y += 0.35

	def move_left(self):
		self.change_x = -MOVE_SPEED

	def move_right(self):
		self.change_x = MOVE_SPEED
	
	def stop(self):
		self.change_x = 0
	
