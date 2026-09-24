import numpy as np
import matplotlib.pyplot as plt

Eps = 1
N = 50
k = 1.38*10**(-23)

def U(q,Eps):
    return q*Eps

U_arr = np.array([U(q, Eps) for q in range(2*N)]) 
q_arr = np.array([q for q in range(2*N)]) 

#as Eps = 1 => U = q 

S_arr = k * N * np.log((N+q_arr)/N) + k * q_arr * np.log((N+q_arr)/q_arr)

fig, ax = plt.subplots(2,1)
ax[0].plot(q_arr, S_arr, label = "S(q)", color = "darkblue")
ax[1].plot(q_arr, U_arr, label = "U(q)", color = "darkgreen")
ax[0].set_title("S(q) vs q")
ax[1].set_title("U(q) vs q")
ax[0].legend()
ax[1].legend()
ax[0].grid() 
ax[1].grid() 
ax[0].set_xlabel("q") 
ax[1].set_xlabel("q")
ax[0].set_ylabel("S(q)")
ax[1].set_ylabel("U(q)")
plt.savefig("einstein", dpi = 500)

T_arr = (U_arr[1:] - U_arr[:-1])/(S_arr[1:] - S_arr[:-1])
U_arr = U_arr[1:]
C_arr = (U_arr[1:] - U_arr[:-1])/(T_arr[1:] - T_arr[:-1])

fig, ax = plt.subplots(2,1, figsize = (10,14))
ax[0].plot(q_arr[1:], T_arr, label = "T(q)", color = "darkred")
ax[0].set_title("T(q) vs q")
ax[1].set_title("C(q) vs q")
ax[0].legend()
ax[0].grid()
ax[0].set_xlabel("q")
ax[0].set_ylabel("T(q)")
ax[1].plot(q_arr[1:-1], C_arr, label = "C(q)", color = "darkorange")
ax[1].grid()
ax[1].set_xlabel("q")
ax[1].set_ylabel("C(q)")
plt.savefig("einstein_T", dpi = 500)

T = np.logspace(-3,23, 1000)
C = N*Eps**2/(k*T**2)*np.exp(Eps/(k*T))/(np.exp(Eps/(k*T))-1)**2
S = N*k*(Eps/(k*T)/(np.exp(Eps/(k*T))-1) - np.log(1-np.exp(-Eps/(k*T))))

fig, ax = plt.subplots(2,1, figsize = (10,14))
ax[0].plot(T, S, label = "S(T)", color = "darkblue")
ax[0].set_title("S(T) vs T")
ax[1].set_title("C(T) vs T")
ax[0].legend()
ax[0].grid()
ax[0].set_xlabel("T")
ax[0].set_ylabel("S(T)")
ax[1].plot(T, C, label = "C(T)", color = "darkgreen")
ax[1].grid()
ax[1].set_xlabel("T")
ax[1].set_ylabel("C(T)")
plt.savefig("einstein_T_C", dpi = 500)