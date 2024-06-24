#!/bin/bash

# Set up the environment
echo "Setting up the environment..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the tests
echo "Running tests..."
pytest --maxfail=1 --disable-warnings -q

# Clean up
echo "Cleaning up..."
deactivate
rm -rf venv

echo "Tests completed."
