#Julio F. Zanetti
#Algorithm for the drone's arm

import math
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

root= Tk()
w = Label(root, text="Drone Calculator")
w.pack()

import pylab 
F=float((3*9.81)/4) #Force per arm
S1=float(1.3) #Factor os Safety - To admissible tension
S2=float(1.3) #Factor of safety 2 - To flexural strenght
T=float(64.1e+6) #flexural yield strenght (Pa)
ci=float(0.004) #intern side (mm)
b=range(1, 200)
L=[x*10**-3 for x in b] #Arm lenght ]- transform in mm
R=[]

for l in L:
    R.append(ci + 1/2*math.sqrt(1/50709)*math.sqrt\
    (-(2000000*F*S1*S2*ci*l - 50709*(125000000000/285711409*F**2*S1**2*S2**2*l**2/T**2 + 1000000000/857134227*math.sqrt(1/3)\
    *math.sqrt((135224*T*ci**3 + 421875*F*S1*S2*l)*F*S1*S2*l)*F*S1*S2*l/T**2)**(2/3)*T)/((125000000000/285711409*F**2*S1**2*S2**2*l**2/T**2 + \
    1000000000/857134227*math.sqrt(1/3)*math.sqrt((135224*T*ci**3 + 421875*F*S1*S2*l)*F*S1*S2*l)*F*S1*S2*l/T**2)**(1/3)*T)) + \
    1/2*math.sqrt(2000000/50709*F*S1*S2*ci*l/((125000000000/285711409*F**2*S1**2*S2**2*l**2/T**2 + 1000000000/857134227*math.sqrt(1/3)*\
    math.sqrt((135224*T*ci**3 + 421875*F*S1*S2*l)*F*S1*S2*l)*F*S1*S2*l/T**2)**(1/3)*T) + 3000000*math.sqrt(1/50709)*F*S1*S2*l/(T*math.sqrt\
    (-(2000000*F*S1*S2*ci*l - 50709*(125000000000/285711409*F**2*S1**2*S2**2*l**2/T**2 + 1000000000/857134227*math.sqrt(1/3)*math.sqrt\
    ((135224*T*ci**3 + 421875*F*S1*S2*l)*F*S1*S2*l)*F*S1*S2*l/T**2)**(2/3)*T)/((125000000000/285711409*F**2*S1**2*S2**2*l**2/T**2 + 1000000000/857134227*math.sqrt\
    (1/3)*math.sqrt((135224*T*ci**3 + 421875*F*S1*S2*l)*F*S1*S2*l)*F*S1*S2*l/T**2)**(1/3)*T))) - (125000000000/285711409*F**2*S1**2*S2**2*l**2/T**2 + \
    1000000000/857134227*math.sqrt(1/3)*math.sqrt((135224*T*ci**3 + 421875*F*S1*S2*l)*F*S1*S2*l)*F*S1*S2*l/T**2)**(1/3)))
    plot = plt.figure(1)
 
L=np.array(L)
R=np.array(R)

LinC=np.polyfit(L, R, 1)
Lin=[]

for l in L:
    Lin=LinC[0]*L+LinC[1]

plt.plot(L,Lin)
plt.gca().invert_xaxis()
plt.ylabel("Largua \"a\" exterior (m)")
plt.xlabel("Largura do braço (m)")
plt.title("Dimensionamento dos braços",  fontweight='bold')
plt.grid(True)
plt.tight_layout()
pylab.show()


root.mainloop()
