# blit test
import pygame

WIDTH = 640
HEIGHT= 480
BLUE  = (  0,  0,  255)
BLACK = (  0,  0,    0)
WHITE = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
myfont = pygame.font.Font(None, 32)
myclock = pygame.time.Clock()
image1 = pygame.image.load("man.png").convert()

screen.fill(BLUE)
screen.blit(image1, (0, 0))

for i in range(9):
  angle = i * 45
  pos = (i * 64, 80)
  image2 = pygame.transform.rotate(image1,angle)
  screen.blit(image2, pos)
  pos = (i * 64, 140)
  image2.set_colorkey(BLACK)
  screen.blit(image2, pos)
  imagetext=myfont.render(str(angle),True,WHITE)
  postext = (i * 64, 190)
  screen.blit(imagetext, postext)

pygame.display.flip()
endflag = 0

while endflag == 0:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: endflag = 1
  myclock.tick(60)

pygame.quit ()
