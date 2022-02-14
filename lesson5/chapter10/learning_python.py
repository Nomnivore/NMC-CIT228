fname = "lesson5/chapter10/learning_python.txt"

# 10-1
with open(fname) as pyFile:
    myPy = pyFile.read()
    
print("---- Output from read() ----")
print(myPy)

print("---- Output from for loop ----")
with open(fname) as pyFile:
    for line in pyFile:
        print(line)
        
print("---- Output from readlines() ----")
with open(fname) as pyFile:
    myPy = pyFile.readlines()

for line in myPy:
    print(line)


# 10-2
print("---- Replacing python with programming ----")
with open(fname) as pyFile:
    for line in pyFile:
        print("Original: ", line)
        print("Modified: ", line.replace("python", " programming"))
