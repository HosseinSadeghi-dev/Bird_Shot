import pygame
import random
import os
import Gun
import Bird
import threading


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

    def choose_gun(self):
        pygame.init()
        font = pygame.font.Font('assets/fonts/arial.ttf', 40)

        awp = font.render('1- AWP', True, (255, 255, 255))
        awp_box = awp.get_rect(center=(self.width / 2, self.height / 2 - 100))

        shotgun = font.render('2- Shotgun', True, (255, 255, 255))
        shotgun_box = shotgun.get_rect(center=(self.width / 2, self.height / 2 - 50))

        bow = font.render('3- Bow', True, (255, 255, 255))
        bow_box = bow.get_rect(center=(self.width / 2, self.height / 2 + 0))

        rand = font.render('4- Random', True, (255, 255, 255))
        random_box = rand.get_rect(center=(self.width / 2, self.height / 2 + 50))

        txt_1 = font.render(f"Esc To Exit", True, (255, 255, 255))
        text_1 = txt_1.get_rect(center=(self.width / 2, self.height / 2 + 120))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == 1073741913:
                        return 1
                    elif event.key == pygame.K_2 or event.key == 1073741914:
                        return 2
                    elif event.key == pygame.K_3 or event.key == 1073741915:
                        return 3
                    elif event.key == pygame.K_4 or event.key == 1073741916:
                        return random.choice([1, 2, 3])
                    elif event.key == pygame.QUIT:
                        exit()

            self.display.blit(awp, awp_box)
            self.display.blit(shotgun, shotgun_box)
            self.display.blit(bow, bow_box)
            self.display.blit(rand, random_box)
            self.display.blit(txt_1, text_1)
            pygame.display.update()

    def play(self):
        pygame.mouse.set_visible(False)

        gun_choice = self.choose_gun()
        if gun_choice == 1:
            gun = Gun.AWP(self.display, self.width, self.height)
        elif gun_choice == 2:
            gun = Gun.Shotgun(self.display, self.width, self.height)
        elif gun_choice == 3:
            gun = Gun.Bow(self.display, self.width, self.height)
        birds = []

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    gun.x = pygame.mouse.get_pos()[0]
                    gun.y = pygame.mouse.get_pos()[1]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if gun.ammo > 0 and not gun.reloading:
                        gun.fire(birds)
                    else:
                        pygame.mixer.Sound('assets/Sounds/empty_clip.wav').play()
                if (event.type == 771) and (gun.ammo <= gun.clip_size / 2):
                    thread = threading.Thread(target=gun.reload, daemon=True)
                    thread.start()

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

            if gun.ammo <= gun.clip_size / 2:
                if gun.reloading:
                    reload = self.font.render(f"RELOADING ...", True, (255, 0, 0))
                else:
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
