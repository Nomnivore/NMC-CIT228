biggestnum = 9999
bignum = 100
smallnum = 10
color = "Purple"
languages = ["python", "ruby", "javascript", "c#"]
car = "ford"

print("---------- Truthy ----------")
print("Is car == 'ford'? ", car == "ford")

print("Is color.lower() == 'purple'? ", color.lower() == "purple")

print("Is bignum > smallnum? ", bignum > smallnum)

print("Is biggestnum > bignum and bignum > smallnum? ", biggestnum > bignum and bignum > smallnum)

print("Is car.upper() == 'TOYOTA' or car.upper() == 'FORD'? ", car.upper() == "TOYOTA" or car.upper() == "FORD")

print("Is python in languages? ", "python" in languages)
print("Is haskell not in languages? ", "haskell" not in languages)

print("---------- Falsy ----------")
print("Is car == 'toyota'? ", car == "toyota")

print("Is color.lower() == 'Purple'? ", color.lower() == "Purple")

print("Is smallnum >= bignum? ", smallnum >= bignum)

print("Is smallnum == color or car in languages? ", smallnum == color or car in languages)

print("Is c++ in languages? ", "c++" in languages)

print("Is javascript not in languages? ", "javascript" not in languages)
