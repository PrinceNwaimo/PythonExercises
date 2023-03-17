import pathlib

path1 = pathlib.Path.home()
my_folder = path1 / "my_folder"
my_folder.mkdir(exist_ok=True)
print(my_folder)
file_paths = [
    my_folder / "file1.txt",
    my_folder / "file2.txt",
    my_folder / "image1.png"
]
for paths in file_paths:
    path1.touch()
    print(file_paths)
delete_my_folder=path1.home()/"my_folder"
delete_my_folder.rmdir()


