import pygame
from random import choice as c, randint as r
from pygame.locals import *
from bird_settings import *

class Bird(pygame.sprite.Sprite):

    def __init__(self, randBird):
        pygame.sprite.Sprite.__init__(self)
        self.idx = 0
        self.speed = speed
        self.randBird = randBird
        self.hitGround = False
        self.angle = 0
        
        self.images =  [
            (BIRDS[self.randBird][0]).convert_alpha(),
            (BIRDS[self.randBird][1]).convert_alpha(),
            (BIRDS[self.randBird][2]).convert_alpha()
        ]

        self.image = self.images[self.idx]
        self.og_image = self.image.copy()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft = (screen_width / 5, screen_height / 2.8))

    def boing(self): 
        if self.rect.bottom >= 0:
            self.speed = -speed 
            SOUNDS['wing'].play()

    def check_hitGround(self):
        if self.rect.bottom >= screen_height - ground_height:
            self.hitGround = True
            SOUNDS['die'].play()

            self.rect.bottom = screen_height - ground_height + 1

    def update(self): 

        if start and not self.hitGround:
            self.speed += gravity
            self.rect.y += self.speed 
    
            self.check_hitGround()

        if not lose:
            self.idx = (self.idx + 1) % 3
            self.image = self.images[self.idx]

        elif self.angle >= -90 and not self.hitGround:
            self.image = pygame.transform.rotozoom(self.og_image, self.angle, 1)
            self.angle -= 15

            self.rect = self.image.get_rect(center = self.rect.center)

class Pipe(pygame.sprite.Sprite):

    def __init__(self, inverted, x_pos, y_pos, colour, direction):
        pygame.sprite.Sprite.__init__(self)

        self.colour = colour
        self.direction = direction
        self.score_counted = False

        if self.colour == "Green":
            self.image = PIPES[0]
        else:
            self.image = PIPES[1]

        self.image = pygame.transform.scale(self.image, (pipe_width, pipe_height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.y = y_pos - self.rect.height
        else:
            self.rect.y = screen_height - y_pos

    def move(self):
        self.rect.x -= game_speed 

        if self.colour == "Red":
            if self.direction == "Up":
                self.rect.y -= pipe_vert_speed
            elif self.direction == "Down":
                self.rect.y += pipe_vert_speed

    def update(self): 
        global score

        if self.rect.x <= - self.rect.width: 
            self.kill()

        if self.rect.left <= 80 and not self.score_counted:
            score += 0.5
            self.score_counted = True

        self.move()
 
class Ground(pygame.sprite.Sprite):
    
    def __init__(self, x_pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('sprites/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (ground_width, ground_height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft = (x_pos, screen_height - ground_height))

    def update(self): 
        if self.rect.x <= - self.rect.width:
            ground_group.empty()
            ground_group.add(Ground(0))
            ground_group.add(Ground(ground_width))

        self.rect.x -= game_speed



def initialise():
    global bird_group, pipe_group, ground_group, bird, background

    background = BACKGROUND[r(0, len(BACKGROUND) - 1)].convert_alpha()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    bird_group = pygame.sprite.Group()
    bird = Bird(r(0, len(BIRDS) - 1))
    bird_group.add(bird)

    pipe_group = pygame.sprite.Group()

    ground_group = pygame.sprite.Group()
    ground1 = Ground(0)
    ground2 = Ground(ground_width)
    ground_group.add(ground1)
    ground_group.add(ground2)

    pygame.time.set_timer(pipe_timer, 1500)
    pygame.time.set_timer(lvl_up_timer, 8000)

def restart(): 
    global start, lose, score, store, speed, game_speed, pipe_vert_speed, bird_group, pipe_group, ground_group, bird, background

    start = False
    lose = False
    score = 0
    store = 0
    speed = 19
    game_speed = 10 
    pipe_vert_speed = 1

    bird_group.empty()
    pipe_group.empty()
    ground_group.empty()
    pygame.event.clear()

    initialise()

def get_random_pipes(x_pos, colour):
    if colour == "Red":
        direction = c(direction_list)
        y_pos = r(200, 300)
    else:
        y_pos = r(100, 380)
        direction = None

    pipe = Pipe(False, x_pos, y_pos, colour, direction)
    inverted_pipe = Pipe(True, x_pos, screen_height - y_pos - pipe_gap, colour, direction)

    pipe_group.add(pipe)
    pipe_group.add(inverted_pipe)

def collision_test():
    global lose

    if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask)
     or pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):

        SOUNDS['hit'].play()

        lose = True

def display_scores():
    global score, store

    score = int(score)
    if score > store:
        store = score
        SOUNDS['point'].play()
        
    score_digits = [int(x) for x in list(str(score))]
    score_width = 0 

    for digit in score_digits:
        score_width += IMAGES[digit].get_width()

    xoffset = (screen_width - score_width) / 2

    for digit in score_digits:
        screen.blit(IMAGES[digit], (xoffset, screen_height * 0.1))
        xoffset += IMAGES[digit].get_width()

def redraw_screen(): # Not optimal

    screen.blit(background, (0, 0))
    bird_group.update()

    if not start: # Beginning
        screen.blit(begin_msg, (110, 150))
        ground_group.update()

    else:
        pipe_group.draw(screen) # Lose/Main Loop

        if not lose: # Main Loop
            pipe_group.update() 
            ground_group.update() 

        else: # Lose
            screen.blit(game_over_msg, (110, 120)) 
        
    ground_group.draw(screen)
    bird_group.draw(screen)



initialise()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()

            elif (event.key == K_SPACE or event.key == K_UP) and not lose:
                bird.boing()
                start = True

            elif event.key == K_RETURN and (lose or not start):
                restart()

        elif start and not lose:
            if event.type == pipe_timer:
                randColour = c(pipe_colour)
                get_random_pipes(screen_width + 300, randColour)

            if event.type == lvl_up_timer:
                if game_speed < max_game_speed:
                    game_speed += 1
                elif game_speed == max_game_speed:
                    pipe_vert_speed = 2

    redraw_screen()

    if start: 
        display_scores()
        
        if not lose: 
            collision_test()

    pygame.display.flip()
