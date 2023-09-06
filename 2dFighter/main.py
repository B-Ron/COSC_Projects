import pygame
from pygame import mixer
from fighter import Fighter

mixer.init()
pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colors
YELLOW = (255,255,0)
RED = (255,0,0)
WHITE = (255,255,255) 

#define game varibles
intro_count =3 
last_count_update = pygame.time.get_ticks()
score = [0,0] #player scores: [p1,p2]
round_over = False
round_over_cooldown = 2000

#define fighter varibales
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]

WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA  = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

#load music and sound effects
pygame.mixer.music.load(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\audio\music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\audio\sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\audio\magic.wav")
magic_fx.set_volume(0.75)


#load background image
bg_image = pygame.image.load(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\images\background\background.jpg").convert_alpha()

#load sritesheets
wizard_sprite = pygame.image.load(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\images\Wizard\wizard.png").convert_alpha()
warrior_sprite = pygame.image.load(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\images\Warrior\warrior.png").convert_alpha()

#load vicorty image
victory_img = pygame.image.load(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\icons\victory.png").convert_alpha()

#define sprite frames
WARRIOR_ANIMATION_FRAMES = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_FRAMES = [8, 8, 1, 8, 8, 3, 7]

#define font
count_font = pygame.font.Font(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\fonts\turok.ttf", 80)
score_font = pygame.font.Font(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\fonts\turok.ttf", 30)

#function for text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#drawing health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x  - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

#create two instances for fighters

fighter1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sprite, WARRIOR_ANIMATION_FRAMES, sword_fx)
fighter2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sprite, WIZARD_ANIMATION_FRAMES, magic_fx)

#game loop
run = True
while run:
    clock.tick(FPS)
    
    #draw background
    draw_bg()
    
    #show player stats
    draw_health_bar(fighter1.health, 20, 20)
    draw_health_bar(fighter2.health, 580, 20)
    draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
    draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)


    #update countdown
    if intro_count <= 0:
        #move fighters
        fighter1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter2, round_over)
        fighter2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter1, round_over)
    
    else:
        #display count timer
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 )
        #update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()
        
    
    #update fighters
    fighter1.update()
    fighter2.update()
    
    #draw fighters
    fighter1.draw(screen)
    fighter2.draw(screen)
    
    #check for player defeat
    if round_over == False:
        if fighter1.alive == False:
            score[1] += 1
            round_over = True
            round__over_time = pygame.time.get_ticks()
    
        elif fighter2.alive == False:
            score[0] += 1
            round_over = True
            round__over_time = pygame.time.get_ticks()
    else:
        #display victory image
        screen.blit(victory_img,(360,150))
        if pygame.time.get_ticks() - round__over_time > round_over_cooldown:
            round_over = False
            intro_count = 3
            fighter1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sprite, WARRIOR_ANIMATION_FRAMES, sword_fx)
            fighter2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sprite, WIZARD_ANIMATION_FRAMES, magic_fx)
            
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #update display
    pygame.display.update()
            
#quit game
pygame.quit()