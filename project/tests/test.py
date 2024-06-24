
import os
# Get the current directory of child_script.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the parent_script.py
parent_script_path = os.path.join(current_dir, '..', 'parent_script.py')
print(parent_script_path)
