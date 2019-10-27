import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf']
base = None

if sys.platform == "win32":
    base = "win32GUI"

setup(name="puzzle",
      version="0.1",
      description="Fun Computer Game",
      options={'build_exe': {'include_files': include_files}},
      executables=[Executable("main.py", base=base)])
