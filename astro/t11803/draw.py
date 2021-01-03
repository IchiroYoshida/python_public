# draw test
import pygame

WIDTH = 640
HEIGHT= 480
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
myclock = pygame.time.Clock()
screen.fill(BLACK)

# line
startpos = (50, 100)
endpos = (150, 200)
pygame.draw.line(screen,WHITE,startpos,endpos) 

# rect
rect = (200, 100, 100, 100)
pygame.draw.rect(screen, RED, rect)

# circle
pos = (400, 150)
radius = 50
pygame.draw.circle(screen, GREEN, pos, radius)

# polygon
poslist = [(500, 200), (550, 100), (600, 200)]
pygame.draw.polygon(screen, BLUE, poslist)

pygame.display.flip()
endflag = 0

while endflag == 0:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: endflag = 1
  myclock.tick(60)

pygame.quit()
