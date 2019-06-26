#! /usr/bin/python
  
import os
from shutil import copyfile

path = '.'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.cue' in file:
            original = os.path.join(r, file)
            modified = original.replace('./','').replace('/', '_')
            print(modified)
            #os.rename(original, modified)
            copyfile(original, modified)
            files.append(os.path.join(r, file))
            

for f in files:
    print(f)
