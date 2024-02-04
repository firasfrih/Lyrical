import pygame
import sys
from pygame.locals import *
import time
from Loading_bar import SCREEN

from class_button import Button
from Text_Box import InputBox
from Submit import submit

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Lyrical Harmony")
CLOCK = pygame.time.Clock()
BG = pygame.image.load("assets/A.JPG")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

Button_sound_sfx = pygame.mixer.Sound("assets/Nextbutton.wav")
Quit_sound_sfx = pygame.mixer.Sound("assets/Quitbutton.wav")

def Start_app():
    SUBMIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 450),
                                text_input="SUBMIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 600), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    TEXT_BOX = InputBox(background_image=pygame.image.load("assets/Rect_large.png"), position=(180, 250),
                        font=get_font(50), base_color="#d7fcd4", hovering_color="White")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit_sound_sfx.play()
                time.sleep(1)
                pygame.quit()
                sys.exit()
            TEXT_BOX.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if SUBMIT_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    if TEXT_BOX.text:  # Check if the text box is not empty
                        Button_sound_sfx.play()
                        submit(TEXT_BOX.text)

                elif QUIT_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    Quit_sound_sfx.play()
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

        SCREEN.blit(BG, (0, 0))
        MENU_TEXT = get_font(50).render("Give a title :)", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        QUIT_BUTTON.update(SCREEN)
        if TEXT_BOX.text:
            SUBMIT_BUTTON.update(SCREEN)
        else:
            SUBMIT_BUTTON.update(SCREEN, active=False)
        pygame.draw.rect(SCREEN, (255, 255, 255), TEXT_BOX.rect)
        TEXT_BOX.draw(SCREEN)
        pygame.display.update()
