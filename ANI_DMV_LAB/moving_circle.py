import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title("Blue Circle Moving Left to Right")

# Create a blue circle patch (initial position x=-6, y=0)
circle = patches.Circle((-6, 0), radius=0.5, color='blue')
ax.add_patch(circle)

# Animation function: updates the center of the circle
def update(frame):
    # 'frame' represents the current x-coordinate
    circle.set_center((frame, 0))
    return circle,

# Define frames: x-coordinates from -6 (off-left) to 6 (off-right)
frames = np.linspace(-6, 6, 80)

# Create animation
# repeat=True (default) ensures the process starts over once finished
ani = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)

# Save the animation as a GIF
ani.save('moving_circle.gif', writer='pillow', fps=30) 
