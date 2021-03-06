import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from score import Score

def run_game():
    #初始化游戏并创建一个对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    hscore = Score()
    stats = GameStats(ai_settings,hscore.score_get())
    sb = Scoreboard(ai_settings,screen,stats)

    bg_color = (230,230,230)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen,ship, aliens)

    play_button = Button(ai_settings, screen, "Play")

    #alien = Alien(ai_settings, screen)

    while True:
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship, aliens, bullets)
        bullets.update()
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets,hscore)
            gf.update_aliens(ai_settings,screen, stats,sb, ship, aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()

        #pygame.display.flip()

run_game()
