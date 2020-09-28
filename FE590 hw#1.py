from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0,2)
y = (x*np.pi)
plt.plot(y,np.sin(y))
plt.plot(y,np.cos(y))
plt.show()

