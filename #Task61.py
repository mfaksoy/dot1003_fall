#Task61
def sum_of_row(matrix, row_no):
    return sum(matrix[row_no])

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = int(input("item to search: ")) 
print(my_matrix[element]) 
print(sum_of_row(my_matrix, element))