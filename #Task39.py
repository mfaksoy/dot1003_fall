#Task39

def cam_agaci_ciz(yukseklik):
    for i in range(yukseklik):
        yildiz_sayisi = 2 * i + 1
        bosluk_sayisi = yukseklik - i - 1
        print(' ' * bosluk_sayisi + '*' * yildiz_sayisi)

    govde_genislik = 3
    govde_yukseklik = yukseklik // 3
    
    govde_hiza_bosluk = yukseklik - 2
    
    for _ in range(govde_yukseklik):
        print(' ' * govde_hiza_bosluk + '*' * govde_genislik)

is_running = True

while is_running:

    var_tahta_boyut = input("Kaç katlı (yüksek) bir çam ağacı çizelim? (Min 3): ")
    
    if not var_tahta_boyut.isdigit():
        print("Hata: Lütfen sadece sayısal bir değer giriniz.")
        is_running = False        
        
    yukseklik = int(var_tahta_boyut)

    if yukseklik < 3:
        print("Hata: Çam ağacı için minimum yükseklik 3 olmalıdır.")
        is_running = False 
   
    else:
        cam_agaci_ciz(yukseklik)
        
        is_running = False

