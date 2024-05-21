file = open("foobar.txt", "w")
file.write("Hello world!")
file.close()

file = open("foobar.txt", "r")
print(file.read())