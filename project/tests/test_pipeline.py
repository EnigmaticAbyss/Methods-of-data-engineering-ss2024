import os
import subprocess
import pytest

@pytest.fixture(scope="module")
def run_pipeline():
    # Path to the pipeline script
    script_path = os.path.join(os.path.dirname(__file__), '..', 'pipeline.py')
        
    try:
        result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(e.stdout)
        print(e.stderr)
    yield
    
    # Clean up any generated files (if necessary)
    output_files = [
        os.path.join(os.path.dirname(__file__), '..', 'data', 'climate-change-earth-surface-temperature-data.db'),
        os.path.join(os.path.dirname(__file__), '..', 'data', 'global-food-agriculture-statistics.db')
    ]
    for file in output_files:
        if os.path.exists(file):
            os.remove(file)

def test_output_files_exist(run_pipeline):
    # Check if the output files are created
    output_files = [
        os.path.join(os.path.dirname(__file__), '..', 'data', 'climate-change-earth-surface-temperature-data.db'),
        os.path.join(os.path.dirname(__file__), '..', 'data', 'global-food-agriculture-statistics.db')
    ]
    for file in output_files:
        assert os.path.exists(file), f"Output file {file} does not exist."
