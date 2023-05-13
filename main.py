import random
print("---Adam Asma Oyununa Hoşgeldin---")
print("Umarım ki adamı asmadan bitirisin.Başarılar <3")
adlar = ["oyun","türk","yabancı","yemek"]
gecerliHarfler = 'abcçdefgğhıijklmnoöprsştuüvyzqwx'
toplamhak = 10

def oyunisimleri():
    oyunlar = ["counterstrike", "tetris", "forzahorizon", "tekken", "minecraft", "portal", "thewitcherwildhunt"]
    return random.choice(oyunlar)

def yabancıfilmisimleri():
    yabancıfilmler = ["inception", "interstellar", "parasite", "joker", "thesilenceofthelambs", "annabelle","chucky"]
    return random.choice(yabancıfilmler)

def türkdizi():
    türkdizileri = ["ezel","kurtlarvadisi","adanalı","kardeşpayı","kuzeygüney","cennetmahallesi","hayatbilgisi"]
    return random.choice(türkdizileri)

def yemekler():
    yemekler = ["lahmacun", "pide", "yapraksarma", "lahanasarma", "mantı", "menemen", "karnıyarık","tavuksote"]
    return random.choice(yemekler)

while True:
    tus = input("0 a basarak türleri öğrenebilirsiniz, 1-4 sayılarını seçerek türleri oynayabilirsiniz: ")
    if tus == "0":
        print("Oyun-🤜🏻(1), Yabancı Film-🤜🏻(2), Türk Dizi-🤜🏻(3), Yemek-🤜🏻(4)")
    elif tus == "1":
        print("Zor oyunlar yok bence😑😑😑😑😑")
        print("Oyunu seçtiniz")
        break
    elif tus == "2":
        print("Popülerleri sordum sakın internetten bakma hee")
        print("Yabancı Film seçtiniz")
        break
    elif tus =="3":
        print("Zor sormadım bak😏😏😏😏")
        print("Türk Dizi seçtiniz")
        break
    elif  tus == "4":
        print("Aman ha canın çekmesin")
        print("Yemek seçtiniz")
        break
    else :
        print("Yanlış tuşa bastınız😡😡😡😡😡")

while True:
    if tus == "1":
        asilkelime = oyunisimleri().lower()
    elif tus == "2":
        asilkelime = yabancıfilmisimleri().lower()
    elif tus == "3":
        asilkelime = türkdizi().lower()
    elif tus == "4":
        asilkelime = yemekler().lower()

    yapilanTahmin = ''
    hataliTahminSayisi = 0

    while hataliTahminSayisi < toplamhak :
        harfBulundu = True

        for harf in asilkelime :
            if harf in yapilanTahmin :
                print(harf, end=' ')
            else:
                print('_', end=' ')
                harfBulundu=False

        print('\n')

        if harfBulundu:
            print("Tebrikler! Doğru kelimeyi buldunuz🎉🎉🎉:", asilkelime)
            break
        tahmin = input("Bir harf veya kelime tahmin edin🤔🤔:").lower()

        if tahmin == "5":
            print("Yeni bir oyun başlatılıyor...\n")
            break
        if tahmin == asilkelime:
            print("Tebrikler! Doğru kelimeyi buldunuz🎉🎉🎉:",asilkelime)
            break
        if len(tahmin)>1:
            print("Yanlış tahmin! Kalan Hakkınız:",toplamhak-hataliTahminSayisi)
            hataliTahminSayisi += 1
            continue
        if tahmin not in gecerliHarfler:
            print("Geçersiz işlem lütfen harf giriniz.")
            continue
        if tahmin in yapilanTahmin:
            print("Bu harfi kullandınız.Başka harf deneyiniz.")
            continue
        yapilanTahmin += tahmin

        if tahmin not in asilkelime:
            hataliTahminSayisi += 1
            print("Yanlış tahmin! Kalan hakkınız:", toplamhak - hataliTahminSayisi)
            if hataliTahminSayisi == toplamhak:
                print("Hakkınız bitti☠☠☠.Doğru Kelime:",asilkelime)
                break

        print("\n" + "=" * 30 + "\n")

    yeniOyun = input("yeni bir oyun oynamk ister misiniz?(Evet için 'e' / Hayır için 'h'): ")
    if yeniOyun.lower() == 'e':
      while True:#Kelimeyi bulunca oyuncu oyuna yeniden başlaması için olan kod
          tus = input("0 a basarak türleri öğrenebilirsiniz, 1-4 sayılarını seçerek türleri oynayabilirsiniz: ")
          if tus == "0":
              print("Oyun-🤜🏻(1), Yabancı Film-🤜🏻(2), Türk Dizi-🤜🏻(3), Yemek-🤜🏻(4)")
          elif tus == "1":
              print("Zor oyunlar yok bence😑😑😑😑😑")
              print("Oyunu seçtiniz")
              break
          elif tus == "2":
              print("Popülerleri sordum sakın internetten bakma hee")
              print("Yabancı Film seçtiniz")
              break
          elif tus == "3":
              print("Zor sormadım bak😏😏😏😏")
              print("Türk Dizi seçtiniz")
              break
          elif tus == "4":
              print("Aman ha canın çekmesin")
              print("Yemek seçtiniz")
              break
          else:
              print("Yanlış tuşa bastınız😡😡😡😡😡")
      continue
    else:
        print("Gidiyor Gönlümün Efendisi..💔..")
        break


