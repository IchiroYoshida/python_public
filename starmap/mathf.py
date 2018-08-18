import numpy as np

def rnd36(x):
    return(x - np.floor(x /360) * 360)

def rnd99(x):
    x = np.radians(x)
    x = np.sin(x)
    x = np.arcsin(x)
    x = np.degrees(x)
    
    return(x)

if __name__ == '__main__':

    for i in range (-500, 500, 5):
        y = rnd36(i)
        print('rnd36 ',i,y)

    for i in range(-500, 500, 5):
        y = rnd99(i)
        print('rnd99',i,y)
