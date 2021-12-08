import os
from settings import *
from projectile import Projectile


class Character(pygame.sprite.Sprite):
    className = "character"

    def __init__(self, pos):
        # Appearance params
        super().__init__()
        self.animations = []
        self.falling = False
        self.facing = 0
        self.frameIndex = 0
        self.updateTime = pygame.time.get_ticks()
        self.stance = 0
        self.getSprites(pos)

        # Combat
        self.canShoot = True
        self.shooting = False
        self.timeLastShot = pygame.time.get_ticks()
        self.bulletCooldown = 1000
        self.bulletColour = RED
        self.dead = False

        # Char movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 1
        self.jumpSpeed = -18

    def getSprites(self, pos):
        rightLeft = ['right', 'left']
        animationTypes = ['Idle', 'Run', 'Jump', 'Death']
        for j in rightLeft:
            LST = []
            for elem in animationTypes:
                lst = []
                frames = len(os.listdir(f"images/{self.className}/{elem}"))

                for i in range(frames):
                    img = pygame.image.load(f"images/{self.className}/{elem}/{i}.png")
                    img = pygame.transform.scale(img, (int(img.get_width() * 1.5), int(img.get_height() * 1.5)))
                    if j == 'left':
                        img = pygame.transform.flip(img, True, False)
                    lst += [img]
                LST += [lst]
            self.animations += [LST]
        self.image = self.animations[self.facing][self.stance][self.frameIndex]
        self.rect = self.image.get_rect(topleft=pos)

    def animatePlayer(self):
        timeGap = 100  # Time waited before resetting image
        self.image = self.animations[self.facing][self.stance][self.frameIndex]  # Update image to match current stance and frame
        if pygame.time.get_ticks() - self.updateTime > timeGap:  # If time since last update has reached timeGap
            self.updateTime = pygame.time.get_ticks()  # Update time since last update
            self.frameIndex += 1  # Move frame forward 1
        if self.frameIndex >= len(self.animations[self.facing][self.stance]):
            if self.stance == 3:
                self.kill()
            self.frameIndex = 0

    def shoot(self):
        if self.facing == 0:
            Dir = 1
            xPos = self.rect.x + 50
            yPos = self.rect.y + 25
        elif self.facing == 1:
            Dir = -1
            xPos = self.rect.x - 10
            yPos = self.rect.y + 25
        return Projectile(xPos, yPos, 5, self.bulletColour, Dir)

    def shootRate(self):
        if self.timeLastShot + self.bulletCooldown < pygame.time.get_ticks() and not self.dead:
            self.canShoot = True
        else:
            self.canShoot = False

    def fall(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if not self.falling:
            self.direction.y += self.jumpSpeed
            self.falling = True
            self.frameIndex = 0
            self.stance = 2

    def die(self):
        if self.health <= 0:
            self.dead = True
            self.stance = 3

    def healthBar(self, scrn):
        pygame.draw.rect(scrn, RED, (self.rect.x, self.rect.y - 10, 43, 5))
        pygame.draw.rect(scrn, GREEN, (self.rect.x, self.rect.y - 10, (43 * (self.health / self.totalHealth)), 5))

    def update(self, xShift):
        self.animatePlayer()
        self.shootRate()
        self.die()
        if self.className != "player":
            self.rect.x += xShift
