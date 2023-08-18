import pygame
import sys
import matplotlib.pyplot as plt
import numpy as np
import threading
from collections import deque

class Particle:
    def __init__(self, mass, pos_x, pos_y, vel_x=0, vel_y=0):
        self.mass = mass
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

G = 1
dt = 0.05  # Smaller time step for more accurate simulation

def calculate_force(particle1, particle2):
    rx = particle2.pos_x - particle1.pos_x
    ry = particle2.pos_y - particle1.pos_y
    r_squared = rx ** 2 + ry ** 2
    r = r_squared ** 0.5
    
    force = (G * particle1.mass * particle2.mass) / r_squared
    force_x = force * rx / r
    force_y = force * ry / r
    
    return force_x, force_y

def update_particle(particle, force_x, force_y):
    acceleration_x = force_x / particle.mass
    acceleration_y = force_y / particle.mass
    
    particle.vel_x += acceleration_x * dt
    particle.vel_y += acceleration_y * dt
    
    particle.pos_x += particle.vel_x * dt
    particle.pos_y += particle.vel_y * dt

def graph_thread():
  # Set black background
    while True:
        plt.clf()  # Clear the previous plot
        plt.plot(np.arange(len(distances)) * dt, distances)  # X-axis in seconds
        plt.xlabel('Time (s)')
        plt.ylabel('Distance')
        plt.title('Distance vs Time')
        plt.grid(True)
        plt.pause(0.01)

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("N-Body Simulation")

red = (255, 0, 0)
blue = (0, 0, 255)
tail_color_1 = (255, 0, 0, 10)  # Subtle red tail
tail_color_2 = (0, 0, 255, 10)  # Subtle blue tail
radius = 20

# Earth's mass is about 5.972 × 10^24 kg
# Sun's mass is about 1.989 × 10^30 kg
# Earth-Sun distance is about 149.6 million km
particle_1 = Particle(mass=100, pos_x=300, pos_y=300, vel_x=0.5, vel_y=0.3)
particle_2 = Particle(mass=200, pos_x=500, pos_y=300, vel_x=-0.5, vel_y=-0.3)

distances = []  # List to store distances over time

tail_length = 50  # Number of positions to keep in the tail
tail_1 = deque(maxlen=tail_length)
tail_2 = deque(maxlen=tail_length)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    # Update tail positions
    tail_1.append((particle_1.pos_x, particle_1.pos_y))
    tail_2.append((particle_2.pos_x, particle_2.pos_y))
    
    # Draw the tail
    for i, (x, y) in enumerate(tail_1):
        alpha = int(255 * (1 - (i / tail_length)))
        pygame.draw.circle(screen, tail_color_1[:3] + (alpha,), (int(x), int(y)), radius // 3)
    
    for i, (x, y) in enumerate(tail_2):
        alpha = int(255 * (1 - (i / tail_length)))
        pygame.draw.circle(screen, tail_color_2[:3] + (alpha,), (int(x), int(y)), radius // 3)
    
    pygame.draw.circle(screen, red, (int(particle_1.pos_x), int(particle_1.pos_y)), radius)
    pygame.draw.circle(screen, blue, (int(particle_2.pos_x), int(particle_2.pos_y)), radius)
    
    force_x, force_y = calculate_force(particle_1, particle_2)
    update_particle(particle_1, force_x, force_y)
    update_particle(particle_2, -force_x, -force_y)
    
    # Calculate distance and add to the distances list
    distance = np.sqrt((particle_2.pos_x - particle_1.pos_x)**2 + (particle_2.pos_y - particle_1.pos_y)**2)
    distances.append(distance)
    
    pygame.display.flip()
    pygame.time.delay(0)

# Start the graphing thread
graphing_thread = threading.Thread(target=graph_thread)
graphing_thread.start()

pygame.quit()
