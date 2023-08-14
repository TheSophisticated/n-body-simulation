import pygame
import numpy as np
import matplotlib
from timeit import default_timer as timer
import time

#Creating the Particle CLass
class particle:
    def __init__(self, mass, posX, posY):
        self.mass = int(mass)
        self.posX = int(posX)
        self.posY = int(posY)

#Setting parameters (in Kg and meters from origin)
G = 1
u = 0
m1 = 100
m2 = 200
r1_x = 10
r1_y = 15
r2_x = 30
r2_y = 45

#Setting timesteps
TIME = timer()
current = time
dt = 0.1 
total_time = 10*60

#Defining Functions
def getDistanceAndForce(particle1, particle2):
    #Getting Distance and Related Angles
    rx = particle1.posX - particle2.posX
    ry = particle1.posY - particle2.posY
    r = ((rx**2) + (ry**2))**(1/2)
    cos = rx/r
    sin = ry/r

    #Getting Forces and Acceleration
    F = (G * particle1.mass * particle2.mass)/(r**2)
    Fx = F * cos
    Fy = F * sin

    return Fx, Fy

def getAccAndVel(particle, fx, fy):
    Ax = fx / particle.mass
    Ay = fy / particle.mass
    time_step = timer()
    Vx = u + (Ax * (time_step - TIME))
    Vy = u + (Ax * (time_step - TIME))

    rx = particle.posX + Vx * (time_step - TIME)
    ry = particle.posY + Vy * (time_step - TIME)

    TIME = time_step

    return rx, ry



#Creating the Particles/Bodies
body_1 = particle(m1, r1_x, r1_y)
body_2 = particle(m2, r2_x, r2_y)

bodies = [body_1, body_2]

Fx = getDistanceAndForce(body_1, body_2)[0]
Fy = getDistanceAndForce(body_1, body_2)[1]
print(Fy)

end = timer()

for body in bodies:
    while end != 600:
        Rx = getAccAndVel(body, Fx, Fy)[0]
        Ry = getAccAndVel(body, Fx, Fy)[1]
        time.sleep(0.1)

pygame.init()
size = (1600,900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("N-Body Simulation")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()