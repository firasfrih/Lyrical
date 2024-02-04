import pygame
from class_button import Button

SCREEN = pygame.display.set_mode((1280, 720))
BACKGROUND_COLOR = (220, 220, 255) 
TEXT_COLOR = (0, 0, 0)
CLOCK = pygame.time.Clock()

def display_upload_message():
	UPLOAD_message = pygame.font.Font("assets/font.ttf", 40).render("Upload in progress...", True, "Black")
	UPLOAD_message_rect = UPLOAD_message.get_rect(center=(640, 360))
	SCREEN.blit(UPLOAD_message, UPLOAD_message_rect)
	pygame.display.update()

# function to simulate loading bar to add to the main.py file in function select() while uploading is true
def loading_bar_simulation():
	loading_bar = pygame.Rect(0, 0, 0, 0)
	loading_bar.w = 0
	loading_bar.h = 50
	loading_bar.x = 0
	loading_bar.y = 0
	loading_bar_color = (255, 255, 255)
	display_upload_message()
	SCREEN.fill(BACKGROUND_COLOR)
	pygame.draw.rect(SCREEN, loading_bar_color, loading_bar)
	pygame.display.update()
	for i in range(0, 1280, 10):
		loading_bar.w += 10
		loading_bar.x += 10
		pygame.draw.rect(SCREEN, loading_bar_color, loading_bar)
		pygame.display.update()
		CLOCK.tick(60)
  