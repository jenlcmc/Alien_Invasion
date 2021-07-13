import sys
import pygame
import json
import time
import random

from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
class AlienInvasion:
    """overall class for game and behavior"""

    def __init__(self):
        """initialize game and create game"""
        pygame.init()
        self.settings = Settings()

        #screen full
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("ALIEN INVASION")
        
        #create instance to store game stats
        self.stats = GameStats(self)
        #create scoreboard
        self.sb = Scoreboard(self)
        #ship
        self.ship = Ship(self)
        #bullet
        self.bullets = pygame.sprite.Group()
        #alien
        self.aliens = pygame.sprite.Group()
        
        #aliens
        self._create_fleet()

        #make play button
        self.play_button = Button(self, "Play")

        #Make difficulty_level button
        self._make_difficulty_buttons()

        #end game

    def _make_difficulty_buttons(self):
        """Make buttons that allow player to select difficulty level."""
        self.easy_button = Button(self, "Easy")
        self.medium_button = Button(self, "Medium")
        self.hard_button = Button(self, "Hard")

        # Position buttons so they don't all overlap.
        self.easy_button.rect.top = (
            self.play_button.rect.top + 1.5 * self.play_button.rect.height)
        self.easy_button._update_msg_position()

        self.medium_button.rect.top = (
            self.easy_button.rect.top + 1.5*self.easy_button.rect.height)
        self.medium_button._update_msg_position()

        self.hard_button.rect.top = (
            self.medium_button.rect.top + 1.5*self.medium_button.rect.height)
        self.hard_button._update_msg_position()

    def run_game(self):
        #Set fps for the game 
        FPS = 80
        clock = pygame.time.Clock()

        """Start the main loop for the game"""
        while True:
            clock.tick(FPS)
            self.screen.fill((0,0,0))
            #chekc for inputs activities
            self._check_events()
            
            if self.stats.game_active:
                #update ship
                self.ship.update()
                #update bullets
                self._update_bullets()
                #upadte aliens
                self._update_aliens()

            #monitor screen
            self._update_screen()
    
    def _check_events(self):
        #watch for keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._close_game()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    self._check_difficulty_buttons(mouse_pos)
                #key up and left + right
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                #key down and left + right
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start a new game when player click play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _check_difficulty_buttons(self, mouse_pos):
        """Set the appropriate difficulty level."""
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        if easy_button_clicked:
            self.settings.difficulty_level = 'easy'
        elif medium_button_clicked:
            self.settings.difficulty_level = 'medium'
        elif hard_button_clicked:
            self.settings.difficulty_level = 'hard'


    def _start_game(self):
            #Reset the game statistics
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True

            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #get rid of remain aliens + bullets
            self.aliens.empty()
            self.bullets.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #Hide the mosue cursor
            pygame.mouse.set_visible(False)
    
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
            self._close_game()
            #fire bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()

    def _check_keyup_events(self, event):
        #respont to key realeases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """Check if any aliens have reached a bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat this same as ship got hit
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
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

        self._check_bullet_alien_collisions()
            
    def _check_bullet_alien_collisions(self):
        #check any bullets hit alien_speedif so, get rid of bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            #destory existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increse_speed()

            #increse level    
            self.stats.level += 1  
            self.sb.prep_level()

    def _update_aliens(self):
        """Check if fleet is at egde 
        If so -> update pos of all aliens
        """
        self._check_fleet_edges()
        """"Update pos of all aliens in fleet"""
        self.aliens.update()

        #look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #look for aliens hitting the bot of screen
        self._check_aliens_bottom()

    #alien making
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create alien and place in row"""
        #create + place
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _ship_hit(self):
        """Respond to ship being hit by alien"""
        if self.stats.ships_left > 0:
            #decrement ship_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #get rid of remain aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """update image on screen and flip to new screen"""
        #fill color
        #self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg, (0,0))
        
        #check for ship
        self.ship.blitme()
        #update bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #make aliens
        self.aliens.draw(self.screen)
        #draw scoreboard
        self.sb.show_score()

        #draw play button if game is inactive 
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()

        #make most recently draw screen possible
        pygame.display.flip()

    def _close_game(self):
        """Save high score and exit"""
        saved_high_score = self.stats.get_saved_high_score()
        if self.stats.high_score > saved_high_score:
            with open('high_score.json', 'w') as f:
                json.dump(self.stats.high_score, f)

        sys.exit()

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()