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
	frames = 0

	def __init__(self, player):
		self.platform_list = pygame.sprite.Group()
		#self.enemy_list = pygame.sprite.Group()
		self.player = player

		self.bg_image = pygame.image.load("bg_castle.png").convert()
		self.bg_image.set_colorkey(WHITE)
		self.bg_loaded = False

	# Update everything
	def update(self):
		# Update lists
		self.platform_list.update()
		#self.enemy_list.update()
		self.frames += 1

		# Remove any platforms above current window
		plat_removed = False
		for plat in self.platform_list:
			if plat.rect.bottom <= 0:
				self.platform_list.remove(plat)
				plat_removed = True
		if plat_removed:
			#print("Removed platform")
			self.create_platform(self.last_plat[2] + SPACE_LEN + self.map_shift)
			self.map_shift = 0

	# Draw everything
	def draw(self, screen):
		# Draw background
		screen.blit(self.bg_image, (0,0))
		
		# Draw platforms
		self.platform_list.draw(screen)
		#self.enemy_list.draw(screen)

	# Shift platforms up
	def shift_map(self, shift_y):
		# Update map_shift variable
		self.map_shift += shift_y

		# Update all platforms locations
		for platform in self.platform_list:
			platform.rect.y += shift_y

		# Update player location
		self.player.rect.y += shift_y
	
	# Generate a platform
	def gen_platform(self, plat):
		# Left side of platform
		plat_l = Platform(plat[0], plat[1])
		plat_l.rect.x = 0
		plat_l.rect.y = plat[2]
		plat_l.player = self.player
		
		# Right side of platform
		plat_r = Platform(SCREEN_WIDTH - plat[0] - GAP_LEN, plat[1])
		plat_r.rect.x = plat[0] + GAP_LEN
		plat_r.rect.y = plat[2]
		plat_r.player = self.player
		
		# Add both platforms to platform_list
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
