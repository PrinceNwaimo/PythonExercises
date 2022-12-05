# from pathlib import Path
#
# file_path = Path.cwd()/"my_lab"/"my_file.txt"
# file_path.mkdir(exist_ok=True)
# file_path.touch(exist_ok=True)
# print(file_path)
# print(file_path.exists())
# print(file_path.is_dir())
# print(file_path.name)
# print(file_path.parent.name)

















from pathlib import Path

folder_path = Path.cwd() /"my_trophy"/"my_file.txt"
folder_path.mkdir(exist_ok=True)
print(folder_path)
folder_path.touch(exist_ok=True)
print(folder_path.name)
print(folder_path.parent)