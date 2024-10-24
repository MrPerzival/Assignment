# Problem-3: Unpacking Tuple Treasures
treasures = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Unpack the first treasure to apprentice X, the last to apprentice Y, and the rest vanish
X, *_, Y = treasures
print(f"First treasure to apprentice X: {X}, Last treasure to apprentice Y: {Y}")

# Assign the first treasure to apprentice I, the last to apprentice J, and combine the middle treasures
I, *middle_treasures, J = treasures
print(f"First treasure to apprentice I: {I}, Last treasure to apprentice J: {J}, Middle treasures: {middle_treasures}")
