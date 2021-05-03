import os

for subdir, dirs, files in os.walk('../data'):
    for filename in files:
        filepath = subdir + '/' + filename

        os.rename(filepath, '../data/' + filename)