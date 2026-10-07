import os, glob

modules = [
    ("01-solar-pv", "Solar PV Suite", "solar_pv_suite.py"),
    ("02-wind-energy", "Wind Energy Suite", "wind_energy_suite.py"),
    ("03-microgrid", "Grid Modeling Suite", "grid_suite.py"),
    ("04-battery", "Battery Storage Suite", "battery_suite.py"),
    ("05-building", "Building Energy Suite", "building_suite.py"),
    ("06-scada", "Monitoring SCADA Suite", "scada_suite.py"),
    ("07-cad", "CAD Suite", "cad_suite.py"),
    ("08-sim", "Simulation Framework", "sim_suite.py"),
    ("09-gis", "GIS Spatial Suite", "gis_suite.py"),
    ("10-reliability", "Reliability Suite", "rel_suite.py"),
    ("11-ev", "EV Suite", "ev_suite.py"),
    ("12-forecast", "Forecast Suite", "forecast_suite.py"),
    ("13-finance", "Energy Finance Suite", "finance_suite.py"),
    ("14-carbon", "Carbon Efficiency Suite", "carbon_suite.py")
]

target_dirs = [
    "/etc/skel/Desktop", 
    "/home/eggs/liveroot/etc/skel/Desktop",
    "/home/eggs/liveroot/home/live/Desktop"
]

for target_dir in target_dirs:
    if os.path.exists(target_dir) or "liveroot" in target_dir:
        os.makedirs(target_dir, exist_ok=True)
        # Remove any existing wirebus desktop files first
        for f in glob.glob(os.path.join(target_dir, "wirebus-*.desktop")):
            os.remove(f)
            
        for dir_name, name, file_name in modules:
            desktop_content = f"""[Desktop Entry]
Version=1.0
Type=Application
Name=WireBusOS - {name}
Exec=xfce4-terminal --hold -e "python3 /opt/WireBusOS/modules/{dir_name}/{file_name}"
Icon=utilities-terminal
Path=/opt/WireBusOS/modules/{dir_name}/
StartupNotify=true
Terminal=false
Categories=Development;Education;Science;
"""
            path = os.path.join(target_dir, f"wirebus-{dir_name}.desktop")
            with open(path, "w") as f:
                f.write(desktop_content)
            os.chmod(path, 0o755)

print("All target desktop directories cleaned and synchronized with exactly 14 modules!")
