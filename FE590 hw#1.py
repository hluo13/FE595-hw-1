from matplotlib import pyplot as plt
import numpy as np

def assignment1():
    x = np.linspace(0, 2)
    y = (x * np.pi)
    plt.plot(y, np.sin(y))
    plt.plot(y, np.cos(y))
    plt.plot(y, np.tan(y))
    plt.xlim((0, 2 * np.pi))
    plt.ylim((-1, 1))
    plt.show()


if __name__ == "__main__":
    assignment1()