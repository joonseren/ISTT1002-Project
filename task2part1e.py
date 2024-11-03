import math
import numpy as np

l1 = 60 
l2 = 50 
theta1 = 20
theta2 = -30
sigma1 = 1
sigma2 = 0.5 
pi_over_180 = math.pi / 180 


relativtUsikkerhetTheta1 = sigma1/abs(theta1)*100
relativtUsikkerhetTheta2 = sigma2/abs(theta2)*100


X_theta1 = -pi_over_180 * l1 * math.sin(pi_over_180 * theta1) - pi_over_180 * l2 * math.sin(pi_over_180 * (theta1 + theta2))
X_theta2 = -pi_over_180 * l2 * math.sin(pi_over_180 * (theta1 + theta2))
Y_theta1 = -pi_over_180 * l1 * math.cos(pi_over_180 * theta1) - pi_over_180 * l2 * math.cos(pi_over_180 * (theta1 + theta2))
Y_theta2 = -pi_over_180 * l2 * math.cos(pi_over_180 * (theta1 + theta2))

varX = X_theta1**2 * sigma1**2 + X_theta2**2 * sigma2**2
varY = Y_theta1**2 * sigma1**2 + Y_theta2**2 * sigma2**2

posX = l1*np.cos(theta1/180*np.pi)+l2*np.cos((theta1+theta2)/180*np.pi)
posY = l1*np.sin(theta1/180*np.pi)+l2*np.sin((theta1+theta2)/180*np.pi)



relativtUsikkerhetX = math.sqrt(varX)/abs(posX)*100
relativtUsikkerhetY = math.sqrt(varY)/abs(posY)*100


print(f"Relativ usikkerhet theta1: {round(relativtUsikkerhetTheta1, 3)}%")
print(f"Relativ usikkerhet theta2: {round(relativtUsikkerhetTheta2, 3)}%")
print(f"Relativ usikkerhet X: {round(relativtUsikkerhetX, 3)}%")
print(f"Relativ usikkerhet Y: {round(relativtUsikkerhetY, 3)}%")