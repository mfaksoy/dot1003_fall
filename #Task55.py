#Task55
def count_item():
    s = input('Enter the input to search: ')
    item = input('Which item do you want to search?: ')
    count = s.count(item)
    print(f"item {item} appeared {count} times")

count_item()