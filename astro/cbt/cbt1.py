from numpy.random import *
from numpy import *
import numpy as np

A = np.array(range(3000))
print(A)


B1 = random.choice(A, 100, replace=False)

ALL = np.copy(B1)

for n in range(20):
    B2 = random.choice(A, 100, replace=False)

    C = np.hstack((ALL,B2))
    D = C.tolist()

    Dup = [ x for x in set(D) if D.count(x) > 1]
    print('Count = ',n+2, 'Dups = ',len(Dup))

    ALL = np.copy(C)
