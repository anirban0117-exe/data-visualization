import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].plot(x, y1)
ax[0].set_title("Sine Wave")

ax[1].plot(x, y2)
ax[1].set_title("Cosine Wave")

plt.tight_layout()
plt.show()

