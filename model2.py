import numpy as np
import matplotlib.pyplot as plt

def lire_parametres(fichier):
    params = {}
    with open(fichier, 'r') as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne or ligne.startswith('#'):
                continue
            cle, valeur = ligne.split('=')
            cle = cle.strip()
            valeur = valeur.strip()
            if ',' in valeur:
                valeur = tuple(map(float, valeur.split(',')))
            elif '.' in valeur or 'e' in valeur.lower():
                valeur = float(valeur)
            else:
                try:
                    valeur = int(valeur)
                except ValueError:
                    pass
            params[cle] = valeur
    return params

# Lecture des paramètres
param = lire_parametres("parametres_f.txt")

# Assignation
A_sol = param["A_sol"]
h = param["h"]
e_mur = param["e_mur"]
lambda_mur = param["lambda_mur"]
rho_mur = param["rho_mur"]
c_p_mur = param["c_p_mur"]
rho_air = param["rho_air"]
c_p_air = param["c_p_air"]
h_int = param["h_int"]

T1_0, T2_0, T3_0, T_int_0 = param["T_init"]
T_ext_base = param["T_ext_base"]
T_ext_ampl = param["T_ext_ampl"]

dt = param["dt"]
t_max = param["t_max"]
N = int(t_max / dt)
t = np.linspace(0, t_max, N)

# Calcul géométrique
A_mur = 2 * (2 * np.sqrt(A_sol)) * h
volume_air = A_sol * h
n_couches = 3
e_couche = e_mur / n_couches
V_couche = A_mur * e_couche
C_mur = rho_mur * c_p_mur * V_couche
R_couche = e_couche / (lambda_mur * A_mur)

C1 = C2 = C3 = C_mur
C_int = volume_air * rho_air * c_p_air + rho_mur * c_p_mur * A_sol * 0.2 + rho_mur * c_p_mur * A_sol * 0.10
R_iso = R12 = R23 = R_couche
R_mur_int = 1 / (h_int * A_mur)

T_ext = lambda t: T_ext_base + T_ext_ampl * np.sin(2 * np.pi * t / 24)

# Initialisation
T1 = np.zeros(N)
T2 = np.zeros(N)
T3 = np.zeros(N)
T_int = np.zeros(N)
T1[0], T2[0], T3[0], T_int[0] = T1_0, T2_0, T3_0, T_int_0

# Simulation
for n in range(N - 1):
    Te = T_ext(t[n])
    dT1 = ((Te - T1[n]) / R_iso - (T1[n] - T2[n]) / R12) / C1
    dT2 = ((T1[n] - T2[n]) / R12 - (T2[n] - T3[n]) / R23) / C2
    dT3 = ((T2[n] - T3[n]) / R23 - (T3[n] - T_int[n]) / R_mur_int) / C3
    dT_int = ((T3[n] - T_int[n]) / R_mur_int) / C_int

    T1[n+1] = T1[n] + dt * 3600 * dT1
    T2[n+1] = T2[n] + dt * 3600 * dT2
    T3[n+1] = T3[n] + dt * 3600 * dT3
    T_int[n+1] = T_int[n] + dt * 3600 * dT_int

# Affichage
plt.figure(figsize=(10,6))
plt.plot(t, T1, label="Mur couche 1 (ext)")
plt.plot(t, T2, label="Mur couche 2")
plt.plot(t, T3, label="Mur couche 3 (int)")
plt.plot(t, T_int, label="Air intérieur")
plt.plot(t, T_ext(t), '--', label="T_ext")
plt.xlabel("Temps (h)")
plt.ylabel("Température (°C)")
plt.title("Modèle thermique générique")
plt.grid()
plt.legend()
plt.show()
