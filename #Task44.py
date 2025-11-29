#Task44
s = input('Your Input: ')
l = len(s)
pad = 16 - l
left = '>' * (pad // 2)
right = '<' * (pad - (pad // 2))
line = '-' * 18
print(line, '|' + left + s + right + '|', line, sep='\n')