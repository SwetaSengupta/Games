import cx_Freeze

executables = [cx_Freeze.Executable("pygametic.py")]

cx_Freeze.setup(
    name="A tic tac toe game by Sweta",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )