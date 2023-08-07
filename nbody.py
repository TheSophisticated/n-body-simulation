#Importing Dependencies
import numpy as np
from matplotlib.animation import FuncAnimation
import time

#Time Step and Total Time
dt = 3600
total_time = 24 * 3600

#Creating Classes
class particle:
    def __init__(self, mass, posX, posY):
        self.mass = int(mass)
        self.posX = int(posX)
        self.posY = int(posY)
    
    def __str__(self) -> str:
        return f"({self.mass})"

class vec2:
    def __init__(self, X, Y):
        self.X = int(X)
        self.Y = int(Y)

#Defining Functions
def getMag(x, y):
    mag = ((x**2) + (y**2))**1/2
    return mag

def getForce(radius, mass1, mass2):
    G = 6.67 * (10**-11)
    F = (G * mass1 * mass2) /radius**2
    return F

def getPairForce(Force, radius, yDiff, xDiff):
    Fx = Force * (xDiff/radius) 
    Fy = Force * (yDiff/radius) 
    return Fx, Fy

def getAcc(Fx, Fy, mass):
    Ax = Fx/mass
    Ay = Fy/ mass
    return Ax, Ay

def getVelocity(acc, time, u):

    if time == 0:
        u = 0

    vx = u + (acc*time)
    return vx

#Main Code
list = []

list.append(particle(1.9891e10, 250, 300))
list.append(particle(5.97219e24, 400, 400))


mag1 = getMag(list[0].posX, list[0].posY)
mag2 = getMag(list[1].posX, list[1].posY)

radius = mag1 - mag2
y = list[0].posY - list[1].posY
x = list[0].posX - list[1].posX

Force = getForce(radius, list[0].mass, list[1].mass)

Fpair = vec2(getPairForce(Force, radius, y, x)[0],  getPairForce(Force, radius, y, x)[1])
AccPair = vec2(getAcc(Fpair.X, Fpair.Y, list[0].mass)[0],getAcc(Fpair.X, Fpair.Y, list[0].mass)[1])    