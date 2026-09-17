import os
import subprocess
import sys

print("Creating virtual environment (.venv)...")
if not os.path.exists(".venv"):
    subprocess.run([sys.executable, "-m", "venv", ".venv"])

# Determine the correct pip path depending on OS
if os.name == "nt":  # Windows
    pip_path = os.path.join(".venv", "Scripts", "pip")
    python_path = os.path.join(".venv", "Scripts", "python")
else:  # Mac / Linux
    pip_path = os.path.join(".venv", "bin", "pip")
    python_path = os.path.join(".venv", "bin", "python")

print("Upgrading pip and installing requirements...")
subprocess.run([pip_path, "install", "--upgrade", "pip"])
subprocess.run([pip_path, "install", "-r", "requirements.txt"])

print("Registering Jupyter kernel...")
subprocess.run([python_path, "-m", "ipykernel", "install", "--user", "--name=health_proj_venv", "--display-name=Python (.venv)"])

print("Setup complete! You're ready to go.")