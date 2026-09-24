import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(0,50,1000)
N = 1
mü = 9.274*10**(-24)
B = 1
k = 1.38*10**(-23)

S = N*k*(np.log(2*np.cosh(mü*B/(k*T))) - np.tanh(mü*B/(k*T))*(mü*B/(k*T)))
C = (mü**2 *B**2 *N/(k*T**2))*(1/np.cosh(mü*B/(k*T)))**2

def Ss(T): 
    return N*k*(np.log(2*np.cosh(mü*B/(k*T))) - np.tanh(mü*B/(k*T))*(mü*B/(k*T)))

def Cc(T):
    return (mü**2 *B**2 *N/(k*T**2))*(1/np.cosh(mü*B/(k*T)))**2


fig, ax = plt.subplots()
ax.plot(T,S, label = "S(T)")
ax.plot(T,C, label = r"$C_B(T)$")
ax.scatter(3.5, Ss(3.5), label = "S(3.5)")
ax.scatter(3.5, Cc(3.5), label = r"$C_B$(3.5)")
ax.grid()
ax.legend()
ax.set_xlabel("Temperature [K]")
ax.set_ylabel(r"S and $C_B$" )
plt.savefig("Plot_S_ans_C_B", dpi= 500)


print(f'S_max is {Ss(50)} and CB_max is 6.043*10^(-24), S(3.5,1) = {Ss(3.5)}, C(3.5,1) = {Cc(3.5)}')
print(f'S(0.6,1) = {Ss(3.5)}, C(0.6,1) = {Cc(0.6)}')