#!/usr/bin/python3
import importlib.util
import sys
import os

if __name__ == "__main__":
    # Check if the file exists
    pyc_file = './hidden_4.pyc'
    if not os.path.exists(pyc_file):
        print(f"Error: {pyc_file} does not exist.")
        sys.exit(1)

    # Load the compiled module
    module_name = 'hidden_4'
    try:
        spec = importlib.util.spec_from_file_location(module_name, pyc_file)
        hidden_4 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(hidden_4)
    except Exception as e:
        print(f"Error loading module: {e}")
        sys.exit(1)
    
    # Get the names defined in the module
    names = dir(hidden_4)
    
    # Filter and sort the names
    filtered_names = sorted(name for name in names if not name.startswith('__'))
    
    # Print the names
    for name in filtered_names:
        print(name)
