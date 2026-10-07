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

for a in apps:
    d = f"/opt/WireBusOS/modules/{a[0]}"
    os.makedirs(d, exist_ok=True)
    
    app_code = (
        "import tkinter as tk\n"
        "from tkinter import messagebox\n\n"
        "class App(tk.Tk):\n"
        "    def __init__(self):\n"
        "        super().__init__()\n"
        f"        self.title(\"{a[3]}\")\n"
        "        self.geometry(\"580x480\")\n"
        "        self.configure(bg=\"#1e1e1e\")\n"
        f"        h = tk.Frame(self, bg=\"{a[4]}\", height=65)\n"
        "        h.pack(fill=tk.X)\n"
        f"        tk.Label(h, text=\"{a[3]}\", bg=\"{a[4]}\", fg=\"white\", font=(\"Arial\", 14, \"bold\")).pack(pady=18, padx=20, anchor=\"w\")\n"
        "        f = tk.LabelFrame(self, text=\" Parameters \", bg=\"#1e1e1e\", fg=\"white\", font=(\"Arial\", 10, \"bold\"))\n"
        "        f.pack(fill=tk.X, padx=20, pady=20)\n"
        f"        tk.Label(f, text=\"{a[5]}\", bg=\"#1e1e1e\", fg=\"white\").grid(row=0, column=0, sticky=\"w\", padx=15, pady=10)\n"
        "        self.e1 = tk.Entry(f, width=15)\n"
        f"        self.e1.insert(0, \"{a[6]}\")\n"
        "        self.e1.grid(row=0, column=1, padx=15, pady=10)\n"
        f"        tk.Label(f, text=\"{a[7]}\", bg=\"#1e1e1e\", fg=\"white\").grid(row=1, column=0, sticky=\"w\", padx=15, pady=10)\n"
        "        self.e2 = tk.Entry(f, width=15)\n"
        f"        self.e2.insert(0, \"{a[8]}\")\n"
        "        self.e2.grid(row=1, column=1, padx=15, pady=10)\n"
        f"        tk.Button(self, text=\"Run Calculation\", command=self.calc, bg=\"{a[4]}\", fg=\"white\", font=(\"Arial\", 10, \"bold\"), width=25, height=2).pack(pady=10)\n"
        "        self.res = tk.Label(self, text=\"Status: Ready\", bg=\"#2d2d2d\", fg=\"#00ffcc\", font=(\"Consolas\", 11, \"bold\"), width=55, height=3, relief=tk.SUNKEN)\n"
        "        self.res.pack(padx=20, pady=10)\n\n"
        "    def calc(self):\n"
        "        try:\n"
        "            v1 = float(self.e1.get())\n"
        "            v2 = float(self.e2.get())\n"
        f"            val = {a[9]}\n"
        f"            self.res.config(text=f\"Result: {{val:,.2f}} {a[10]}\")\n"
        "        except:\n"
        "            messagebox.showerror(\"Error\", \"Invalid input.\")\n\n"
        "if __name__ == \"__main__\":\n"
        "    App().mainloop()\n"
    )
    
    with open(f"{d}/{a[2]}", "w") as sf:
        sf.write(app_code)
    
    desk = (
        "[Desktop Entry]\n"
        "Version=1.0\n"
        "Type=Application\n"
        f"Name=WireBusOS - {a[1]}\n"
        f"Exec=python3 /opt/WireBusOS/modules/{a[0]}/{a[2]}\n"
        "Icon=utilities-terminal\n"
        f"Path=/opt/WireBusOS/modules/{a[0]}/\n"
        "StartupNotify=false\n"
        "Terminal=false\n"
        "Categories=Development;Education;Science;\n"
    )
    p = f"/etc/skel/Desktop/wirebus-{a[0]}.desktop"
    with open(p, "w") as df:
        df.write(desk)
    os.chmod(p, 0o755)

print("All 14 apps and shortcuts successfully created!")
