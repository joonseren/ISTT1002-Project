import math

l1 = 60 
l2 = 50 
theta1 = 20
theta2 = -30 
pi_over_180 = math.pi / 180 
X_theta1 = -pi_over_180 * l1 * math.sin(pi_over_180 * theta1) - pi_over_180 * l2 * math.sin(pi_over_180 * (theta1 + theta2))
X_theta2 = -pi_over_180 * l2 * math.sin(pi_over_180 * (theta1 + theta2))

print(X_theta1**2)
print(X_theta2**2)