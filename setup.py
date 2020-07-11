import sys
import cx_Freeze
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
executables = [cx_Freeze.Executable('pygametic.py')]

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "tic tac toe game by sweta",
        version = "0.1",
        description = "My tic tac toe game!",
        options={"build_exe": {"packages": ["pygame"]}},
        executables=executables
)
        