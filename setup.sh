#!/bin/bash
echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment and installing requirements..."
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Registering kernel for Jupyter..."
python -m ipykernel install --user --name=health_proj_venv --display-name "Python (.venv)"

echo "Setup complete! You're ready to go."

