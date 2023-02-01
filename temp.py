from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('.') if isfile(join('./', f)) and f.endswith(".py")]

for file in onlyfiles:
    with open(file, 'a') as f:
        f.write('"""\n\n"""')"""

"""