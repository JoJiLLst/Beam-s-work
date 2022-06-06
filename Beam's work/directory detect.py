import glob
path="D:\\jillzaza\\Coding_area\\Main project work\\Code\\Beam's work\\Human face\\"
print('\nNamed with wildcard ranges:')
for files in glob.glob(path + '/*[1-50].*'):
    print(files)