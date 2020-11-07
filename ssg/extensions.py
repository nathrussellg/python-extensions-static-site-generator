import sys, importlib
import Path from pathlib

def load_module(directory, name):
    sys.path.insert(0,directory)
    importlib.import_module(name)
    sys.path.pop(0)