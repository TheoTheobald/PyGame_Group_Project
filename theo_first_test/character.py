import pygame, os
from settings import *
from projectile import Projectile


class Character(pygame.sprite.Sprite):
    className = "character"

    def __init__(self, pos):
        # Appearance params
        super().__init__()
        self.animations = []  # Declares a blank list to add animations to
        self.facing = 0  # Facing 0 is right, facing 1 is left
        self.frameIndex = 0  # The index of the current animation for the sprite in a list
        self.updateTime = pygame.time.get_ticks()  # Sets the last time the character image changed to the moment that it is instantiated
        self.stance = 0  # Stance 0 is idle, 1 is run, 2 is jump, 3 is dead
        self.getSprites(pos)  # Runs the get sprites function to generate self.image

        # Combat
        self.canShoot = True  # Initially the character is able to shoot, becomes false for a period of time after shooting
        self.shooting = False  # Doesn't start shooting
        self.timeLastShot = pygame.time.get_ticks()  # Time character last shot set
        self.bulletCooldown = 800  # Time between shots for charactre
        self.bulletColour = RED  # Bullet colour - this determines damage for the most part
        self.bulletThickness = 5
        self.bulletSpeed = 14
        self.bulletOffsetXPlus = 50  # How much to the right of the character the bullet is when facing right
        self.bulletOffsetXMinus = -10  # How much to the left of the character the bullet is when facing left
        self.bulletOffsetY = 25  # How far down the sprite the bullet comes out
        self.dead = False  # Keeps track of if the character is alive
        self.scoreGiven = False  # Has the player received score for this character yet - prevents score being attributed multiple times per kill

        # Char movement
        self.direction = pygame.math.Vector2(0, 0)  # Direction of movement for character
        self.speed = 5  # Default character speed
        self.gravity = 1  # Rate of increase in y
        self.jumpSpeed = -18  # Initial speed of jump

    def getSprites(self, pos):  # Creates a 3D array of images for the enemy and playable characters
        rightLeft = ['right', 'left']  # First layer into the the array - right and left
        animationTypes = ['Idle', 'Run', 'Jump', 'Death']  # Second layer into the array - four states of animation
        for j in rightLeft:
            LST = []
            for elem in animationTypes:
                lst = []
                frames = len(os.listdir(
                    f"images/{self.className}/{elem}"))  # Third layer into the array, number of images in that animation loop

                for i in range(frames):
                    img = pygame.image.load(f"images/{self.className}/{elem}/{i}.png")
                    img = pygame.transform.scale(img, (int(img.get_width() * 1.5), int(img.get_height() * 1.5)))
                    if j == 'left':
                        img = pygame.transform.flip(img, True, False)
                    lst += [img]
                LST += [lst]
            self.animations += [LST]  # List of lists of lists
        self.image = self.animations[self.facing][self.stance][
            self.frameIndex]  # Sets the image to the first in the starting array
        self.rect = self.image.get_rect(topleft=pos)  # Assigns rect

    def animatePlayer(self):  # Iterates through all the images in the characters animations array
        timeGap = 100  # Time waited before resetting image
        self.image = self.animations[self.facing][self.stance][
            self.frameIndex]  # Update image to match current stance and frame
        if pygame.time.get_ticks() - self.updateTime > timeGap:  # If time since last update has reached timeGap
            if self.stance == 3 and self.frameIndex == len(
                    self.animations[self.facing][self.stance]) - 1 and self.className == 'player':
                pass
            else:
                self.updateTime = pygame.time.get_ticks()  # Update time since last update
                self.frameIndex += 1  # Move frame forward 1
        if self.frameIndex >= len(self.animations[self.facing][self.stance]):
            if self.stance == 3 and self.className != 'player':  # If stance = dead and not player, delete the sprite
                self.kill()
            self.frameIndex = 0  # if not dead, then start animation loop again

    def shoot(self):  # Function to create a projectile in front of the character
        yPos = self.rect.y + self.bulletOffsetY
        if self.facing == 0:
            Dir = 1
            xPos = self.rect.x + self.bulletOffsetXPlus
        elif self.facing == 1:
            Dir = -1
            xPos = self.rect.x + self.bulletOffsetXMinus
        return Projectile(xPos, yPos, self.bulletThickness, self.bulletColour, Dir, self.bulletSpeed)

    def shootRate(self):  # Determines if enough time has passed since the last bulled shot
        if self.timeLastShot + self.bulletCooldown < pygame.time.get_ticks() and not self.dead:
            self.canShoot = True
        else:
            self.canShoot = False

    def fall(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def die(self):
        if self.health <= 0:
            self.dead = True
            if self.className == 'bigEnemy' or self.className == 'boss':  # Ideally would have made the stances mean the same thing across all characters, to avoid this if
                self.stance = 1
            else:
                self.stance = 3
        if self.dead == True:  # Stops the bodies sliding around the floor
            self.direction.x = 0

    def healthBar(self,
                  scrn):  # Draws two bars above the characters head, one red, one green, green shortens as health depletes
        pygame.draw.rect(scrn, RED, (self.rect.x, self.rect.y - 10, 43, 5))
        pygame.draw.rect(scrn, GREEN, (self.rect.x, self.rect.y - 10, (43 * (self.health / self.totalHealth)), 5))

    def update(self, xShift):  # Update function included in level run function to run required character functions
        self.animatePlayer()
        self.shootRate()
        self.die()
        if self.className != "player":  # Stops the xShift applying to the player, xShift governs screen scrolling
            self.rect.x += xShift
