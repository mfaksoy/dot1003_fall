#Task29
var_sifre = "furkan"
var_kalan_hak = 3
var_is_running = True

while var_kalan_hak > 0 and var_is_running == True:
    var_kalan_hak -= 1
    var_i_sifre = input("Sifre?")
    
    if var_i_sifre == var_sifre:
        print ("Welcome")
        var_is_running =False
    
    elif var_kalan_hak > 0:
        print("Try again")
    
if var_kalan_hak == 0 and var_i_sifre != var_sifre :
        print("Over")

    

    



