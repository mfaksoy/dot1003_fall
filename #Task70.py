#Task70
def create_tuple(x, y):
    return (x, y)
game_table = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
user_inputs = []

running = True

while running:
    action = input("please type new or exit: ").lower().strip()

    if action == "new":
        try:
            x_str = input("please enter x: ")
            y_str = input("please enter y: ")
            x = int(x_str)
            y = int(y_str)
        
            user_inputs.append(create_tuple(x, y))
            
        except ValueError:
            print("Geçersiz giriş. Lütfen sayı giriniz.")
        
    elif action == "exit":
        running = False

for x, y in user_inputs:
    if 0 <= x < 3 and 0 <= y < 3:
        game_table[y][x] = "*"

for row in game_table:
    print(" ".join(row))
