# ブロック崩し
import pygame
import math

def sgn(a):
  return 1 if a > 0 else -1

WIDTH  = 640  
HEIGHT = 480  
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
YELLOW = (255, 255,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)
colortable = [RED, YELLOW, GREEN]

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
myfont = pygame.font.Font(None, 64)
myclock = pygame.time.Clock()
br = 10         # ボールの半径
paddlew = 96    # パドルの幅
paddleh = 16    # パドルの高さ
blockw = 48     # ブロックの幅
blockh = 24     #ブロックの高さ
endflag = 0

while endflag == 0:
  ballx = WIDTH / 2    # ボールのX座標
  bally = HEIGHT - 170 # ボールのY座標
  bx1 = 2              # ボールの速度（X成分）
  by1 = -2.5           # ボールの速度（Y成分）
  x = WIDTH / 2         
  y = HEIGHT - 64       
  paddle = pygame.Rect(x - (paddlew / 2), \
  y - (paddleh / 2), paddlew, paddleh)
  blocks = []
  for i in range(50):
    x = (i % 10) * (blockw + 4) + 64
    y = int(i / 10) * (blockh + 4) + 64
    blocks.append(pygame.Rect(x, y, blockw, \
    blockh))
  gameover = 0
  while endflag == 0:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: endflag = 1
    press = pygame.key.get_pressed()
    x = paddle.centerx
    if(press[pygame.K_LEFT ]): x -= 8
    if(press[pygame.K_RIGHT]): x += 8
    if x >= (paddlew / 2) \
    and x <= (WIDTH - (paddlew / 2)):
      paddle.centerx = x
    x = ballx + bx1
    y = bally + by1
    if x < br or x > (WIDTH - br): bx1 = -bx1
    if y < br: by1 = -by1
    if y > HEIGHT: gameover += 1
    dx = paddle.centerx - x
    dy = paddle.centery - y
    if dy == 0: dy = 1
    if abs(dx) < (paddlew / 2 + br) \
    and abs(dy) < (paddleh / 2 + br):
      if abs(dx / dy) > (paddlew / paddleh):
        bx1 = -bx1
        ballx = paddle.centerx - sgn(dx) \
        * (paddlew/2 + br)
      else:
        bx1 = -dx / 10
        by1 = -by1
        bally = paddle.centery - sgn(dy) \
        * (paddleh/2 + br)
    for block in blocks:
      dx = block.centerx - x
      dy = block.centery - y
      if dy == 0: dy = 1
      if abs(dx) < (blockw / 2 + br) \
      and abs(dy) < (blockh / 2 + br):
        if abs(dx / dy) > (blockw / blockh):
          bx1 = -bx1
          ballx = block.centerx - sgn(dx) \
          * (blockw / 2 + br)
        else:
          by1 = -by1
          bally = block.centery - sgn(dy) \
          * (blockh / 2 + br)
        blocks.remove(block)
        break
    ballx += bx1
    bally += by1
    screen.fill(BLUE)
    for block in blocks:
      color = colortable[int(block.y / 28) % 3]
      pygame.draw.rect(screen, color, block)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.circle(screen, WHITE, \
    (int(ballx), int(bally)), br)
    if gameover > 0:
      imagetext = \
      myfont.render("GAME OVER", True, WHITE)
      screen.blit(imagetext, (180, 300))
      if gameover > 200: break         
    myclock.tick(60)
    pygame.display.flip()
pygame.quit()

