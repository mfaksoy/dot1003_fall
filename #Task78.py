#Task78
def new_game():
    game_name = input("game name: ").strip()
    release_year_str = input("release year: ").strip()

    if not game_name or len(game_name) > 40:
        raise ValueError("Invalid game name: Cannot be empty or longer than 40 characters.")

    try:
        release_year = int(release_year_str)
    except ValueError:
        raise ValueError("Invalid release year: Must be an integer.")

    if release_year < 0 or release_year > 2024:
        raise ValueError("Invalid release year: Cannot be negative or greater than 2024.")
    
    return (game_name, release_year)

game_list = []
flag = True

while flag:
    user_command = input("add or exit: ").lower().strip()
    
    if user_command == "exit":
        flag = False 
        
    elif user_command == "add":
        try:
            
            game_list.append(new_game())
            
        except ValueError as e:
            
            print(f"Error: {e}")
            
for game in game_list:
    print(f"Game name: {game[0]}, Release Year: {game[1]}")