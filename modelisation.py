import numpy as np
import matplotlib.pyplot as plt

# === Données géométriques et physiques ===
A_sol = 50
h = 2.5
e_mur = 0.3
e_iso = 0.1
lambda_iso = 0.04
rho_mur = 2200
c_p_mur = 880
rho_air = 1.2
c_p_air = 1000

volume_air = A_sol * h
A_mur = 2 * (np.sqrt(A_sol) + np.sqrt(A_sol)) * h

C_int = volume_air * rho_air * c_p_air
V_mur = A_mur * e_mur
C_mur = V_mur * rho_mur * c_p_mur
print(C_mur)
R_iso = e_iso / (lambda_iso * A_mur)
R_mur_int = 0.15

# === Simulation avec Euler explicite ===
dt = 0.1  # h
t_max = 72
N = int(t_max / dt)
t = np.linspace(0, t_max, N)

T_ext = lambda t: 10 + 10 * np.sin(2 * np.pi * t / 24)

T_mur = np.zeros(N)
T_int = np.zeros(N)
T_mur[0] = 15
T_int[0] = 20

for n in range(N - 1):
    Te = T_ext(t[n])
    dT_mur = (Te - T_mur[n]) / R_iso - (T_mur[n] - T_int[n]) / R_mur_int
    dT_int = (T_mur[n] - T_int[n]) / R_mur_int
    T_mur[n+1] = T_mur[n] + dt * dT_mur / 1000
    T_int[n+1] = T_int[n] + dt * dT_int / 1000

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
