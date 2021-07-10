import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        """Init button attribute"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set dimesions and properties of button 
        self.width, self.height = 230, 50
        self.button_color = (0, 255, 0) #need to change color 
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 45)

        #build button;s rect obj and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #The button message need to be prepped only 1
        self._prep_msg(msg) 

    def _prep_msg(self, msg):
        """Turn msg into rendered image and center text of button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def _update_msg_position(self):
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        #draw blank button and draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)