import numpy as np
import matplotlib.pyplot as plt

# === PARAMÈTRES ===
# Températures initiales (en °C)
T_ext_amp = 5                 # amplitude de variation extérieure
T_ext_moy = 5                  # moyenne extérieure (ex: hiver)
T_int_0 = 20                   # température intérieure initiale

# Bâtiment
S = 100                        # surface au sol (m²)
h_bat = 3                      # hauteur du bâtiment (m)
V = S * h_bat                 # volume (m³)
rho_m = 1800                  # densité matériau (kg/m³)
c_m = 840                     # capacité thermique massique (J/kg·K)

# Parois
e = 0.3                       # épaisseur isolant (m)
lambda_iso = 0.04            # conductivité isolant (W/m·K)
h_conv = 8                   # coefficient de convection (W/m²·K)

# === CALCULS PRÉALABLES ===
A_ech = S + 4 * h_bat * np.sqrt(S)   # surface d’échange : murs + toit
m = rho_m * V                       # masse de matériaux
C_tot = m * c_m                     # inertie thermique (J/K)

R_conduct = e / (lambda_iso * A_ech)      # résistance thermique par conduction
R_conv = 1 / (h_conv * A_ech)             # résistance par convection
R_tot = 1 / (1/R_conduct + 1/R_conv)      # association en parallèle

# === SIMULATION TEMPORELLE ===
dt = 60                             # pas de temps (s)
t_max = 1000 * 3600                   # 48 heures
n_steps = int(t_max / dt)

T_int = np.zeros(n_steps)
T_int[0] = T_int_0

temps = np.linspace(0, t_max / 3600, n_steps)  # en heures

def T_ext(t):
    return T_ext_moy + T_ext_amp * np.sin(2 * np.pi * t / (24 * 3600))

for i in range(1, n_steps):
    flux = (T_ext(i * dt) - T_int[i-1]) / R_tot
    dT = (flux * dt) / C_tot
    T_int[i] = T_int[i-1] + dT

# === AFFICHAGE ===
plt.plot(temps, T_int, label="Température intérieure")
plt.plot(temps, T_ext(np.array(temps) * 3600), label="Température extérieure", linestyle='--')
plt.xlabel("Temps (h)")
plt.ylabel("Température (°C)")
plt.legend()
plt.title("Évolution thermique du bâtiment")
plt.grid()
plt.show()
