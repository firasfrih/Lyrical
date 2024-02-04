import pygame
import sys
from class_button import Button
from Translate import translate_lyrics

def display_language_selection(lyrics_text):
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Language Selection")
    CLOCK = pygame.time.Clock()
    BACKGROUND_COLOR = (220, 220, 255)  # Light purple background
    TEXT_COLOR = (0, 0, 0)  # Black text color
    font = pygame.font.Font("assets/font.ttf", 14)# Font for displaying language buttons
    # Dictionary of language codes and their corresponding full names
    language_names = {
        "de": "German",
        "en": "English",
        "ro": "Romanian",
        "nl": "Dutch ",
        "pt": "Portuguese",
        "da": "Danish",
        "es": "Spanish",
        "fr": "French",
        "no": "Norwegian",
        "it": "Italian",
        "sv": "Swedish",
        "tr": "Turkish",
    }
    languages = list(language_names.keys())  # Get the language codes
    language_buttons = []
    button_y = 50
    for language in languages:
        button = Button(image=pygame.image.load("assets/Rect_Languages.png"),
                        pos=(SCREEN_WIDTH // 2, button_y),
                        text_input=language_names[language], font=font,  # Use language code
                        base_color="#d7fcd4", hovering_color="White")
        language_buttons.append(button)
        button_y += 50

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if any language button is clicked
                for button in language_buttons:
                    if button.checkForInput(event.pos):
                        #print(lyrics_text)
                        # Get the language code from the language name
                        language_code = next((code for code, name in language_names.items() if name == button.text_input), None)

                        if language_code is not None:
                            translated_lyrics = translate_lyrics(lyrics_text, language_code)
        SCREEN.fill(BACKGROUND_COLOR)
        for button in language_buttons:
            button.update(SCREEN)
        pygame.display.flip()
        CLOCK.tick(30)

    pygame.quit()
    sys.exit()
