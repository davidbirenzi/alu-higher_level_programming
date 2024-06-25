#!/usr/bin/python3
import importlib.util
import sys

if __name__ == "__main__":
    # Load the compiled module
    module_name = 'hidden_4'
    spec = importlib.util.spec_from_file_location(module_name, './hidden_4.pyc')
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    
    # Get the names defined in the module
    names = dir(hidden_4)
    
    # Filter and sort the names
    filtered_names = sorted(name for name in names if not name.startswith('__'))
    
    # Print the names
    for name in filtered_names:
        print(name)
