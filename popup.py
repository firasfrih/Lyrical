import pygame

def display_popup(message, screen):
    popup_font = pygame.font.Font(None, 24)
    popup_text = popup_font.render(message, True, (255, 255, 255))
    popup_rect = popup_text.get_rect(bottomright=(screen.get_width() - 20, screen.get_height() - 20))
    screen.blit(popup_text, popup_rect)
    pygame.display.flip()
    pygame.time.wait(8000)  # Display the pop-up for 8 seconds
