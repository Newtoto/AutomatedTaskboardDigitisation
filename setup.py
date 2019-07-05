import cx_Freeze

executables = [cx_Freeze.Executable("TaskboardTracker.py")]

cx_Freeze.setup(
    name="TaskboardDigitisation",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":[]}},
    executables = executables

    )