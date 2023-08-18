import pygame
from timeit import default_timer as timer
import time
import sys

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
r1_x = 1000
r1_y = 1500
r2_x = 0
r2_y = 0
rad = 50
red = (255, 0, 0)
blue = (0, 0, 255)

#Setting timesteps
start = timer()
current = time
dt = 0.1 
total_time = 10*60

#Defining Functions
def getDistanceAndForce(particle1, particle2):
    #Getting Distance and Related Angles
    rx = particle1.posX - particle2.posX
    ry = particle1.posY - particle2.posY
    print(rx, ry)
    r = ((rx**2) + (ry**2))**(1/2)
    if r == 0:
        print("R is 0")
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
    Vx = u + (Ax * dt)
    Vy = u + (Ax * dt)

    rx = particle.posX + Vx * (dt)
    ry = particle.posY + Vy * (dt)

    return rx, ry



#Creating the Particles/Bodies
body_1 = particle(m1, r1_x, r1_y)
body_2 = particle(m2, r2_x, r2_y)

bodies = [body_1, body_2]

pygame.init()
size = (1600,900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("N-Body Simulation")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    pygame.draw.circle(screen, red, (body_1.posX, body_1.posY), rad)
    pygame.draw.circle(screen, blue, (body_2.posX, body_2.posY), rad)
    Fx = getDistanceAndForce(body_1,body_2)[0]
    Fy = getDistanceAndForce(body_1,body_2)[1]      
    print(Fx,Fy)
    #Body - 1:
    body_1.posX = getAccAndVel(body_1, Fx, Fy)[0]
    body_1.posY = getAccAndVel(body_1, Fx, Fy)[1]

    #Body - 2
    body_2.posX = getAccAndVel(body_1, Fx, Fy)[0]
    body_2.posY = getAccAndVel(body_1, Fx, Fy)[1]

    
       
pygame.quit() 
                
    

