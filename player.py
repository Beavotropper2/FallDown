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

	# Initialize all player attributes
	def __init__(self):
		# Call parent constructor
		pygame.sprite.Sprite.__init__(self)

		# Create player
		self.width = 25
		self.height = 33
		self.image = pygame.Surface([self.width, self.height]).convert()
		self.image.blit(pygame.image.load("bomb.png"), (0,0), (0,0,self.width,self.height))
		self.image.set_colorkey(BLACK)

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
				
		# Check if player off left side of screen
		if self.rect.left < 0:
			self.rect.left = 0
			
		# Check if player off right side of screen
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		
		# Check if player has lost
		if self.rect.top <= 2:
			self.alive = False
			self.explode()
			
	# Check horizontal collisions
	def check_x_coll(self):
		plat_hit_list = pygame.sprite.spritecollide(self, self.game_map.platform_list, False)
		for block in plat_hit_list:
			if self.change_x > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom
			self.change_x = 0
	
	# Check vertical collisions
	def check_y_coll(self):
		plat_hit_list = pygame.sprite.spritecollide(self, self.game_map.platform_list, False)
		for block in plat_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom
			self.change_y = 0
	# Make player explode
	def explode(self):
		self.width = 50
		self.height = 47
		self.image = pygame.Surface([self.width, self.height]).convert()
		self.image.blit(pygame.image.load("explosion.png"), (0,0), (0,0,self.width,self.height))
		self.image.set_colorkey(BLACK)

	# Calculate gravity of player
	def calc_grav(self):
		
		# If player isn't currently falling, set their starting fall speed
		if self.change_y == 0:
			self.change_y = 10
		# If player is currently falling, slightly increase fall speed
		else:
			self.change_y += 0.30

	# Set player's left movement speed
	def move_left(self):
		self.change_x = -MOVE_SPEED

	# Set player's right movement speed
	def move_right(self):
		self.change_x = MOVE_SPEED
	
	# Stop player's movement
	def stop(self):
		self.change_x = 0
	
