import pygame

start = False
lose = False
FPS = 30
screen_width = 400
screen_height = 600
score = 0
store = 0

gravity = 2.5
speed = 19
game_speed = 10
max_game_speed = 15

pipe_width = 75
pipe_height = 550
pipe_gap = 180
pipe_vert_speed = 1

ground_width = 2 * screen_width
ground_height = 100

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('bird bird')

BIRDS = (
    (
        pygame.image.load('sprites/bluebird-upflap.png'),
        pygame.image.load('sprites/bluebird-midflap.png'),
        pygame.image.load('sprites/bluebird-downflap.png')
        
    ),
    (
        pygame.image.load('sprites/redbird-upflap.png'),
        pygame.image.load('sprites/redbird-midflap.png'),
        pygame.image.load('sprites/redbird-downflap.png'),
    ),
    (
        pygame.image.load('sprites/yellowbird-upflap.png'),
        pygame.image.load('sprites/yellowbird-midflap.png'),
        pygame.image.load('sprites/yellowbird-downflap.png'),
    ) 
)

PIPES = (
    pygame.image.load('sprites/pipe-green.png').convert_alpha(),
    pygame.image.load('sprites/pipe-red.png').convert_alpha()
)

IMAGES = (
    pygame.image.load('sprites/0.png').convert_alpha(),
    pygame.image.load('sprites/1.png').convert_alpha(),
    pygame.image.load('sprites/2.png').convert_alpha(),
    pygame.image.load('sprites/3.png').convert_alpha(),
    pygame.image.load('sprites/4.png').convert_alpha(),
    pygame.image.load('sprites/5.png').convert_alpha(),
    pygame.image.load('sprites/6.png').convert_alpha(),
    pygame.image.load('sprites/7.png').convert_alpha(),
    pygame.image.load('sprites/8.png').convert_alpha(),
    pygame.image.load('sprites/9.png').convert_alpha()
)

SOUNDS = {}

SOUNDS['die']    = pygame.mixer.Sound('audio/die.wav')
SOUNDS['hit']    = pygame.mixer.Sound('audio/hit.wav')
SOUNDS['point']  = pygame.mixer.Sound('audio/point.wav')
SOUNDS['swoosh'] = pygame.mixer.Sound('audio/swoosh.wav')
SOUNDS['wing']   = pygame.mixer.Sound('audio/wing.wav')

BACKGROUND = (
    pygame.image.load('sprites/background-day.png'),
    pygame.image.load('sprites/background-night.png')
)

begin_msg = pygame.image.load('sprites/message.png').convert_alpha()
game_over_msg = pygame.image.load('sprites/gameover.png').convert_alpha()


pipe_colour = ["Green"] * 3 + ["Red"]
direction_list = ["Up", "Down"]

pipe_timer = pygame.USEREVENT + 1
lvl_up_timer = pygame.USEREVENT + 2


    

    



