import time
import pygame
import sys
from pygame.locals import *

from class_button import Button
from Start import Start_app

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Lyrical Harmony")
CLOCK = pygame.time.Clock()
BG = pygame.image.load("assets/B.JPG")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

Button_sound_sfx = pygame.mixer.Sound("assets/Nextbutton.wav")
Quit_sound_sfx = pygame.mixer.Sound("assets/Quitbutton.wav")

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render("Welcome :)", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        START_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 250),
                                  text_input="START", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 450), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for button in [START_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit_sound_sfx.play()
                time.sleep(1)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Button_sound_sfx.play()
                    time.sleep(1)
                    Start_app()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Quit_sound_sfx.play()
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()
