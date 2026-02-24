import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)         
ax.set_ylim(-2, 2)         
ax.set_title("Progressive Line Animation")
ax.grid(True, linestyle='--', alpha=0.6)


line, = ax.plot([], [], 'b-', lw=2) 
point, = ax.plot([], [], 'ro')      

x_data = []
y_data = []


def update(frame):

    x = frame
    
    if len(y_data) == 0:
        y = 0
    else:
       
        y = y_data[-1] + np.random.uniform(-0.3, 0.3)
        y = np.clip(y, -1.8, 1.8) 
        
    x_data.append(x)
    y_data.append(y)
    

    line.set_data(x_data, y_data)
    point.set_data([x], [y])
    
    return line, point

frames = np.linspace(0, 10, 100)
ani = FuncAnimation(fig, update, frames=frames, blit=True, interval=50)


plt.show()