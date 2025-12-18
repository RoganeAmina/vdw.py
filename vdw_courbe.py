import matplotlib.pyplot as plt
n=2
R=0.08134
V=1
a=3.658
b=0.04267
T_valeurs=[]
P_valeurs=[]
for T in range(300,321,1):
    P=n*R*T/(V-b)-(n**2*a/V**2)
    T_valeurs.append(T)
    P_valeurs.append(P)
plt.plot(T_valeurs,P_valeurs)
plt.xlabel('Température')
plt.ylabel('Pression')
plt.title('Variation de P en fonction de T')
plt.show()