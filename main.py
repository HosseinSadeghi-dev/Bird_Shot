import pygame
import random
import os
import Gun
import Bird


class Game:

    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font('assets/fonts/arial.ttf', 18)
        self.width = 850
        self.height = 480
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('assets/Images/background.jpg')
        self.fps = 60

    def play(self):
        pygame.mouse.set_visible(False)

        gun = Gun.Gun(self.display, self.width, self.height)
        birds = []

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    gun.x = pygame.mouse.get_pos()[0]
                    gun.y = pygame.mouse.get_pos()[1]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if gun.ammo > 0:
                        gun.fire(birds)
                if (event.type == 771) and (gun.ammo < 10):
                    gun.reload()

            if random.random() < 0.05:
                if random.random() <= 0.08:
                    birds.append(Bird.Eagle(self.display, self.width, self.height))
                elif random.random() <= 0.25:
                    birds.append(Bird.Stork(self.display, self.width, self.height))
                else:
                    birds.append(Bird.Duck(self.display, self.width, self.height))

            self.display.blit(self.background, [0, 0])
            gun.show()

            for bird in birds:
                bird.fly()
                if -50 <= bird.x <= self.width + 50:
                    bird.show()
                else:
                    birds.remove(bird)

            score = self.font.render(f"Score: {gun.score}", True, (0, 0, 0))
            score_box = score.get_rect(center=(self.width / 2, self.height - 10))
            self.display.blit(score, score_box)

            ammo = self.font.render(f"X {gun.ammo}", True, (0, 0, 0))
            ammo_box = score.get_rect(center=(70, self.height - 37))
            self.display.blit(gun.bullet, [10, self.height - 60])
            self.display.blit(ammo, ammo_box)

            if gun.ammo < 3:
                reload = self.font.render(f"R To Reload", True, (255, 0, 0))
                reload_box = score.get_rect(center=(self.width - 80, self.height - 37))
                self.display.blit(reload, reload_box)

            pygame.display.update()
            self.clock.tick(self.fps)


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    os.system('cls||clear')
    main()
