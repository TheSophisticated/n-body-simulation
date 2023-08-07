import sys
import pygame
import numpy as np

# Constants (scaled down)
G = 6.67430e-7  # Gravitational constant (m^3/kg/s^2) - Scaled down by a factor of 1e-4
m1 = 1e5       # Mass of body 1 (kg) - Scaled down by a factor of 1e-5
m2 = 1e5       # Mass of body 2 (kg) - Scaled down by a factor of 1e-5

# Initial positions and velocities (scaled down)
r1_init = np.array([-100, 0.0])  # Initial position of body 1 (pixels) - Scaled down by a factor of 1e-2
r2_init = np.array([100, 0.0])   # Initial position of body 2 (pixels) - Scaled down by a factor of 1e-2
v1_init = np.array([0.0, 2])     # Initial velocity of body 1 (pixels/s) - Scaled down by a factor of 1e-1
v2_init = np.array([0.0, -2])    # Initial velocity of body 2 (pixels/s) - Scaled down by a factor of 1e-1

# Time step and total time
dt = 0.01  # Time step (seconds) - Reduced to 0.01 seconds for better accuracy
total_time = 60*60  # Total time to simulate (seconds) - 1 hour

pygame.init()

# Window dimensions
win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("2-Body Simulation using Pygame")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Function to calculate the gravitational force between two bodies
def gravitational_force(r1, r2, m1, m2):
    r12 = r2 - r1
    dist = np.linalg.norm(r12)
    direction = r12 / dist
    force_magnitude = (G * m1 * m2) / (dist**2)
    force = direction * force_magnitude
    return force

# Function to update positions and velocities using Euler's method
def update_positions_and_velocities(r1, r2, v1, v2, m1, m2, dt):
    force = gravitational_force(r1, r2, m1, m2)
    a1 = force / m1
    a2 = -force / m2

    v1 += a1 * dt
    v2 += a2 * dt

    r1 += v1 * dt
    r2 += v2 * dt

    return r1, r2, v1, v2

# Scaling factor for visualization
scale_factor = 100

# Initial positions
r1_init *= scale_factor
r2_init *= scale_factor

# Simulation loop
t = 0
clock = pygame.time.Clock()
while t <= total_time:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    r1_init, r2_init, v1_init, v2_init = update_positions_and_velocities(
        r1_init, r2_init, v1_init, v2_init, m1, m2, dt
    )

    win.fill(black)

    # Draw bodies (scaled up for visualization)
    body1_pos = (int(win_width / 2 + r1_init[0]), int(win_height / 2 + r1_init[1]))
    body2_pos = (int(win_width / 2 + r2_init[0]), int(win_height / 2 + r2_init[1]))
    pygame.draw.circle(win, white, body1_pos, 10)
    pygame.draw.circle(win, white, body2_pos, 10)

    # Update the screen
    pygame.display.flip()
    clock.tick(60)

    t += dt

pygame.quit()
