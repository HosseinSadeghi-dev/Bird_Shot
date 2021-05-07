import pygame
import time


class Gun:

    def __init__(self, display, width, height):
        pygame.init()
        self.x = width / 2
        self.y = height / 2
        self.display = display
        self.score = 0
        self.sound.set_volume(0.15)

        self.ammo = self.ammo
        self.clip_size = self.clip_size
        self.reload_time = self.reload_time
        self.bullet = self.bullet
        self.image = self.image
        self.sound = self.sound

    def show(self):
        self.display.blit(self.image, [self.x, self.y])

    def fire(self, birds):
        self.ammo -= 1
        self.sound.play()
        for bird in birds:
            if not bird.is_dead and pygame.Rect(
                    self.x, self.y, 32, 32).colliderect(pygame.Rect(bird.x, bird.y, 32, 32)):
                bird.get_shot()
                self.score += bird.point

    def reload(self):
        time.sleep(self.reload_time)
        self.ammo = self.clip_size


class Shotgun(Gun):
    def __init__(self, display, width, height):
        self.ammo = 7
        self.clip_size = 7
        self.reload_time = 3
        self.image = pygame.image.load('assets/images/shotgun_aim.png')
        self.sound = pygame.mixer.Sound('assets/Sounds/shotgun.wav')
        self.bullet = pygame.image.load('assets/images/shotgun_ammo.png')
        self.bullet = pygame.transform.scale(self.bullet, (15, 44))
        Gun.__init__(self, display, width, height)


class AWP(Gun):
    def __init__(self, display, width, height):
        self.ammo = 12
        self.clip_size = 12
        self.reload_time = 2
        self.image = pygame.transform.scale(pygame.image.load('assets/images/awp_aim.png'), (15, 15))
        self.sound = pygame.mixer.Sound('assets/Sounds/awp.wav')
        self.bullet = pygame.image.load('assets/images/awp_ammo.png')
        self.bullet = pygame.transform.scale(self.bullet, (15, 44))
        Gun.__init__(self, display, width, height)


class Bow(Gun):
    def __init__(self, display, width, height):
        self.ammo = 1
        self.clip_size = 1
        self.reload_time = 0.2
        self.image = pygame.transform.scale(pygame.image.load('assets/images/arrow_aim.png'), (10, 11))
        self.sound = pygame.mixer.Sound('assets/Sounds/arrow.wav')
        self.bullet = pygame.image.load('assets/images/arrow.png')
        self.bullet = pygame.transform.scale(self.bullet, (40, 40))
        Gun.__init__(self, display, width, height)