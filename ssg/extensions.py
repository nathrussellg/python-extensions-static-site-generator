import sys, importlib
from pathlib import Path

def load_module(directory, name):
    sys.path.insert(0,directory)
    importlib.import_module(name)
    sys.path.pop(0)