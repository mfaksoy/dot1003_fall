#Task30
adet = 0
toplam = 0
tek = 0
cift = 0

forend = True
while forend:
    sayi = int(input("Number (0 please)"))
    
    if sayi == 0:
        forend = False

     
    adet = adet + 1
    toplam = toplam + sayi
    
    if sayi % 2 == 0:
        cift = cift + 1
    else:
        tek = tek + 1
print("\n--- RESULT ---")
print("Total Number:", adet)
print("Sum:", toplam)

if adet != 0:
    
    print("Mean:", toplam / adet)

print("Odd :", tek)
print("Even:", cift)