import pygame
from random import randint

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