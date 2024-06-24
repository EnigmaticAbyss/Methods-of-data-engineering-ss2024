import os
import subprocess
import pytest
# Get the current directory of child_script.py
script_path = os.path.join(os.path.dirname(__file__), '..', 'hello.py')
subprocess.run(['python', script_path], check=True)


