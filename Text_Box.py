import pygame

class InputBox:
    def __init__(self, background_image, position , font, base_color, hovering_color):
        self.background_image = background_image
        self.position = position
        self.text = ""  # Initial text is empty
        self.font = pygame.font.Font(None, 50)  # Default font
        self.active = False  # Whether the textbox is currently active for typing
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is inside the textbox
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # If Enter key is pressed, textbox loses focus
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    # If Backspace key is pressed, remove the last character
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        screen.blit(self.background_image, self.position)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.position[0] + self.background_image.get_width() / 2,
                                                   self.position[1] + self.background_image.get_height() / 2))
        screen.blit(text_surface, text_rect)

    @property
    def rect(self):
        return self.background_image.get_rect(topleft=self.position)
