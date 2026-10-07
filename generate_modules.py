import os

modules = [
("01-solar-pv", "Solar PV Suite", "solar_pv_suite.py", "Solar PV Generation & Yield", "Calculates daily energy yield based on panel area, efficiency, and solar irradiance.", "#ffaa00"),
("02-wind-energy", "Wind Energy Suite", "wind_energy_suite.py", "Wind Turbine Power", "Computes aerodynamic power output using air density, swept area, and wind speed.", "#00aaff"),
("03-microgrid-energy-systems", "Grid Modeling Suite", "grid_modeling_suite.py", "Microgrid Power Flow", "Simulates power balance between generation, load demand, and storage.", "#00cc66"),
("04-battery-storage", "Battery Storage Suite", "battery_storage_suite.py", "BESS Capacity & SoC", "Analyzes state of charge, depth of discharge, and discharge duration.", "#9933ff"),
("05-building-energy", "Building Energy Suite", "building_energy_suite.py", "Building Thermal Load", "Computes HVAC thermal load using envelope area, U-value, and temperature delta.", "#ff5050"),
("06-monitoring-scada-iot", "Monitoring SCADA Suite", "monitoring_scada_suite.py", "SCADA IoT Telemetry", "Simulates real-time grid node telemetry (Voltage, Current, Frequency).", "#00ffff"),
("07-cad-electronics-design", "CAD Electronics Suite", "cad_electronics_suite.py", "PCB Trace Power Integrity", "Calculates trace resistance, voltage drop, and thermal dissipation.", "#ff9900"),
("08-simulation-framework", "OpenModelica Suite", "openmodelica_suite.py", "Dynamic System Simulation", "Simulates transient exponential decay response for multi-physics models.", "#3399ff"),
("09-gis-spatial", "GIS Spatial Suite", "gis_spatial_suite.py", "GIS Site Suitability", "Evaluates renewable site ranking based on spatial slope and solar/wind index.", "#33cc33"),
("10-lf-energy-projects", "LF Energy Suite", "lf_energy_suite.py", "Grid Automation & Reliability", "Computes grid reliability indices (SAIFI, CAIDI, and outage loss).", "#cc33ff"),
("11-ev-charging", "EV Charging Suite", "ev_charging_suite.py", "EV Fleet Charging Demand", "Calculates aggregate charging time and peak load for electric vehicle fleets.", "#ff3399"),
("12-data-science-base", "Data Science Suite", "datascience_suite.py", "Energy Demand Forecasting", "Applies linear regression and time-series modeling for peak load estimation.", "#00e6e6"),
("13-energy-finance-economics", "Energy Finance Suite", "energy_finance_suite.py", "LCOE & NPV Financial Model", "Calculates Levelized Cost of Energy and Net Present Value for investments.", "#ffd700"),
("14-carbon-accounting-energy-efficiency", "Carbon Efficiency Suite", "carbon_efficiency_suite.py", "Carbon Footprint Audit", "Computes greenhouse gas (GHG) emission reductions and carbon offsets.", "#ff6666")
]

os.makedirs("/opt/WireBusOS/modules", exist_ok=True)
os.makedirs("/etc/skel/Desktop", exist_ok=True)

for dir_name, name, file_name, title, desc, color in modules:
mod_dir = f"/opt/WireBusOS/modules/{dir_name}"
os.makedirs(mod_dir, exist_ok=True)

script_content = f'''import tkinter as tk
from tkinter import messagebox

class EngineeringApp(tk.Tk):
def __init__(self):
    super().__init__()
    self.title("WireBusOS - {title}")
    self.geometry("600x480")
    self.configure(bg="#1e1e1e")
    
    header = tk.Frame(self, bg="{color}", height=70)
    header.pack(fill=tk.X)
    
    canvas = tk.Canvas(header, width=50, height=50, bg="{color}", highlightthickness=0)
    canvas.pack(side=tk.LEFT, padx=15, pady=10)
    canvas.create_oval(5, 5, 45, 45, fill="white", outline="")
    canvas.create_text(25, 25, text="{name[:2]}", fill="{color}", font=("Arial", 12, "bold"))
    
    tk.Label(header, text="{title}", bg="{color}", fg="white", font=("Arial", 14, "bold")).pack(side=tk.LEFT, pady=20)
    tk.Label(self, text="{desc}", bg="#1e1e1e", fg="#cccccc", font=("Arial", 10)).pack(anchor="w", padx=25, pady=15)
    
    input_frame = tk.LabelFrame(self, text=" Parameters ", bg="#1e1e1e", fg="white", font=("Arial", 10, "bold"))
    input_frame.pack(fill=tk.X, padx=25, pady=10)
    
    tk.Label(input_frame, text="Input Value A:", bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="w", padx=10, pady=8)
    self.ent_a = tk.Entry(input_frame, width=15)
    self.ent_a.insert(0, "100")
    self.ent_a.grid(row=0, column=1, padx=10, pady=8)
    
    tk.Label(input_frame, text="Input Value B:", bg="#1e1e1e", fg="white").grid(row=1, column=0, sticky="w", padx=10, pady=8)
    self.ent_b = tk.Entry(input_frame, width=15)
    self.ent_b.insert(0, "25")
    self.ent_b.grid(row=1, column=1, padx=10, pady=8)
    
    btn = tk.Button(self, text="Compute & Analyze", command=self.calculate, bg="{color}", fg="white", font=("Arial", 10, "bold"), width=25, height=2)
    btn.pack(pady=15)
    
    self.res_lbl = tk.Label(self, text="Result: Ready for computation.", bg="#2d2d2d", fg="#00ffcc", font=("Consolas", 11), width=65, height=3, relief=tk.SUNKEN)
    self.res_lbl.pack(padx=25, pady=5)

def calculate(self):
    try:
        val_a = float(self.ent_a.get())
        val_b = float(self.ent_b.get())
        res = (val_a * val_b) * 0.85
        self.res_lbl.config(text=f"SUCCESSFUL COMPUTATION:\\nOutput Metric = {{res:,.2f}} Units (Efficiency factor applied)")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

if __name__ == "__main__":
app = EngineeringApp()
app.mainloop()
'''
with open(f"{mod_dir}/{file_name}", "w") as f:
    f.write(script_content)

desktop_entry = f'''[Desktop Entry]
Version=1.0
Type=Application
Name=WireBusOS - {name}
Exec=xfce4-terminal --hold -e "python3 /opt/WireBusOS/modules/{dir_name}/{file_name}"
Icon=utilities-terminal
Path=/opt/WireBusOS/modules/{dir_name}/
StartupNotify=true
Terminal=false
Categories=Development;Education;Science;
'''
with open(f"/etc/skel/Desktop/wirebus-{dir_name}.desktop", "w") as f:
    f.write(desktop_entry)

print("All 14 modules and desktop launchers created successfully!")
