import os

script_path = os.path.join(os.path.dirname(__file__), '..', 'pipeline.py')
print(script_path)



# Step 1: Get the directory of the current script
current_script_dir = os.path.dirname(os.path.abspath(__file__))
print(current_script_dir)
# Step 2: Get the parent directory
parent_dir = os.path.abspath(os.path.join(current_script_dir, os.pardir))
print(parent_dir)
# Step 3: Construct the path to the target file in the parent directory
target_file_path = os.path.join(parent_dir, 'target_file.txt')
print(target_file_path)