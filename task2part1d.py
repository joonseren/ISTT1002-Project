import math
import numpy as np
import matplotlib.pyplot as plt

# Definerer variabler
l1 = 60 
l2 = 50 
theta1 = 20
theta2 = -30
sigma1 = 1
sigma2 = 0.5 
pi_over_180 = math.pi / 180 

# Regner ut forventet posisjon til enden av robotarmen
xend = l1 * math.cos(theta1 * pi_over_180) + l2 * math.cos((theta1 + theta2) * pi_over_180)
yend = l1 * math.sin(theta1 * pi_over_180) + l2 * math.sin((theta1 + theta2) * pi_over_180)


# Regner ut de partiellderiverte
X_theta1 = -pi_over_180 * l1 * math.sin(pi_over_180 * theta1) - pi_over_180 * l2 * math.sin(pi_over_180 * (theta1 + theta2))
X_theta2 = -pi_over_180 * l2 * math.sin(pi_over_180 * (theta1 + theta2))
Y_theta1 = -pi_over_180 * l1 * math.cos(pi_over_180 * theta1) - pi_over_180 * l2 * math.cos(pi_over_180 * (theta1 + theta2))
Y_theta2 = -pi_over_180 * l2 * math.cos(pi_over_180 * (theta1 + theta2))