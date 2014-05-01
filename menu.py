import pygame, random
from constants import *

class Menu():
	# Menu (main menu)
	main_menu = None
	# Menu (score menu)
	score_menu = None
	
	def __init__(self, screen):
		self.screen = screen
		self.title_font = pygame.font.Font(None, 64)
		self.content_font = pygame.font.Font(None, 32)
		
		# Init main_menu
		self.menu_text = self.title_font.render("Fall Down", 2, LIME)
		self.menu_pos = [(SCREEN_WIDTH - self.menu_text.get_rect().width) / 2, 
						(SCREEN_HEIGHT - self.menu_text.get_rect().height) / 2]
						
		self.dir1_text = self.content_font.render("Use the left and right directional keys to guide the bomb through openings", 2, LIME)
		self.dir1_pos = [(SCREEN_WIDTH - self.dir1_text.get_rect().width) / 2, 
						(SCREEN_HEIGHT - self.dir1_text.get_rect().height) / 2 + 100]
		self.dir2_text = self.content_font.render("Press enter/return to begin the game!", 2, LIME)
		self.dir2_pos = [(SCREEN_WIDTH - self.dir2_text.get_rect().width) / 2, 
						(SCREEN_HEIGHT - self.dir2_text.get_rect().height) / 2 + 150]
		
		# Init score_menu
		
	
	def show_main(self):
		# Draw all text onto main menu screen
		self.screen.blit(self.menu_text, self.menu_pos)
		self.screen.blit(self.dir1_text, self.dir1_pos)
		self.screen.blit(self.dir2_text, self.dir2_pos)
		pygame.display.flip()
		
		done = False
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						done = True
						
	def show_score(self, score):
		# Create score text
		pass
		score_text = self.title_font.render("Player Score: " + str(score), 2, LIME)
		score_pos = [(SCREEN_WIDTH - score_text.get_rect().width) / 2,
							(SCREEN_HEIGHT - score_text.get_rect().height) / 2]
		
		score_background = pygame.Surface([SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2])
		score_pos = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
		
		self.screen.blit(score_background, score_pos)
		
		done = False
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						done = True
