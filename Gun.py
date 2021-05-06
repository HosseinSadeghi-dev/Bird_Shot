import pygame
import time


class Gun:

    def __init__(self, display, width, height):
        pygame.init()
        self.x = width / 2
        self.y = height / 2
        self.display = display
        self.ammo = 10
        # 173 * 513 px --> 15 * 44 px
        self.bullet = pygame.transform.scale(pygame.image.load('assets/Images/bullet.png'), (15, 44))
        # 32 * 32 px
        self.image = pygame.image.load('assets/images/shooter.png')
        self.score = 0
        self.sound = pygame.mixer.Sound('assets/Sounds/shotgun.wav')
        self.sound.set_volume(0.15)

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
        time.sleep(2)
        self.ammo = 10
