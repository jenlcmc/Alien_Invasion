import sys
import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """overall class for game and behavior"""
    def __init__(self):
        """initialize game and create game"""
        pygame.init()
        self.settings = Settings()

        #screen full
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("ALIEN INVASION")
        #ship
        self.ship = Ship(self)
        #bullet
        self.bullets = pygame.sprite.Group()
        #alien
        self.aliens = pygame.sprite.Group()
        
        #aliens
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #chekc for inputs activities
            self._check_events()
            #update ship
            self.ship.update()
            #update bullets
            self._update_bullets()
            #monitor screen
            self._update_screen()
    
    def _check_events(self):
        #watch for keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #key up and left + right
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                #key down and left + right
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    #check down key
    def _check_keydown_events(self, event):
        #respont to keypresses
        if event.key == pygame.K_RIGHT:
            #move ship to right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #move ship to left
            self.ship.moving_left = True
            #exit key with q
        elif event.key == pygame.K_q:
            sys.exit()
            #fire bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        #respont to key realeases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    #control bullet
    def _fire_bullet(self):
        """Create new bullet and add it to bullets group"""
        #limit bullets to 5
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
            """Update pos of bullets and get rid of old"""
            #update bullet
            self.bullets.update()
            #delete bullet 
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    #alien making
    def _create_fleet(self):
        """create fleet of alien"""
        #make alien + find num in row
        #spacing between each is = to 1 alien width 
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        #create 1st row
        for alien_number in range(number_alien_x):
            #create + place
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _update_screen(self):
        """update image on screen and flip to new screen"""
        #fill color
        self.screen.fill(self.settings.bg_color)
        #check for ship
        self.ship.blitme()
        #update bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #make aliens
        self.aliens.draw(self.screen)
        #make most recently draw screen possible
        pygame.display.flip()

    

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()