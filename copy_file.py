# to copy from 1 file to another

from shutil import copyfile
print("Enter x for exit")
source_file = input("Enter source file name:")
if(source_file == "x"):
    exit()
else:
    destination_file = input("Enter destination file name:")
    copyfile(source_file,destination_file)
    print("File copied successfully...")
    check = input("Want to display the content(y/n):")
    if(check == "n"):
        exit()
    else:
        temp = open(destination_file,"r")
        print(temp.read())
        temp.close()
