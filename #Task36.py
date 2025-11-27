#Task36
is_running = True
list_puan = []
var_bitiş = "exit"

while is_running:
    
    var_puan = (input("Puan"))
    
    if var_bitiş == var_puan:
     is_running = False

    elif var_puan.isdigit():
       list_puan.append(int(var_puan))

print(sum(list_puan))


