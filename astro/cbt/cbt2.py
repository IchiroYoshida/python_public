from numpy.random import *
from numpy import *
import numpy as np

A = np.array(range(3000))

B = random.choice(A, 100, replace=False)
ALL = np.copy(B)

for n in range(999):

    B = random.choice(A, 100, replace=False)
    ALL = np.hstack((ALL,B))

    D = ALL.tolist()

    Dup = [ x for x in set(D) if D.count(x) > 1]
    print('Count = ',n+2, 'Dups = ',len(Dup))
