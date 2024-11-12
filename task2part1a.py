import numpy as np
from matplotlib import pyplot as plt

# Definerer variabler
l1, l2 = 60, 50
theta1 = 20
theta2 = -30
noise = np.linspace(-2, 2, 21) # Støy i vinklene

# Funksjon som regner ut x-posisjonen til enden av robotarmen
def calc_xend_pos(theta1, theta2, l1, l2):
    xend = l1*np.cos(theta1/180*np.pi)+l2*np.cos((theta1+theta2)/180*np.pi)
    return xend


# Lager tomme lister for x-posisjonene
xTheta1 = []
xTheta2 = []

# For-loop som fyller listene med x-posisjonene
for i in range(len(noise)):
    xTheta1.append(calc_xend_pos(theta1 + noise[i], theta2, l1, l2))
    xTheta2.append(calc_xend_pos(theta1, theta2 + noise[i], l1, l2))

# Plotter x-posisjonen mot støyen i theta1 og theta2
plt.plot(noise, xTheta1, label='theta1')
plt.plot(noise, xTheta2, label='theta2')
plt.xlabel('Støy')
plt.ylabel('x')
plt.title('Sammenligning mellom theta1 og theta2')
plt.legend()
plt.grid(True)
plt.show()
