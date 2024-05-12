import pygame

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