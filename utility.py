import os
import sys

def get_exe_path():
    try:
        # If bundled by PyInstaller
        return sys._MEIPASS
    except AttributeError:
        # If running from .py
        return os.path.abspath(os.path.dirname(__file__))
