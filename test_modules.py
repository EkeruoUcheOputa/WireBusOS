import os
import subprocess
import sys

modules_dir = "/opt/WireBusOS/modules"
print("=== Scanning WireBusOS Modules ===")

for item in sorted(os.listdir(modules_dir)):
    module_path = os.path.join(modules_dir, item)
    if os.path.isdir(module_path):
        # Look for python files inside the directory
        py_files = [f for f in os.listdir(module_path) if f.endswith('.py')]
        if py_files:
            target_script = os.path.join(module_path, py_files[0])
            print(f"\n[TESTING] Module: {item} -> Script: {py_files[0]}")
            try:
                # Run with a short timeout to catch hangs
                result = subprocess.run(
                    [sys.executable, target_script], 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE, 
                    timeout=3
                )
                if result.returncode == 0:
                    print(f"  [PASS] {item}")
                else:
                    print(f"  [FAIL] {item} exited with code {result.returncode}")
                    print(f"  Error: {result.stderr.decode()[:200]}...")
            except subprocess.TimeoutExpired:
                print(f"  [HANG/TIMEOUT] {item} tried to open a GUI or hung waiting for input.")
            except Exception as e:
                print(f"  [ERROR] {item}: {e}")
        else:
            print(f"\n[SKIP] {item}: No Python files found.")
