import numpy as np
import matplotlib.pyplot as plt

# === Données géométriques et physiques ===
A_sol = 300
h = 2.5
e_mur = 0.6
lambda_iso = 2.2 #pierre calcaire
rho_mur = 2500 #pierre calcaire
c_p_mur = 880 #pierre calcaire
rho_air = 1.2
c_p_air = 1000
h_int = 9

volume_air = A_sol * h

#Calcule surface echange avec l'exterieur

A_mur = 2 * (np.sqrt(A_sol) + np.sqrt(A_sol)) * h


#Calcule des capcités thermiques ainsi que des resistances thermiques
C_int = volume_air * rho_air * c_p_air + rho_mur * c_p_mur * A_sol * 0.2 +  rho_mur * c_p_mur * A_sol * 0.10
V_mur = A_mur * e_mur
C_mur = V_mur * rho_mur * c_p_mur
R_iso = e_mur / (lambda_iso * A_mur)
R_mur_int = 1/(A_mur*h_int)
print(A_mur)
print(R_mur_int)

# === Simulation avec Euler explicite ===
dt = 0.1  # h
t_max = 72
N = int(t_max / dt)
t = np.linspace(0, t_max, N)

T_ext = lambda t: 26 + 7 * np.sin(2 * np.pi * t / 24)

T_mur = np.zeros(N)
T_int = np.zeros(N)
T_mur[0] = 25
T_int[0] = 20

for n in range(N - 1):
    Te = T_ext(t[n])
    dT_mur = (Te - T_mur[n]) / R_iso - (T_mur[n] - T_int[n]) / R_mur_int
    dT_int = (T_mur[n] - T_int[n]) / R_mur_int
    T_mur[n+1] = T_mur[n] + dt*3600 * dT_mur / C_mur
    T_int[n+1] = T_int[n] + dt *3600 *dT_int / C_int

# === Affichage ===
plt.figure(figsize=(10,6))
plt.plot(t, T_mur, label="T_mur (Euler)")
plt.plot(t, T_int, label="T_int (Euler)")
plt.plot(t, T_ext(t), '--', label="T_ext")
plt.xlabel("Temps (h)")
plt.ylabel("Température (°C)")
plt.title("Simulation thermique (Euler explicite)")
plt.grid()
plt.legend()
plt.show()
