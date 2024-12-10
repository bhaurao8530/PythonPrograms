file = open("file.txt", "r")
print(f"{len(file.readlines())} lines in file")
file.close()
