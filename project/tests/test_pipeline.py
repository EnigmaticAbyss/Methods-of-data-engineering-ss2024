import os
import subprocess
import pytest

@pytest.fixture(scope="module")
def run_pipeline():
    # Path to the pipeline script
 
    # Step 1: Get the directory of the current script
    # current_script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # # Step 2: Get the parent directory
    # parent_dir = os.path.abspath(os.path.join(current_script_dir, os.pardir))
    
    # # Step 3: Construct the path to the target file in the parent directory
    # target_file_path = os.path.join(parent_dir,'pipeline.py')
    current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the parent_script.py
    parent_script_path = os.path.join(current_dir, '..', 'pipeline.py')
    # Execute the pipeline
    subprocess.run(['python', parent_script_path], check=True)
    
    yield
      # Step 1: Get the directory of the current script
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Step 2: Get the parent directory
    parent_dir = os.path.abspath(os.path.join(current_script_dir, os.pardir))
    
    # Step 3: Construct the path to the target file in the parent directory
    target_file_path = os.path.join(parent_dir,'pipeline.py') 
    # Clean up any generated files (if necessary)
    # Step 1: Get the directory of the current script
    current_script_dir = os.path.dirname(os.path.abspath(__file__))

    # Step 2: Navigate up two levels to the grandparent directory
    grandparent_dir = os.path.abspath(os.path.join(current_script_dir, os.pardir, os.pardir))

    # Step 3: Construct the path to the target file in the grandparent directory
    target_file_path = os.path.join(grandparent_dir,'data')
    output_files = [
        os.path.join(target_file_path, 'climate-change-earth-surface-temperature-data.db'),
        os.path.join(target_file_path, 'global-food-agriculture-statistics.db')
    ]
    for file in output_files:
        if os.path.exists(file):
            os.remove(file)

def test_output_files_exist(run_pipeline):
    current_script_dir = os.path.dirname(os.path.abspath(__file__))

    # Step 2: Navigate up two levels to the grandparent directory
    grandparent_dir = os.path.abspath(os.path.join(current_script_dir, os.pardir, os.pardir))

    # Step 3: Construct the path to the target file in the grandparent directory
    target_file_path = os.path.join(grandparent_dir,'data')
    # Check if the output files are created
    output_files = [
        os.path.join(target_file_path, 'climate-change-earth-surface-temperature-data.db'),
        os.path.join(target_file_path, 'global-food-agriculture-statistics.db')
    ]
    for file in output_files:
        assert os.path.exists(file), f"Output file {file} does not exist."
