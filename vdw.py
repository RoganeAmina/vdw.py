import numpy as np
#coefficients de vdw
a=0.3658
b=4.267e-5
T=300
P=50e5
R=8.314
#coefficients de l'équation cubique
A=1
B=-(b+R*T/P)
C=a/P
D=-a*b/P
coeffs=(A,B,C,D)
racine=np.roots(coeffs)
print(coeffs)