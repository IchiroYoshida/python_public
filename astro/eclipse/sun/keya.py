import ephem
import math
#from operator import itemgetter
import pygame


WIDTH = 640
HEIGHT = 480
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
BLUE  = (  0,  0,255)

def check_non_zero(x):
    return x > 0

# Date
timetuple = (2009, 7, 22, 0, 00, 00)

# Location
gatech = ephem.Observer()
gatech.lon, gatech.lat = '130.198', '33.637' #Keya, Itoshima, Fukuoka,  Japan
gatech.date=timetuple

# Objects
sun, moon = ephem.Sun(), ephem.Moon()

# Output list
results=[]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
myclock = pygame.time.Clock()

for x in range(0,11000):
    screen.fill(BLUE)

    gatech.date= (ephem.date(ephem.date(timetuple)+x*ephem.second))
    sun.compute(gatech)
    moon.compute(gatech)
    r_sun=sun.size/2
    r_moon=moon.size/2
    s=math.degrees(ephem.separation((sun.az, sun.alt), (moon.az, moon.alt)))*60*60
    az = int ((sun.az - moon.az) * 10000) + 320    # X
    alt = int ((sun.alt - moon.alt) * 10000) + 240 # Y
    r_sun2 = int (r_sun * .1)
    r_moon2 = int (r_moon * .1)

    #Sun
    pos = (320, 240)
    radius = r_sun2
    pygame.draw.circle(screen, WHITE, pos, radius)

    #Moon
    pos = (az, alt)
    radius = r_moon2
    pygame.draw.circle(screen, BLACK, pos, radius)

    pygame.display.update()

endflag = 0

while endflag == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: endflag = 1
    myclock.tick(60)


pygame.quit()
