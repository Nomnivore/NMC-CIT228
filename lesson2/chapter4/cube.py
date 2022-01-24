cubes = [1 ** 3, 2 ** 3, 3 ** 3, 4 ** 3, 5 **
         3, 6 ** 3, 7 ** 3, 8 ** 3, 9 ** 3, 10 ** 3]

for cube in cubes:
    print(f"The next cube is {cube}")

cubes_comp = [n ** 3 for n in range(1, 10)]

print(f"Cubes made with list comprehension: {cubes_comp}")
