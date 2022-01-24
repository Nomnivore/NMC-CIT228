cats = ["Emmy", "Gizmo", "Simba", "Mia", "Misty", "Basil", "Remie"]

print(f"Original list: {cats}")

cats.insert(5, "Simon")
cats.append("Clyde")
cats.append("Kona")

print(f"List after additions: {cats}")

del cats[5]
cats.pop(-1)

print(f"List after deletions: {cats}")

print(f"List with temporary sort: {sorted(cats)}")
cats.reverse()
print(f"List sorted in reverse: {cats}")
cats.sort()
print(f"List sorted in alphabetical order: {cats}")

print(f"There are {len(cats)} cats in the final list.")
