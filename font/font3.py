import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3)
y=x**2

plt.plot(x,y,label='二次曲線')
plt.legend()

plt.show()

