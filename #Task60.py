#Task60
def finder(matrix, element):
    for r, row in enumerate(matrix):
        if element in row:
            c = row.index(element)
            print(f"find at row: {r} column: {c}")
            return True
    return False

# Örnek kullanım (Task'taki gibi)
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = int(input("item to search: "))
for row in my_matrix:
    print(row)
print(finder(my_matrix, element))