import pygame
import random


class Bird:
    def __init__(self, display, width, height):
        self.direction = random.choice(['rtl', 'ltr'])
        if self.direction == 'rtl':
            self.x = width + 50
        else:
            self.x = -50
        self.y = random.randint(0, height / 2)
        self.display = display
        self.height = height
        self.width = width
        self.image = self.image
        self.speed = self.speed
        self.point = self.point
        self.sound = self.sound
        self.is_dead = False

    def show(self):
        if self.direction == 'rtl':
            self.display.blit(pygame.transform.flip(self.image, True, False), [self.x, self.y])
        else:
            self.display.blit(self.image, [self.x, self.y])

    def fly(self):
        if self.direction == 'rtl':
            self.x -= self.speed
            # if not self.is_dead:
            #     self.y += random.choice([2, 0, -2])
        else:
            self.x += self.speed
            # if not self.is_dead:
            #     self.y += random.choice([2, 0, -2])

    def get_shot(self):
        self.is_dead = True
        self.sound.play()
        self.speed = 0
        rand = random.randint(self.height / 1.5, self.height - 40)
        while self.y < rand:
            self.y += 1
        self.image = pygame.transform.flip(self.image, False, True)


class Duck(Bird):
    def __init__(self, display, width, height):
        self.image = pygame.image.load('assets/images/duck.png')
        self.speed = 4
        self.point = 1
        self.sound = pygame.mixer.Sound('assets/Sounds/duck.wav')
        Bird.__init__(self, display, width, height)


class Stork(Bird):
    def __init__(self, display, width, height):
        # 64 * 64 px --> 32 * 32 px
        self.image = pygame.transform.scale(pygame.image.load('assets/images/stork.png'), (32, 32))
        self.speed = 6
        self.point = 2
        self.sound = pygame.mixer.Sound('assets/Sounds/duck.wav')
        Bird.__init__(self, display, width, height)


class Eagle(Bird):
    def __init__(self, display, width, height):
        # 536 * 466 px --> 32 * 32 px
        self.image = pygame.transform.scale(pygame.image.load('assets/images/eagle.png'), (24, 27))
        self.speed = 8
        self.point = 4
        self.sound = pygame.mixer.Sound('assets/Sounds/eagle.wav')
        self.sound.set_volume(0.35)
        Bird.__init__(self, display, width, height)
