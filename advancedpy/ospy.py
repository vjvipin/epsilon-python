import sys
import os

#print(dir(os))
os.mkdir("mynewdir")
os.chdir("mynewdir")
os.mkdir("anotherdir")
os.chdir("anotherdir")
print (os.getcwd())
#print(os.environ)
#print(os.getenv("PATH"))
#print(sys.path)
#print("\n")
#print(sys.executable)

#print(dir(sys))

#print(os.sys)


