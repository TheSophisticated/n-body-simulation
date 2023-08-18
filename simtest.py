import pygame
import sys

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

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("N-Body Simulation")

red = (255, 0, 0)
blue = (0, 0, 255)
radius = 20

particle_1 = Particle(mass=100, pos_x=300, pos_y=300, vel_x=0.5, vel_y=0.3)
particle_2 = Particle(mass=200, pos_x=500, pos_y=300, vel_x=-0.5, vel_y=-0.3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    pygame.draw.circle(screen, red, (int(particle_1.pos_x), int(particle_1.pos_y)), radius)
    pygame.draw.circle(screen, blue, (int(particle_2.pos_x), int(particle_2.pos_y)), radius)
    
    force_x, force_y = calculate_force(particle_1, particle_2)
    update_particle(particle_1, force_x, force_y)
    update_particle(particle_2, -force_x, -force_y)
    
    pygame.display.flip()
    pygame.time.delay(0)

pygame.quit()
