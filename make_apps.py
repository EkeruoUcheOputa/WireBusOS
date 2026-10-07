import os

apps = [
("01-solar-pv", "Solar PV Suite", "solar_pv_suite.py", "Solar PV Generation", "#ffaa00", "Panel Area (sq.m):", "15.0", "Irradiance:", "5.5", "v1 * v2 * 0.78", "kWh/day"),
("02-wind-energy", "Wind Energy Suite", "wind_energy_suite.py", "Wind Turbine Power", "#00aaff", "Swept Area (sq.m):", "200.0", "Wind Speed:", "12.0", "0.5 * 1.225 * v1 * (v2**3) * 0.42 / 1000", "kW"),
("03-microgrid", "Grid Suite", "grid_suite.py", "Microgrid Flow", "#00cc66", "Generation (kW):", "500.0", "Load (kW):", "420.0", "v1 - v2", "kW Net"),
("04-battery", "Battery Suite", "battery_suite.py", "BESS Capacity", "#9933ff", "Capacity (kWh):", "250.0", "Max DoD (%):", "80.0", "v1 * (v2 / 100.0) * 0.9", "kWh Usable"),
("05-building", "Building Suite", "building_suite.py", "Thermal Load", "#ff5050", "Area (sq.m):", "350.0", "Temp Delta:", "15.0", "v1 * v2 * 1.2 / 1000", "kW HVAC"),
("06-scada", "SCADA Suite", "scada_suite.py", "IoT Telemetry", "#00ffff", "Nominal V:", "415.0", "Measured V:", "402.0", "abs(v1 - v2) / v1 * 100", "% Deviation"),
("07-cad", "CAD Suite", "cad_suite.py", "PCB Trace", "#ff9900", "Current (A):", "3.5", "Length (mm):", "50.0", "(1.72e-5 * v2) / (v1 + 0.001)", "mOhm"),
("08-sim", "Simulation Suite", "sim_suite.py", "Dynamic System", "#3399ff", "Initial Value:", "100.0", "Time Const:", "5.0", "v1 * 2.718 ** (-1.0 / max(v2, 0.1))", "Metric"),
("09-gis", "GIS Suite", "gis_suite.py", "Site Suitability", "#33cc33", "Slope (deg):", "4.5", "Resource Index:", "88.5", "(100.0 - v1) * (v2 / 100.0)", "% Index"),
("10-reliability", "Reliability Suite", "rel_suite.py", "Grid Reliability", "#cc33ff", "Interrupted:", "1200", "Total Cust:", "15000", "(v1 / max(v2, 1)) * 100", "Rate"),
("11-ev", "EV Suite", "ev_suite.py", "EV Fleet Demand", "#ff3399", "Fleet Size:", "25", "Charger (kW):", "50.0", "v1 * v2 * 0.85", "kW Peak"),
("12-forecast", "Forecast Suite", "forecast_suite.py", "Demand Forecast", "#00e6e6", "Peak (kW):", "1250.0", "Growth (%):", "6.5", "v1 * (1.0 + (v2 / 100.0))", "kW Peak"),
("13-finance", "Finance Suite", "finance_suite.py", "LCOE & NPV", "#ffd700", "Capital ($):", "150000", "Cash Flow ($):", "32000", "(v2 * 15) - v1", "$ NPV"),
("14-carbon", "Carbon Suite", "carbon_suite.py", "Carbon Audit", "#ff6666", "Saved (kWh):", "45000", "Emission Factor:", "0.45", "v1 * v2 / 1000.0", "tCO2e")
]

os.makedirs("/opt/WireBusOS/modules", exist_ok=True)
os.makedirs("/etc/skel/Desktop", exist_ok=True)

for app in apps:
dir_name, name, file_name, title, color, lbl1, def1, lbl2, def2, expr, unit = app
d = f"/opt/WireBusOS/modules/{dir_name}"
os.makedirs(d, exist_ok=True)

code = "import tkinter as tk\n"
code += "from tkinter import messagebox\n\n"
code += "class App(tk.Tk):\n"
code += "    def __init__(self):\n"
code += "        super().__init__()\n"
code += f'        self.title("{title}")\n'
code += '        self.geometry("580x480")\n'
code += f'        self.configure(bg="#1e1e1e")\n\n'
code += f'        hdr = tk.Frame(self, bg="{color}", height=65)\n'
code += "        hdr.pack(fill=tk.X)\n"
code += f'        tk.Label(hdr, text="{title}", bg="{color}", fg="white", font=("Arial", 14, "bold")).pack(pady=18, padx=20, anchor="w")\n\n'
code += '        f = tk.LabelFrame(self, text=" Parameters ", bg="#1e1e1e", fg="white", font=("Arial", 10, "bold"))\n'
code += '        f.pack(fill=tk.X, padx=20, pady=20)\n\n'
code += f'        tk.Label(f, text="{lbl1}", bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="w", padx=15, pady=10)\n'
code += '        self.e1 = tk.Entry(f, width=15)\n'
code += f'        self.e1.insert(0, "{def1}")\n'
code += '        self.e1.grid(row=0, column=1, padx=15, pady=10)\n\n'
code += f'        tk.Label(f, text="{lbl2}", bg="#1e1e1e", fg="white").grid(row=1, column=0, sticky="w", padx=15, pady=10)\n'
code += '        self.e2 = tk.Entry(f, width=15)\n'
code += f'        self.e2.insert(0, "{def2}")\n'
code += '        self.e2.grid(row=1, column=1, padx=15, pady=10)\n\n'
code += f'        tk.Button(self, text="Run Calculation", command=self.calc, bg="{color}", fg="white", font=("Arial", 10, "bold"), width=25, height=2).pack(pady=10)\n\n'
code += '        self.res = tk.Label(self, text="Status: Ready", bg="#2d2d2d", fg="#00ffcc", font=("Consolas", 11, "bold"), width=55, height=3, relief=tk.SUNKEN)\n'
code += '        self.res.pack(padx=20, pady=10)\n\n'
code += "    def calc(self):\n"
code += "        try:\n"
code += "            v1 = float(self.e1.get())\n"
code += "            v2 = float(self.e2.get())\n"
code += f"            val = {expr}\n"
code += f'            self.res.config(text=f"Result: {{val:,.2f}} {unit}")\n'
code += "        except Exception:\n"
code += '            messagebox.showerror("Error", "Invalid numeric input.")\n\n'
code += "if __name__ == '__main__':\n"
code += "    App().mainloop()\n"

with open(f"{d}/{file_name}", "w") as sf:
    sf.write(code)

desktop = f"[Desktop Entry]\nVersion=1.0\nType=Application\nName=WireBusOS - {name}\nExec=python3 /opt/WireBusOS/modules/{dir_name}/{file_name}\nIcon=utilities-terminal\nPath=/opt/WireBusOS/modules/{dir_name}/\nStartupNotify=false\nTerminal=false\nCategories=Development;Education;Science;\n"
path = f"/etc/skel/Desktop/wirebus-{dir_name}.desktop"
with open(path, "w") as df:
    df.write(desktop)
os.chmod(path, 0o755)

print("All 14 apps successfully created!")
