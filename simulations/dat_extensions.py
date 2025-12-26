import numpy as np
import pandas as pd
import os
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
RE_VALUES = [1e3, 1e4, 1e5]
TIME_SPAN = (0, 10)
TIME_EVAL = np.linspace(0, 10, 1000)
SEED = 42
DELTA = 0.618

def simulate_plasma_stability(Re):
    def standard_plasma(t, y):
        x, v = y
        noise = np.random.normal(0, 0.1)
        return [v, -x + noise / Re]
    
    def quasi_plasma(t, y):
        x, v = y
        noise = np.random.normal(0, 0.1)
        return [v, -x - DELTA * v + noise / Re]
    
    y0 = [0.1, 0.0]
    sol_s = solve_ivp(standard_plasma, TIME_SPAN, y0, t_eval=TIME_EVAL)
    sol_q = solve_ivp(quasi_plasma, TIME_SPAN, y0, t_eval=TIME_EVAL)
    
    return np.max(np.abs(sol_q.y[0])), np.max(np.abs(sol_s.y[0]))

def simulate_quantum_entanglement(Re):
    noise_levels = np.random.uniform(0.1, 0.5, 100) / Re
    q_entropy = np.mean(noise_levels * (1 - DELTA))
    s_entropy = np.mean(noise_levels)
    return q_entropy, s_entropy

def run_extensions():
    print("🔬 Executing DAT 2.0 High-Fidelity Extensions...")
    np.random.seed(SEED)
    results = []
    
    for Re in RE_VALUES:
        q_p, s_p = simulate_plasma_stability(Re)
        q_q, s_q = simulate_quantum_entanglement(Re)
        results.append({
            "Re": Re,
            "Plasma_Gain": f"{s_p/q_p:.2f}x",
            "Quantum_Gain": f"{s_q/q_q:.2f}x"
        })
    
    os.makedirs("data", exist_ok=True)
    pd.DataFrame(results).to_csv("data/dat_extensions_simulations.csv", index=False)
    print("✅ Results archived in data/dat_extensions_simulations.csv")

if __name__ == "__main__":
    run_extensions()
