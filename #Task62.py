#Task62
def sum_of_column(matrix, col_no):
    return sum(row[col_no] for row in matrix)

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = int(input("column no: "))
for row in my_matrix:
    print(row)
print(sum_of_column(my_matrix, element))