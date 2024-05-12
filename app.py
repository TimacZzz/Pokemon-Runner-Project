import pygame
from sys import exit
from random import choice
from player import Player
from obstacles import Obstacle

#Check Collision
def collision_sprite(score):
    for item in obstacle_group:
        if pygame.sprite.collide_rect(player.sprite, item):
            if item.type == 'food':
                item.remove(obstacle_group)
                score += 1
            else:
                obstacle_group.empty()
                player.sprite.gravity = 0
                player.sprite.rect.bottom = 320
                return False, score
    return True, score

#Display scores on the screen
def display_score(score):
    score_surf = test_font.render(f'Score: {score}', False, (255, 255, 255))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)

#Initialize Pygame
pygame.init()

#Create screen
screen = pygame.display.set_mode((800, 400))
clock =pygame.time.Clock()

test_font = pygame.font.Font('others/Pixeltype.ttf', 50)
score = 0

#Background & Title & Icon
background = pygame.image.load('others/forest.png').convert_alpha()
pygame.display.set_caption('Pokemon Runner')
icon = pygame.image.load('others/pokemon icon.png')
pygame.display.set_icon(icon)

#Music
relax_music = pygame.mixer.Sound('others/relax.mp3')
battle_music = pygame.mixer.Sound('others/battle.mp3')
relax_music.set_volume(0.1)
battle_music.set_volume(0.1)

end_scene = pygame.image.load('others/end.png').convert_alpha()
end_pikachu = pygame.image.load('others/pikachu.png').convert_alpha()
game_over = pygame.image.load('others/gameover.png').convert_alpha()

game_active = False
started = False

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

game_name = test_font.render('Pokemon Runner',False,(255, 255, 255))
game_name_rect = game_name.get_rect(center = (410,50))

game_message = test_font.render('Press enter to begin',False,(255, 255, 255))
game_message_rect = game_message.get_rect(center = (410,300))

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly','ground','fly', 'ground', 'food'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_active = True
                started = True
                score = 0


    if game_active:
        relax_music.stop()
        screen.blit(background, (-150, 0))
        battle_music.play(loops=-1)

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        result = collision_sprite(score)
        game_active = result[0]
        score = result[1]
        display_score(score)


    else:
        battle_music.stop()
        relax_music.play(loops=-1)
        screen.blit(end_scene, (0, 0))
        screen.blit(end_pikachu, (260, 60))
        if started == False:
            screen.blit(game_name, game_name_rect)
            screen.blit(game_message, game_message_rect)
        else:
            display_score(score)
            screen.blit(game_message, game_message_rect)


    pygame.display.update()
    clock.tick(60)
