import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
x=np.linspace(0,2*np.pi,200)
line,=ax.plot(x,np.sin(x))

def update(frame):
    line.set_ydata(np.sin(x+frame/10))
    return line,
ani=FuncAnimation(fig,update,frames=100,interval=50,blit=True)

plt.title('sine wave animation')
plt.xlabel('x-axis')
plt.ylabel('y=sin(x)')
plt.grid(True)
plt.show()