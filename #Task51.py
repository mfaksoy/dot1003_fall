#Task51
s = "The quick brown fox jumps over the lazy dog"
while 1:
    item = input('What are you looking for? ')
    if item == '-1':
        print('Bye.')
        exit()
    i = s.find(item)
    print(f"found it at {i}" if i != -1 else "not found")