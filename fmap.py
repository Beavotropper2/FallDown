import pygame, random
from platform import Platform
from constants import *

class Map():
	# Lists of collidable objects
	platform_list = None
	enemy_list = None
	last_plat = None

	# Distance scrolled down
	map_shift = 0

	def __init__(self, player):
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player

	# Update everything
	def update(self):
		# Remove any platforms above current window
		plat_removed = False
		for plat in self.platform_list:
			if plat.rect.bottom <= 0:
				self.platform_list.remove(plat)
				plat_removed = True
		if plat_removed:
			print("Removed platform")
			self.create_platform(self.last_plat[2] + SPACE_LEN + self.map_shift)
			self.map_shift = 0
		
		# Update lists
		self.platform_list.update()
		self.enemy_list.update()

	# Draw everything
	def draw(self, screen):
		# Draw background
		screen.fill(BLACK)
		
		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)

	# Scroll down
	def shift_map(self, shift_y):
		self.map_shift += shift_y

		for platform in self.platform_list:
			platform.rect.y += shift_y

		self.player.rect.y += shift_y
	
	# Generate a platform
	def gen_platform(self, plat):
		plat_l = Platform(plat[0], plat[1])
		plat_l.rect.x = 0
		plat_l.rect.y = plat[2]
		plat_l.player = self.player
		
		plat_r = Platform(SCREEN_WIDTH - plat[0] - GAP_LEN, plat[1])
		plat_r.rect.x = plat[0] + GAP_LEN
		plat_r.rect.y = plat[2]
		plat_r.player = self.player
		
		self.platform_list.add(plat_l)
		self.platform_list.add(plat_r)
		
	def create_platform(self, yloc):
		# Create platform dimensions based on last platform
		if self.last_plat is None:
			plat = [random.randrange(0, SCREEN_WIDTH - GAP_LEN), 25, yloc]
		elif self.last_plat[0] < SCREEN_WIDTH / 2:
			plat = [random.randrange(SCREEN_WIDTH / 2, SCREEN_WIDTH - GAP_LEN), 25, yloc]
		else:
			plat = [random.randrange(0, SCREEN_WIDTH / 2), 25, yloc]
			
		# Generate platform
		self.gen_platform(plat)
		#print("Platform created")
		
		# Save current platform
		self.last_plat = plat
