# version=input('version:\n0-PySide2\n1-PySide6\n2-PyQt5\n3-PyQt6\n')
# if version=='0':
#     import PySide2 as qt
# elif version=='1':
#     import PySide6 as qt
# elif version=='2':
#     import PyQt5 as qt
# elif version=='3':
#     import PyQt6 as qt
import PySide6 as qt
import os
os.chdir(os.path.dirname(qt.__file__))
file=input('file: ')
if '"' not in file:
    file='"'+file+'"'
os.system(f'.{os.sep}uic -g python {file} -o {os.sep.join(file.split(os.sep)[:-1])+os.sep}ui_{file.split(os.sep)[-1][:-3]}py"')