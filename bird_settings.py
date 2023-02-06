import pygame

start = False
FPS = 30
screen_width, screen_height = 400, 600
score = store = 0

speed = 19
gravtiy = 2.5
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

IMAGES = SOUNDS = {}

BIRDS = (
    (
        pygame.image.load('sprites/bluebird-upflap.png').convert_alpha(),
        pygame.image.load('sprites/bluebird-midflap.png').convert_alpha(),
        pygame.image.load('sprites/bluebird-downflap.png').convert_alpha()
        
    ),
    (
        pygame.image.load('sprites/redbird-upflap.png').convert_alpha(),
        pygame.image.load('sprites/redbird-midflap.png').convert_alpha(),
        pygame.image.load('sprites/redbird-downflap.png').convert_alpha(),
    ),
    (
        pygame.image.load('sprites/yellowbird-upflap.png').convert_alpha(),
        pygame.image.load('sprites/yellowbird-midflap.png').convert_alpha(),
        pygame.image.load('sprites/yellowbird-downflap.png').convert_alpha(),
    ) 
)

PIPES = (
    pygame.image.load('sprites/pipe-green.png').convert_alpha(),
    pygame.image.load('sprites/pipe-red.png').convert_alpha()
)

IMAGES['numbers'] = (
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

SOUNDS['die']    = pygame.mixer.Sound('audio/die.wav')
SOUNDS['hit']    = pygame.mixer.Sound('audio/hit.wav')
SOUNDS['point']  = pygame.mixer.Sound('audio/point.wav')
SOUNDS['swoosh'] = pygame.mixer.Sound('audio/swoosh.wav')
SOUNDS['wing']   = pygame.mixer.Sound('audio/wing.wav')




BACKGROUND = pygame.image.load('sprites/background-day.png').convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND, (screen_width, screen_height))
BEGIN_IMAGE = pygame.image.load('sprites/message.png').convert_alpha()

pipe_colour = ["Green"] * 4 + ["Red"]
direction_list = ["Up", "Down"]

pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer, 1500)

lvl_up_timer = pygame.USEREVENT + 2
pygame.time.set_timer(lvl_up_timer, 8000)

    

    



