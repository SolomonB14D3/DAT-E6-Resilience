import pandas as pd
import json
import os

def verify_all():
    summary = {}
    
    # Pillar 2 Check
    p2_path = 'data/pillar2/PHASON_STRAIN_ENERGY_LOG.csv'
    if os.path.exists(p2_path):
        p2 = pd.read_csv(p2_path)
        summary['Pillar_2_Resilience'] = "PASS" if not p2.empty else "WARNING: No Slips"
    else:
        summary['Pillar_2_Resilience'] = "FAIL: Missing Log"
    
    # Pillar 4 Check: Smart Column Detection
    p4_path = 'data/THERMAL_CONDUCTIVITY_LOG.csv'
    if os.path.exists(p4_path):
        p4 = pd.read_csv(p4_path)
        # Find column that looks like Conductivity (k)
        k_col = [c for c in p4.columns if c.lower() in ['k', 'conductivity', 'thermal_conductivity']]
        if k_col:
            k_final = p4.iloc[-1][k_col[0]]
            summary['Pillar_4_Thermal'] = "PASS" if 25000 < k_final < 35000 else "FAIL: Out of Bounds"
            summary['Final_Conductivity'] = float(k_final)
        else:
            summary['Pillar_4_Thermal'] = "FAIL: Column Not Found"
    else:
        summary['Pillar_4_Thermal'] = "FAIL: Missing Log"

    with open('SUMMARY_REPORT.json', 'w') as f:
        json.dump(summary, f, indent=4)
    print("\n📋 Summary Report Generated: SUMMARY_REPORT.json")

if __name__ == "__main__":
    verify_all()
