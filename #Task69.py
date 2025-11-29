#Task69

weapon1 = ("blade", 10)
weapon2 = ("sabre", 35)
weapon3 = ("sword", 50)
meele_weapon = [weapon1, weapon2, weapon3]

def print_best_weapon(weapon_list):
    best_weapon = max(weapon_list, key=lambda w: w[1])
    
    print(best_weapon[0])

print_best_weapon(meele_weapon)