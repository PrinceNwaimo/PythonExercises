# from pathlib import Path
#
# file_path = Path.home()/"Self trials 34"
# file_path.mkdir(exist_ok=True)
# file_path.touch(exist_ok=True)
# print(file_path)
# print(file_path.exists())
# print(file_path.is_dir())
# print(file_path.name)
# print(file_path.parent.name)


#
# from pathlib import Path
#
# folder_path = Path.cwd() /"my_trophy"/"my_file.txt"
# folder_path.mkdir(exist_ok=True)
# print(folder_path)
# folder_path.touch(exist_ok=True) #run so as not to give us error
# print(folder_path.name)
# print(folder_path.parent)

import pathlib

path1 = pathlib.Path.cwd()
folder_a = path1 / "folder_a"
folder_a.mkdir(exist_ok=True)
# here, we want to create a list of paths
file_paths = [
    folder_a / "private.img",
    folder_a / "lyrics.txt",
    folder_a / "alone.vid",
    folder_a / "inside.csv",
    folder_a / "Bible.txt",
    folder_a / "looks.jpg"
]
for path in file_paths:
    path.touch()

# print(path1)
# for file in folder_a.iterdir():#This makes it iterable, making it possible to get all the folders in file.
#     print(file.name)
#     for files in path1.iterdir():
#            print(files.name)
# to filter  the files you want to get, you can use glob method
#     for file in folder_a.glob("*.JPG"):
#             print(file.name)
for files in path1.glob("**/*.csv"):
    print(files.name)
    # to move files
    # source = path1 / "celsius.py", "Cipher_algorithm.py", "Circle.py", "Class_work.py", "classexample.py", " classfile2.py"
    # destination = path1 / "folder_a" / "celsius.py", "Cipher_algorithm.py", "Circle.py", "Class_work.py", "classexample.py", "classfile2.py"
    # source.replace(destination)
