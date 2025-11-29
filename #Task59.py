#Task59
def longest_name(input_list):
    return min(input_list, key=len)

game_list = ["Doom", "Max Payne", "FTL"]
print(game_list)
print(longest_name(game_list))