import time
import math
import itertools
from scipy import integrate
import turtle

PI = math.pi
R = 20
V = 3
g = 9.81
P = 4*PI*R/V #period of each "8"
#Thrust

def f(x):
    return V * math.sin(Yaw_velocity * x)
def f2(x):
    return V * math.cos(Yaw_velocity * x)


win = turtle.Screen()

Takeoff = time.process_time()
#for n in itertools.count():
 #   t = time.process_time()- Takeoff
 
while True:
    #turtle.pendown()
    t = time.process_time()- Takeoff
    if int(t / (0.5*P)) % 2 == 0:
       #     2 * n * (0.5 * P) <= t < (2 * n + 1) * (0.5 * P):
        Yaw_velocity = V/R #angular velocity
        Roll_angle = math.atan( V**2/(g*R)) #

    #elif (2 * n + 1) * (0.5 * P) <= t < (2 * n + 2) * (0.5 * P):
    else :
        Yaw_velocity = -V/R #angular velocity
        Roll_angle = -math.atan(V**2 / (g*R))

    print(t, Yaw_velocity, Roll_angle)

    X = integrate.quad(f, 0, t)
    Y = integrate.quad(f2, 0, t)
    x = int(X[0] * 10)
    y = int(Y[0] * 10)
    
    turtle.goto(x,y)
    turtle.dot()






