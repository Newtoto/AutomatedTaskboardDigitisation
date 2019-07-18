import cx_Freeze

executables = [cx_Freeze.Executable("TaskboardTimeline.py")]

cx_Freeze.setup(
     name="TaskboardTimeline",
     options={"build_exe": {"packages":["pygame"],
                            "include_files":[]}},
    executables = executables
)
 
#from distutils.core import setup
#import py2exe

#setup(console=['show_images.py'])