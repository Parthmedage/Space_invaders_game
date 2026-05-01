import pygame
import math
import random
pygame.init()
from pygame import mixer

gamewindow = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

backgroundImg = pygame.image.load('ba.jpg')

icon = pygame.display.set_icon(pygame.image.load('spaceship.png'))

playerImg = pygame.image.load('player.png') 
playerX = 368
playerY = 480
playerX_change = 0

def player(x,y):
    gamewindow.blit(playerImg, (x, y))
number_of_enemies = 6
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(50)
    enemyX_change.append(-0.5)
    enemyY_change.append(40)

def enemy1(x,y,i): 
    gamewindow.blit(enemyImg[i], (x, y))



bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 1.2
bullet_state = "ready"

def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    gamewindow.blit(bulletImg, (x +16, y+10))

def isCollision(enemy1X, enemy1Y, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemy1X - bulletX, 2)) + (math.pow(enemy1Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
# SHOW SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scoreX = 10
scoreY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    gamewindow.blit(score, (x, y))
def game_over_text():
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    gamewindow.blit(over_text, (200, 250))

# Background Sound
mixer.music.load('background.mp3')
mixer.music.play(-1)


# Game Loop
running = True

while running: 
    gamewindow.fill((0, 0, 0))
    gamewindow.blit(backgroundImg, (0, 0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change=playerX_change -0.7
            if event.key == pygame.K_RIGHT:
                playerX_change=playerX_change +0.7
            if event.key == pygame.KEYUP:
                playerX_change = 0
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound('lazer.mp3')
                    bulletSound.play()
                    bulletX = playerX
                    bullet(bulletX, bulletY)
        
        
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    for i in range(number_of_enemies):
        if enemyX[i] <= 0:
            enemyX_change[i] = +0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]
        enemyX[i] += enemyX_change[i]
    
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound('exp.mp3')
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = 50
            score_value += 1 
        enemy1(enemyX[i], enemyY[i], i)
    
    
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    show_score(scoreX, scoreY)
    if enemyY[i] > 440:
        for j in range(number_of_enemies):
            enemyY[j] = 2000
        game_over_text()
        
    

    playerX += playerX_change
    player(playerX, playerY)
    
    pygame.display.update() 
    
  