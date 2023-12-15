#pip install pygame
import pygame, sys , threading , time
from class_button import Button
from pygame.locals import *
from tkinter import Tk, filedialog
from Loading_bar import loading_bar_simulation
#from speechrecognition import recognize_lyrics
from sphinx import sphinx_recognize_lyrics


pygame.init()
SCREEN = pygame.display.set_mode((1280, 720)) #Fullscreen pygame.FULLSCREEN)  
pygame.display.set_caption("Lyrical Harmony")
CLOCK = pygame.time.Clock()
BG = pygame.image.load("assets/B.JPG")


Button_sound_sfx = pygame.mixer.Sound("assets/Nextbutton.wav")
Quit_sound_sfx = pygame.mixer.Sound("assets/Quitbutton.wav")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def select():
    uploading = False
    upload_start_time = None
    upload_successful = True  # Assume success by default
    file_path = None

    while True:
        SELECT_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        
        if uploading:
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - upload_start_time) / 1000  # Convert to seconds
            if elapsed_time < 10:
                # Display a loading bar during the 10-second timeout
                loading_bar_simulation()
            else:
                # Recognize lyrics and display them 5 words for 2 seconds and play the song
                #lyrics = recognize_lyrics(file_path)
                lyrics = sphinx_recognize_lyrics(file_path)
                words = lyrics.split()
                #play the song
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()  # Play the music
                for i in range(0, len(words), 5):
                    SCREEN.fill("black")
                    lyrics_text = get_font(40).render(" ".join(words[i:i+5]), True, "White")
                    lyrics_rect = lyrics_text.get_rect(center=(640, 360))
                    SCREEN.blit(lyrics_text, lyrics_rect)
                    pygame.display.update()
                    time.sleep(2)           
            # Display the "Upload Failed" message if it failed, otherwise "Upload in Progress"
        else:
            if not upload_successful:
                # If the upload failed, show "Upload Failed" and "Back" button only
                UPLOAD_TEXT = get_font(40).render("Upload Failed :(", True, "White")
                UPLOAD_RECT = UPLOAD_TEXT.get_rect(center=(640, 260))
                SCREEN.blit(UPLOAD_TEXT, UPLOAD_RECT)

                SELECT_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
                SELECT_BACK.changeColor(SELECT_MOUSE_POS)
                SELECT_BACK.update(SCREEN)
            else:
                if file_path is None:
                    # Show the file selection dialog only if the upload was not successful and a file was not already selected
                    root = Tk()
                    root.withdraw()
                    file_path = filedialog.askopenfilename()
                    root.destroy()

                    if not file_path:
                        # File dialog was canceled
                        main_menu()  # Return to the main menu
                if file_path:
                    # Do something with the selected file (e.g., pass it to the backend)
                    # You can update your backend logic here
                    uploading = True
                    upload_start_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit_sound_sfx.play()
                time.sleep(1)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if uploading:
                    Button_sound_sfx.play()
                    # Ignore clicks on the "Back" button during upload
                    continue
                if SELECT_BACK.checkForInput(SELECT_MOUSE_POS):
                    Button_sound_sfx.play()
                    main_menu()
        pygame.display.update()
def start():
    while True:
        START_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black") #pour que après avoir cliqué sur start, l'écran soit noir et non pas le fond d'écran du menu principal
        START_TEXT = get_font(40).render("Choose your song", True, "White")
        START_RECT = START_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(START_TEXT, START_RECT)
        START_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        START_BACK.changeColor(START_MOUSE_POS)
        START_BACK.update(SCREEN)
        START_SELECT = Button(image=None, pos=(640, 360), text_input="SELECT FILE", font=get_font(40), base_color="White", hovering_color="Green")
        START_SELECT.changeColor(START_MOUSE_POS)
        START_SELECT.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit_sound_sfx.play()
                time.sleep(1)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Button_sound_sfx.play()
                if START_BACK.checkForInput(START_MOUSE_POS):
                  Button_sound_sfx.play() 
                  main_menu()
                  break
                elif START_SELECT.checkForInput(START_MOUSE_POS):
                    Button_sound_sfx.play()
                    select()
        pygame.display.update()
        
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
               # Button_sound_sfx.play()
                if START_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Button_sound_sfx.play()
                    start()
                    #loading_bar_simulation()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Quit_sound_sfx.play()
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()