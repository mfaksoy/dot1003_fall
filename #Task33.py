#Task33

list_istenen = []
var_is_running = True
var_cikis = "exit"

while var_is_running:
    
    var_ekleme = input("Listeye ekleme")
    list_istenen.append(var_ekleme)

    if var_ekleme == var_cikis:
        var_is_running =False

print(list_istenen)
