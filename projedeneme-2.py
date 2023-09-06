import time

başlık = "bu program not defteri prgramıdır girdiğiniz metinleri saveler ve liste halinde size verir!!!"

print(başlık.upper())


kayıt_listesi = [ ]

kayıt_isim = input("yeni bir kayıt oluşturmak için kaydınızın ismini girin yazınız: ")

kayıt_listesi.append(kayıt_isim)


notdefteri = input("kayıdınızı giriniz: ")
    

kayıt_isim_kontrol = input("görmek istediğiniz kaydın ismini girin: ")

if kayıt_isim_kontrol == kayıt_isim:
    print(notdefteri)


kayıt_listesi_kontrol = input("tüm kayıtlarınızın isimlerini görmek istiyıorsanız 'kayıtlarım' yazın !... = ")

if kayıt_listesi_kontrol == 'kayıtlarım':
    print(kayıt_listesi)

time.sleep(1)

seçenek = input("programımız bitti eğer çıkmak istiyorsanı q ya devam etmek istiyorsanız d ye basın! : ")

if seçenek == "q".lower():
    print("çıkış yapılıyor...")
    time.sleep(1)
    print("...")
    print("...")
    print("...")
    print("...")
    print("...")
    print("çıkış yapıldı!")
    quit()
elif seçenek == "d".lower():
    print("programa devam edilecek lütfen bekleyin...")
    time.sleep(1)

başlık = "bu program not defteri prgramıdır girdiğiniz metinleri saveler ve liste halinde size verir!!!"

print(başlık.upper())


kayıt_listesi = [ ]

kayıt_isim = input("yeni bir kayıt oluşturmak için kaydınızın ismini girin yazınız: ")

kayıt_listesi.append(kayıt_isim)


notdefteri = input("kayıdınızı giriniz: ")
    

kayıt_isim_kontrol = input("görmek istediğiniz kaydın ismini girin: ")

if kayıt_isim_kontrol == kayıt_isim:
    print(notdefteri)


kayıt_listesi_kontrol = input("tüm kayıtlarınızın isimlerini görmek istiyıorsanız 'kayıtlarım' yazın !... = ")

if kayıt_listesi_kontrol == 'kayıtlarım':
    print(kayıt_listesi)
