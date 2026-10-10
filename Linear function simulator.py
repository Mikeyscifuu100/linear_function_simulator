import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def eqn_line(slope, intercept, x_values):
    y_values = [slope * x + intercept for x in x_values]
    return y_values


# Change these to simulate a different linear function.
slope = 3
intercept = -4

x_values = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_values = eqn_line(slope, intercept, x_values)
print(y_values)

# Extra points make the animation move smoothly.
animated_x = np.linspace(min(x_values), max(x_values), 200)
animated_y = eqn_line(slope, intercept, animated_x)

# Set up the graph.
fig, ax = plt.subplots(figsize=(8, 6))

ax.set_title(f"Linear Function: y = {slope}x {intercept:+g}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(min(x_values) - 1, max(x_values) + 1)

padding = max(1, (max(y_values) - min(y_values)) * 0.1)
ax.set_ylim(min(y_values) - padding, max(y_values) + padding)

ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.grid(True, alpha=0.3)

# Show the original calculated points.
ax.scatter(x_values, y_values, color="gray", label="Calculated points")

# Objects that will change during the animation.
line, = ax.plot([], [], color="blue", linewidth=2, label="Linear function")
point, = ax.plot([], [], "ro", label="Moving point")
coordinates = ax.text(0.03, 0.95, "", transform=ax.transAxes, va="top")

ax.legend(loc="lower right")


def init():
    line.set_data([], [])
    point.set_data([], [])
    coordinates.set_text("")
    return line, point, coordinates


def update(frame):
    # Draw the line up to the current point.
    line.set_data(animated_x[:frame + 1], animated_y[:frame + 1])

    # Move the red point.
    x = animated_x[frame]
    y = animated_y[frame]
    point.set_data([x], [y])

    coordinates.set_text(f"x = {x:.2f}, y = {y:.2f}")
    return line, point, coordinates


animation = FuncAnimation(
    fig,
    update,
    frames=len(animated_x),
    init_func=init,
    interval=30,       # Milliseconds between frames.
    blit=True,
    repeat=True
)

plt.tight_layout()
plt.show()