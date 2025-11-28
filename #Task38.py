#Task38

is_running = True
var_oluşan_tahta = 0

while is_running:
    var_tahta_boyut = int(input("Boyutu gir (Min2)"))    
    
    if var_tahta_boyut < 2 :
        print("Min 2")
        
    
    else :
        var_oluşan_tahta =[["_"for tahta_oluştur in range(var_tahta_boyut)] for tahta_oluştur2 in range(var_tahta_boyut)]

        for satır in var_oluşan_tahta:
          print(" | ".join(satır))
        
        is_running = False