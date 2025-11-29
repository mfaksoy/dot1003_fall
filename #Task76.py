#Task76
import datetime

def age_calc():
    is_valid = False
    
    while not is_valid:
        birth_year_input = input("What is your birthyear? ")
    
        try:
            birth_year = int(birth_year_input)
            is_valid = True  
            
            current_year = datetime.datetime.now().year
            age = current_year - birth_year
            
            # Yaşı döndür
            return age
            
        except ValueError:
            print("Invalid Input.")
           
print(f"You are {age_calc()} years old")