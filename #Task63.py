#Task63
def tripler(input_list):
    return [n * 3 for n in input_list]

my_lucky_numbers = [4, 8, 15, 16, 23, 42]
tripled_numbers = tripler(my_lucky_numbers)
print(f"My Lucky Numbers: {my_lucky_numbers}")
print(f"Tripled Numbers: {tripled_numbers}")