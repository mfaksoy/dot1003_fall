#Task68
my_coordinates = {}
def coordinator(x, y):
    return (x, y)


data = [
    ((0, 0), "Home"),
    ((1, 1), "Work"),
    ((-1, -1), "School")
]


for (x, y), name in data:
    my_coordinates[coordinator(x, y)] = name

for k, v in my_coordinates.items():
    print(f"position: {k} name: {v}")