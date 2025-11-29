#Task53
def create_spruce():
    h = int(input('Spruce height: '))
    b = int(input('Box Size: '))
    
    line = '-' * (b - 2)
    print(f"|{line}|")
    
    row = 1
    while row <= h:
        stars = '*' * (2 * row - 1)
        content = f"|{stars.center(b - 2)}|"
        print(content)
        row += 1
    
    print(f"|{'*'.center(b - 2)}|")
    print(f"|{line}|")

create_spruce()