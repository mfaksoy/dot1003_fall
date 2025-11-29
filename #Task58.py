#Task58
def anarya(input_list):
    return input_list[::-1]

game_list = []
while 1:
    user_input = input("Enter game or 'exit': ")
    if user_input == 'exit':
        print(game_list)
        print(anarya(game_list))
        exit()
    game_list.append(user_input)
