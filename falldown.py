# Fall Down

import pygame, random

from player import Player
from fmap import Map
from constants import *

def main():
	# Initialize Pygame
	pygame.init()
    
	# Create an 800x600 sized screen
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
     
	# Set the title of the window
	pygame.display.set_caption('Fall Down')
     
	# Create the player
	player = Player()
	
	# Create the map
	game_map = Map(player)
	for y in range(400, SCREEN_HEIGHT * 2, SPACE_LEN):
		game_map.create_platform(y)

	# Set active sprites
	active_sprites = pygame.sprite.Group()
	player.game_map = game_map
	player.rect.x = random.randrange(0, SCREEN_WIDTH - player.width)
	player.rect.y = 50 + player.rect.height
	active_sprites.add(player)

	# Create game clock
	clock = pygame.time.Clock()

	# Loop until window closed
	done = False

	score = 0
    
	while not done:
	    
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
     
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.move_left()
				if event.key == pygame.K_RIGHT:
					player.move_right()
                     
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					player.stop()
				if event.key == pygame.K_RIGHT:
					player.stop()
                    
        # --- Game Logic ---
        
		# Update player
		active_sprites.update()
		#print("Player y_location: " + str(player.rect.y))

		# Update map
		game_map.update()

		# Check if player has lost
		if not player.alive:
			done = True

		# Draw everything
		game_map.draw(screen)
		active_sprites.draw(screen)

		# Limit to 60 FPS
		clock.tick(60)

		game_map.shift_map(MAP_SHIFT)

		pygame.display.flip()

	pygame.quit()
		
if __name__ == "__main__":
	main()
