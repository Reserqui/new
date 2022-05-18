import os
import subprocess

path_to_pdf = os.path.abspath('D:\BookFolder/books about python/baba.pdf')
path_to_acrobat = os.path.abspath("C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe")
process = subprocess.Popen([path_to_acrobat, '/A', 'page=120', path_to_pdf], shell=False, stdout=subprocess.PIPE)
