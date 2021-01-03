# pocker game
import pygame
import random

WIDTH = 640
HEIGHT = 480
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
CARDW = 30
CARDH = 48
OUTSIDE = 999

class Cardclass(pygame.sprite.Sprite):
  def __init__(self,num):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((CARDW, CARDH))
    self.rect = self.image.get_rect()
    self.num = num

def initcard(): 
  for sp in allgroup.sprites():
    sp.rect.centerx = OUTSIDE
    sp.rect.centery = OUTSIDE
  for pl in range(plmax):
    for i in range(5):
      opened = False
      if pl == plmy: opened = True
      setcard(pl, i, rndcard(), opened)
  sortcard(plmy)

def selectcard(cursor):
  x = cardx(cursor)
  y = cardy(plmy)
  pygame.draw.rect(screen, \
  YELLOW, (x - (50 / 2), y - (68 / 2), 50, 68))
  textimage = efont.render("OK", True, WHITE)
  screen.blit(textimage, \
  (cardx(5) - 14, cardy(plmy) - 10))

def killcard(cursor):
  n = crd[plmy][cursor]
  if n == -1: return  
  sp = allgroup.sprites()
  sp[n].rect.centerx = OUTSIDE - 1  
  sp[n].rect.centery = OUTSIDE - 1
  crd[plmy][cursor] = -1

def showcard():
  for i in range(5):
    if crd[plmy][i] == -1 :
      setcard(plmy, i, rndcard(), True)
  bestlv = bestpl = 0
  for pl in range(plmax):
    lv = getlevel(pl)
    hand[pl] = int(lv)
    if bestlv < lv :
      bestlv = lv
      bestpl = pl
  for pl in range(plmax):
    temp = -100
    if pl == bestpl: temp=300
    prize[pl] = temp
    score[pl] += temp
    for i in range(5):
      setcard(pl, i, -1, True)

def getlevel(pl):
  sortcard(pl)
  strgt = flash = 1  
  mark = int(crd[pl][0] / 13)
  num = crd[pl][0] % 13
  for i in range(1, 5): 
    if (num + i) != (crd[pl][i] % 13): strgt = 0
    if mark != int(crd[pl][i] / 13): flash = 0
  if strgt != 0 and flash != 0 :
    if num == 8: return 9  
    return 8 + (num / 100)  
  pair = card = 0 
  cnt = 1
  for i in range(4):
    n = crd[pl][i]
    n2 = crd[pl][i + 1]
    if (n % 13) == (n2 % 13):
      if cnt == 1: pair += 1
      s = (n % 13) / 100
      cnt += 1
      if card < cnt: card = cnt
    else: cnt = 1  
  if card == 4: return 7 + s
  if card == 3 and pair == 2: return 6 + s
  if flash != 0: return 5 + (num / 100)   
  if strgt != 0: return 4 + (num / 100)   
  if card == 3 and pair == 1: return 3 + s  
  if card == 2 and pair == 2: return 2 + s  
  if card == 2 and pair == 1: return 1 + s  
  return 0  

def result():
  for pl in range(plmax):
    color = BLACK
    if prize[pl] > 0: color = WHITE
    textimage=jfont.render(handname[hand[pl]], \
    True, color)
    screen.blit(textimage, \
    (cardx(0), cardy(pl) + 30))
    textimage = efont.render(str(prize[pl]), \
    True, color)
    screen.blit(textimage,(cardx(5),cardy(pl)))

def cardx(i): return ((i * 48) + 250)
def cardy(pl): return ((4 - pl) * 100)

def setcard(pl, i, n, opened):
  if n == -1: n = crd[pl][i]
  crd[pl][i] = n
  sp = allgroup.sprites()
  sp[n].rect.centerx = cardx(i)
  sp[n].rect.centery = cardy(pl)
  temp = n
  if opened == False: temp = 52
  u = (temp % 13) * CARDW
  v = int(temp / 13) * CARDH
  sp[n].image = \
  pygame.Surface.subsurface(cardimage, \
  (u, v, CARDW, CARDH))

def rndcard():
  sp = allgroup.sprites()
  while 1:
    spn = random.randint(0, 51)
    x = sp[spn].rect.centerx
    y = sp[spn].rect.centery
    if x == OUTSIDE and y == OUTSIDE: break
  return spn

def sortcard(pl):
  sp = allgroup.sprites()
  for i in range(4):
    for i2 in range(i + 1, 5):
      n = crd[pl][i]
      n2 = crd[pl][i2]
      if (n % 13) > (n2 % 13) :
        sp[n].rect.centerx = cardx(i2)  
        sp[n2].rect.centerx = cardx(i)
        crd[pl][i] = n2
        crd[pl][i2] = n
# main
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
myclock = pygame.time.Clock()
efont = pygame.font.Font(None, 32)
jfont = pygame.font.Font("ipag.ttc", 24)
cardimage = pygame.image.load("card.png")
plmy = 0
plmax = 4  
handname = ["ブタ", "ワンペア", "ツーペア", "スリーカード", "ストレート", "フラッシュ", "フルハウス", "フォーカード", "ストレートフラッシュ", "ロイヤルストレートフラッシュ"]
crd = [[0 for i in range(5)] \
for j in range(plmax)]
username = ["YOU", "CPU3", "CPU2", "CPU1"]
score = [1000, 1000, 1000, 1000]
prize = [0, 0, 0, 0]
hand = [0, 0, 0, 0]
allgroup = pygame.sprite.Group()
for i in range(52):
  allgroup.add(Cardclass(i))

seq = cursor = endflag = 0
while endflag==0:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: endflag=1
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT: cursor-=1
      if event.key == pygame.K_RIGHT: cursor+=1
      if event.key == pygame.K_RETURN: seq+=1
  if (cursor < 0): cursor = 0
  if (cursor > 5): cursor = 5
  screen.fill(GREEN)
  if seq == 0:
    initcard()
    seq += 1
  elif seq == 1: selectcard(cursor)
  elif seq == 2:
    if cursor < 5:
      killcard(cursor)
      seq -= 1
    else:
      showcard()
      seq += 1
  elif seq == 3: result()
  elif seq == 4: seq = 0

  allgroup.draw(screen)
  for pl in range(plmax):
    textimage = \
    efont.render(username[pl], True, WHITE)
    screen.blit(textimage, (80, cardy(pl) - 30))
    textimage = efont.render(str(score[pl]), \
    True, YELLOW)
    screen.blit(textimage, (130, cardy(pl)))
  myclock.tick(60)
  pygame.display.flip()
pygame.quit()

