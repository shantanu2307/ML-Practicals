import matplotlib.pyplot as plt
import numpy as np

#Plot of sin graph

x=np.arange(0,4*np.pi,0.1)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '-r', label='Cosine')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
plt.legend(framealpha=1, frameon=True)
plt.show()

