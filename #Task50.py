#Task50
s = input('Please enter string: ')
item = input('Please enter search item: ')
i = s.find(item)
print(f"found it at {i}" if i != -1 else "not found")