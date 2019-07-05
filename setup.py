# import cx_Freeze

# executables = [cx_Freeze.Executable("show_images.py")]

# cx_Freeze.setup(
#     name="TaskboardDigitisation",
#     options={"build_exe": {"packages":["pygame"],
#                            "include_files":["Images"]}},
#     executables = executables

#     )
from distutils.core import setup
import py2exe

setup(console=['show_images.py'])