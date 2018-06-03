import sys
import os.path
from cx_Freeze import setup, Executable

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


base = None
if sys.platform == 'win32':base = 'Win32GUI'

opts = { 'include_files':['logo.gif'],'include_files':[os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll')],'includes':['re']}

setup( name = 'NoteMe',
       version = '1.0',
       author = 'Ayush Raj',
       options = { 'build_exe':opts },
       executables = [ Executable('NoteMe.py',base=base)])
