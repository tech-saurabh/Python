file = open("python.txt","w")
file.write("file read and write operations\n")
file.write("Python is an interpreted high-level programming language\n")
file.write("Created by Guido van Rossum\n")
file.write("first released in 1991\n")

# Read contents from a file :
file = open("python.txt")
temp = file.read()
print(temp)
