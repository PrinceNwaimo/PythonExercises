try:
    file_name = open("C:\Users\Admin\Documents\12 Rules of Overriding in Java You Should Know_files\f.txt", "r")
    file_name.read()
except IOError:
    print("Cannot write to a close file")
else:
    file_name.close()
    print("Successful")