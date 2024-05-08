import pygame
from sys import exit
from random import randint, choice

#Class for the player -> Pikachu
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_run1 = pygame.image.load('player/player1.png').convert_alpha()
        player_run2 = pygame.image.load('player/player2.png').convert_alpha()
        player_run3 = pygame.image.load('player/player3.png').convert_alpha()
        player_run4 = pygame.image.load('player/player4.png').convert_alpha()
        self.player_run = [player_run1, player_run2, player_run3, player_run4]
        self.player_run_index = 0
        player_jump1 = pygame.image.load('player/jump1.png').convert_alpha()
        player_jump2 = pygame.image.load('player/jump2.png').convert_alpha()
        player_jump3 = pygame.image.load('player/jump3.png').convert_alpha()
        player_jump4 = pygame.image.load('player/jump4.png').convert_alpha()
        self.player_jump = [player_jump1, player_jump2, player_jump3, player_jump4]
        self.player_jump_index = 0
        self.image = self.player_run[self.player_run_index]
        self.rect = self.image.get_rect(midbottom=(150, 320))
        self.jump_image = self.player_jump[self.player_jump_index]
        self.jump_rect = self.jump_image.get_rect()
        self.gravity = 0

    #If Space is pressed and player is on the ground, jump
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 320:
            self.gravity = -22

    #Stimulate a gravity for the player
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 320:
            self.rect.bottom = 320

    #Animate the player
    def animation(self):
        if self.rect.bottom < 320:
            self.image = self.jump_image
            self.player_jump_index += 0.3
            if self.player_jump_index >= len(self.player_jump):
                self.player_jump_index = 0
            self.image = self.player_jump[int(self.player_jump_index)]
        else:
            self.player_run_index += 0.1
            if self.player_run_index >= len(self.player_run):
                self.player_run_index = 0
            self.image = self.player_run[int(self.player_run_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()

#Class for the obstacles: Charizard, Blastoise & Pokemon Food
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load('fly/fly1.png')
            fly_2 = pygame.image.load('fly/fly2.png')
            fly_3 = pygame.image.load('fly/fly3.png')
            fly_4 = pygame.image.load('fly/fly4.png')
            self.frames = [fly_1, fly_2, fly_3, fly_4]
            y_pos = 190
        if type == 'food':
            food = pygame.image.load('others/food.png')
            self.frames = [food]
            y_pos = 330
        if type == 'ground':
            ground_1 = pygame.image.load('ground/walk1.png')
            ground_2 = pygame.image.load('ground/walk2.png')
            ground_3 = pygame.image.load('ground/walk3.png')
            ground_4 = pygame.image.load('ground/walk4.png')
            ground_5 = pygame.image.load('ground/walk5.png')
            self.frames = [ground_1, ground_2, ground_3, ground_4, ground_5]
            y_pos = 311

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))
        self.type = type

    #Animate the obstacles
    def animation_state(self):
        if type == 'food':
            self.animationn_index = 0
            self.image = self.frames[self.animationn_index]
        else:
            self.animation_index += 0.1
            if self.animation_index >= len(self.frames):
                self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    #Destroy obstacles if they leave screen
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

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