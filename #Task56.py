#Task56
def clear_vowels(s):
    return ''.join(c for c in s if c.lower() not in 'aeiou')


menu_button = "new game"
print(clear_vowels(menu_button))