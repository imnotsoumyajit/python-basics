from pathlib import Path

# 2 types
# Absolute Path : from the root of the disk | eg: c:\programs\something
# Relative Path : from the working directory| eg: 

# path=Path('13-package/ecom')
# path=Path('13-package/email')
# print(path.exists())
# # print(path.mkdir())
# print(path.exists())
# print(path.rmdir())
# print(path.exists())

path=Path() # empty () means current directory
# print(path.glob('*.*')) # we can search dirs with this   *.* is all file names with all extension type
for file in path.glob('*.py'):
    print(file)



