import math

l1 = 60 
l2 = 50 
theta1 = 20
theta2 = -30
sigma1 = 1
sigma2 = 0.5 
pi_over_180 = math.pi / 180 


X_theta1 = -pi_over_180 * l1 * math.sin(pi_over_180 * theta1) - pi_over_180 * l2 * math.sin(pi_over_180 * (theta1 + theta2))
X_theta2 = -pi_over_180 * l2 * math.sin(pi_over_180 * (theta1 + theta2))
Y_theta1 = -pi_over_180 * l1 * math.cos(pi_over_180 * theta1) - pi_over_180 * l2 * math.cos(pi_over_180 * (theta1 + theta2))
Y_theta2 = -pi_over_180 * l2 * math.cos(pi_over_180 * (theta1 + theta2))

varX = X_theta1**2 * sigma1**2 + X_theta2**2 * sigma2**2
varY = Y_theta1**2 * sigma1**2 + Y_theta2**2 * sigma2**2

print(f"Var(X) = {varX}")
print(f"Var(Y) = {varY}")
