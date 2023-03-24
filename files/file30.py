import os
for dirpath, dirnames, filenames in os.walk('.'):
    print("Current path: ", dirpath)
    print("Directories", dirnames)
    print("Files: ", filenames)
    print()