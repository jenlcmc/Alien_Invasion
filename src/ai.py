import pygame

from random import random
from alien_invasion import AlienInvasion

class AI:
    def __init__(self, ai_game):
        #reference to game object
        self.ai_game = ai_game

    def run_game(self):
        #start game in active state  
        self.ai_game.stats.game_active = True
        pygame.mouse.set_visible(False)

        #speed up the game 
        self._modify_speed(1.5)

        #make full fleet size
        self.fleet_size = len(self.ai_game.aliens)

        #main loop of the game
        while True:
            #check event to use q to quit
            self.ai_game._check_events()
            self._implement_strategy()

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()

            self.ai_game._update_screen()

    def _implement_strategy(self):
        #target an alien  
        target_alien = self._get_target_alien()

        #MOve to the target 
        ship = self.ai_game.ship
        if ship.rect.x < target_alien.rect.x:
            ship.moving_right = True
            ship.moving_left = False
        elif ship.rect.x > target_alien.rect.x:
            ship.moving_right = False
            ship.moving_left = True

        #sweep right left for the ship until half is destroy then stop
        """if len(self.ai_game.aliens) >= 0.5 * self.fleet_size:
            self._sweep_right_left()
        else:
            self.ai_game.ship.moving_right = False
            self.ai_game.ship.moving_left = False"""

        #fire bullet  
        firing_frequency = 0.5  

        if random() < firing_frequency:
            self.ai_game._fire_bullet()

    def _get_target_alien(self):
        #find right most alien in bot pick one and compare
        #return coordination of alien  
        target_alien = self.ai_game.aliens.sprites()[0]
        for alien in self.ai_game.aliens.sprites():
            if alien.rect.y > target_alien.rect.y:
                #father down than target
                target_alien = alien
            elif alien.rect.y < target_alien.rect.y:
                #above target_alien
                continue
            elif alien.rect.x > target_alien.rect.x:
                #in same row but far right
                target_alien = alien
        
        return target_alien

    def _sweep_right_left(self):
        #make ship move 
        ship = self.ai_game.ship
        screen_rect = self.ai_game.screen.get_rect()

        if not ship.moving_left and not ship.moving_right:
            #ship not move so have to move
            ship.moving_right = True
        elif (ship.moving_right and ship.rect.right > screen_rect.right - 10):
            #ship will get git right egde -> move left
            ship.moving_right = False
            ship.moving_left = True
        elif(ship.moving_left and ship.rect.left < 10):
            ship.moving_left = False
            ship.moving_right = True

    def _modify_speed(self, speed_factor):
        self.ai_game.settings.ship_speed *= speed_factor
        self.ai_game.settings.bullet_speed *= speed_factor
        self.ai_game.settings.alien_speed *= speed_factor

if __name__ == "__main__":
    ai_game = AlienInvasion()

    ai_player = AI(ai_game)
    ai_player.run_game()
