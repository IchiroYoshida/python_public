# shooting game
import pygame
import math
import random

WIDTH = 640
HEIGHT = 480
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
OUTSIDE = 999

class Spclass(pygame.sprite.Sprite):
  def __init__(self, x, y, angle, num):
    pygame.sprite.Sprite.__init__(self)
    tempimage = pygame.transform.rotate( \
    charas[num].image, -angle)
    self.image = tempimage
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y
    self.angle = angle
    self.hp = charas[num].hp
    self.enemy = charas[num].enemy
    self.time = 0

class Explosion(Spclass):
  def update(self):
    if self.time > 10: 
      self.rect.centerx = OUTSIDE

class Shot(Spclass):
  def update(self):
    self.rect.centery -= 8
    hitlist = pygame.sprite.spritecollide( \
    self, allgroup, False)
    for sp in hitlist:
      if sp.enemy==False or sp.hp==99: continue
      self.rect.centerx = OUTSIDE
      sp.hp -= 1
      break

class Fireball(Spclass):
  def update(self):
    rad = math.radians(self.angle - 90)
    self.rect.centerx += (math.cos(rad)) * 4
    self.rect.centery += (math.sin(rad)) * 4

class Player(Spclass):
  def update(self):
    press = pygame.key.get_pressed()
    if(press[pygame.K_UP]): self.rect.centery-=4
    if(press[pygame.K_DOWN]): 
      self.rect.centery += 4
    if(press[pygame.K_LEFT]): 
      self.rect.centerx -= 4
    if(press[pygame.K_RIGHT]): 
      self.rect.centerx += 4
    if(self.rect.centerx < 16): 
      self.rect.centerx = 16
    if(self.rect.centery < 16):
      self.rect.centery = 16
    if(self.rect.centerx > WIDTH - 16 ): 
      self.rect.centerx = WIDTH - 16
    if(self.rect.centery > HEIGHT - 16):
      self.rect.centery = HEIGHT - 16
    if(press[pygame.K_SPACE] != 0) and \
    (self.time % 10==0):
      newsp = Shot( \
      self.rect.centerx,self.rect.centery,0,1)
      allgroup.add(newsp)
    hitlist = pygame.sprite.spritecollide( \
    self, allgroup, False)
    for sp in hitlist:
      if sp.enemy == True:
        self.hp -= 1
        sp.hp -= 1
        break

class Fighter(Spclass):
  def update(self):
    self.rect.centery += 2
    self.rect.centerx += \
    int((self.time % 200) / 100) * 2 - 1
    if allgroup.has(player) == 0 or \
    random.randint(0, 100) !=0: return
    dx = player.rect.centerx - self.rect.centerx
    dy = player.rect.centery - self.rect.centery
    angle = math.degrees(math.atan2(dy,dx))+90
    newsp = Fireball(self.rect.centerx, \
    self.rect.centery, angle, 2)
    allgroup.add(newsp)

class Boss(Spclass):
  def update(self):
    if(self.time < 100):
      self.rect.centery += 1
      return
    rad = math.radians(self.time - 100)
    self.rect.centerx = \
    (WIDTH / 2) + (math.sin(rad) * 200)
    if(self.time % 3 == 0):
      angle = (self.time * 4) % 360
      newsp = Fireball(self.rect.centerx, \
      self.rect.centery, angle, 2)
      allgroup.add(newsp)

class Characlass:
  def __init__(self, filename, hp ,enemy):
    self.image = \
    pygame.image.load(filename).convert()
    colorkey = self.image.get_at((0, 0))
    self.image.set_colorkey(colorkey)
    self.hp = hp
    self.enemy = enemy

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
myfont = pygame.font.Font(None, 48)
myclock = pygame.time.Clock()
charas = []
charas.append(Characlass("chr0.png", 1 ,False))
charas.append(Characlass("chr1.png", 1 ,False)) 
charas.append(Characlass("chr2.png", 99,True)) 
charas.append(Characlass("chr3.png", 1 ,False))
charas.append(Characlass("chr4.png", 1 ,True)) 
charas.append(Characlass("chr5.png", 10,True)) 
stars = []
for i in range(10):
  x = random.randint(0, WIDTH - 1)
  y = random.randint(0, HEIGHT - 1)
  stars.append([x, y, 2, 2])

allgroup = pygame.sprite.Group()
endflag = 0
while endflag == 0:
  allgroup.empty()
  player = Player(WIDTH/2, HEIGHT*3/4, 0 ,3)
  allgroup.add(player)
  bosstimer = 60 * 20
  gameover = 0
  while endflag == 0:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: endflag=1
    screen.fill(BLACK)
    for i in range(len(stars)):
      stars[i][1] = (stars[i][1]+i+1) % HEIGHT
      pygame.draw.rect(screen, WHITE ,stars[i])
    bosstimer -= 1
    if bosstimer==0:
      boss = Boss(WIDTH/2, 0, 180, 5)
      allgroup.add(boss)
    elif bosstimer < 0:
      if allgroup.has(boss)==0: bosstimer=60*20
    elif random.randint(0,100) == 0:
      x = random.randint(0, WIDTH - 200) + 100
      newsp = Fighter(x, 0, 180, 4)
      allgroup.add(newsp)
    allgroup.update()
    for sp in allgroup.sprites():
      sp.time += 1
      x = sp.rect.centerx
      y = sp.rect.centery
      if sp.hp <= 0:
        allgroup.remove(sp)
        newsp = Explosion(x, y, 0, 0)
        allgroup.add(newsp)
      if x<0 or x>WIDTH or y<0 or y>HEIGHT:
        allgroup.remove(sp)
    allgroup.draw(screen)
    if allgroup.has(player)==0:
      imagetext = \
      myfont.render("GAME OVER", True, WHITE)
      screen.blit(imagetext, (230, 200))
      gameover += 1
      if gameover >= 120: break
    myclock.tick(60)
    pygame.display.flip()
pygame.quit()

