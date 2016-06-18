l = [2, 6, 6,  7, 7, 7, 7, 4, 23424, 12]

lookup = set()

ordered_unique = []

for i in l:
    if i not in lookup:
        ordered_unique.append(i)
        lookup.add(i)

print(ordered_unique)
