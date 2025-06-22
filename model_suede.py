# simulation_suede.py
import numpy as np
import matplotlib.pyplot as plt

# === Données géométriques ===
A_sol = 300         # m²
h = 2.5             # m
e_mur = 0.2       # m (épaisseur totale)
lambda_mur = 0.15    # W/m·K (bois sapin)
rho_mur = 1200      # kg/m³
c_p_mur = 2000      # J/kg·K
rho_air = 1.2       # kg/m³
c_p_air = 1000      # J/kg·K
h_int = 9           # W/m²·K

# === Surfaces et volumes ===
A_mur = 2 * (2 * np.sqrt(A_sol)) * h
volume_air = A_sol * h
V_mur_total = A_mur * e_mur

# === Découpage en 3 couches ===
n_couches = 3
e_couche = e_mur / n_couches
V_couche = A_mur * e_couche
C_mur = rho_mur * c_p_mur * V_couche
#Conduction
R_couche = e_couche / (lambda_mur * A_mur)

# === Résistances et capacités ===
C1 = C2 = C3 = C_mur
C_int = volume_air * rho_air * c_p_air + rho_mur * c_p_mur * A_sol * 0.2 +  rho_mur * c_p_mur * A_sol * 0.10
R_iso = R_couche       # résistance vers extérieur
R12 = R23 = R_couche   # résistances internes murales
#Conduco-convection
R_mur_int = 1 / (h_int * A_mur)

# === Simulation ===
dt = 0.1
t_max = 300
N = int(t_max / dt)
t = np.linspace(0, t_max, N)
T_ext = lambda t: 0 + 7 * np.sin(2 * np.pi * t / 24)

# === Initialisation ===
T1 = np.zeros(N)
T2 = np.zeros(N)
T3 = np.zeros(N)
T_int = np.zeros(N)
T1[0] = 3
T2[0] = 8
T3[0] = 13
T_int[0] = 15  # bâtiment chauffé

for n in range(N - 1):
    Te = T_ext(t[n])
    dT1 = ((Te - T1[n]) / R_iso - (T1[n] - T2[n]) / R12) / C1
    dT2 = ((T1[n] - T2[n]) / R12 - (T2[n] - T3[n]) / R23) / C2
    dT3 = ((T2[n] - T3[n]) / R23 - (T3[n] - T_int[n]) / R_mur_int) / C3
    dT_int = ((T3[n] - T_int[n]) / R_mur_int) / C_int

    T1[n+1] = T1[n] + dt*3600 * dT1 
    T2[n+1] = T2[n] + dt*3600 * dT2 
    T3[n+1] = T3[n] + dt*3600 * dT3 
    T_int[n+1] = T_int[n] + dt*3600 * dT_int 

# === Affichage ===
plt.figure(figsize=(10,6))
plt.plot(t, T1, label="Mur couche 1 (ext)")
plt.plot(t, T2, label="Mur couche 2")
plt.plot(t, T3, label="Mur couche 3 (int)")
plt.plot(t, T_int, label="Air intérieur")
plt.plot(t, T_ext(t), '--', label="T_ext")
plt.xlabel("Temps (h)")
plt.ylabel("Température (°C)")
plt.title("Modèle thermique - Maison en Suède")
plt.grid()
plt.legend()
plt.show()