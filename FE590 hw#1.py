from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0,2)
y = (x*np.pi)
plt.plot(y,np.sin(y))
plt.plot(y,np.cos(y))

plt.plot(a, np.tan(a))
plt.ylim(-1,1)

plt.show()

