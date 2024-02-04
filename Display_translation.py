import pygame
import sys
import time

from class_button import Button

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def display_translation(lyrics_text):
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Lyrical Harmony")
    CLOCK = pygame.time.Clock()
    BACKGROUND_COLOR = (220, 220, 255)  # Light purple background
    TEXT_COLOR = (0, 0, 0)   # Black text color
    Quit_sound_sfx = pygame.mixer.Sound("assets/Quitbutton.wav")
    font = pygame.font.Font("assets/font.ttf", 11)  # Font for displaying lyrics
    lines = lyrics_text.split('\n') # Split lyrics into lines
    line_spacing = 25
    y_offset = 0
    scroll_speed = 10
    QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(1100, 200), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    y_offset += scroll_speed
                elif event.button == 5:
                    y_offset -= scroll_speed
                if QUIT_BUTTON.checkForInput(event.pos):
                    Quit_sound_sfx.play()
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()
        SCREEN.fill(BACKGROUND_COLOR)
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, TEXT_COLOR)
            text_rect = text_surface.get_rect(topleft=(50, 50 + i * line_spacing + y_offset))
            SCREEN.blit(text_surface, text_rect)
        QUIT_BUTTON.update(SCREEN)
        pygame.display.flip()
        CLOCK.tick(30)
    pygame.quit()
    sys.exit()

