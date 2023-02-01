import os
from fnmatch import fnmatch

root = './tests'
pattern = "*.py"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            new_name = 'test_' + name
            print(os.path.join(path, name))
            os.rename(os.path.join(path, name), os.path.join(path, new_name))