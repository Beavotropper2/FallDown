import pygame, random
from constants import *

class Menu():
	# Menu (main menu)
	main_menu = None
	# Menu (score menu)
	score_menu = None
	
	def __init__(self, screen):
		self.screen = screen
		
		# Init main_menu
		menu_font = pygame.font.Font(None, 64)
		self.menu_text = menu_font.render("Fall Down", 2, LIME)
		self.menu_pos = [(SCREEN_WIDTH - self.menu_text.get_rect().width) / 2, 
						(SCREEN_HEIGHT - self.menu_text.get_rect().height) / 2]
		
		# Init score_menu
		
	
	def show_main(self):
		self.screen.blit(self.menu_text, self.menu_pos)
		pygame.display.flip()
		pygame.time.wait(4000)

	def show_score(self):
		pass
