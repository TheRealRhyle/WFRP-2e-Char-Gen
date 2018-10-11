import os
from subprocess import call

for filename in os.listdir('D:\GHRepo\WFRP-2e-Char-Gen'):

    if '.ui' in filename:
        print("UI File: " + filename)
        pyfname = filename.replace('.ui','.py')
        call(['pyuic5','-x',filename,'-o',pyfname])