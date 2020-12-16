import random

isim = input("isminizi giriniz:")
yas = int(input("yasinizi giriniz:"))
can = 10


oyunagiris = input("Oyuna girmek istiyormusunuz E/H")
if yas ==18 and oyunagiris=="E":
    print("oyuna giris yaptiniz iyi oyunlar")
hangiyol = input("hangiyol")
if hangiyol == "sag":
    hasar = random.randint(1,10)
    ödul = random.randint(1,10)
    result = (can-hasar)    
    print(f"Sağ yolu seçtiniz aldığınız hasar{hasar} aldığınız ödül{ödul}")
    if result == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            print(f"kalan canınız {result} 0'dan yukarı olduğu için bu seviyeye katılmaya hak kazandınız")
    if hangiyol == "sag":
        hasar = random.randint(1,10)
        ödul = random.randint(1,10)
        result=can-hasar
        print(f" GÖZLERİ KIRMIZI ! aldığın hasar{hasar} kalan can {result} oyunu tamamladın: tebrikler  ")    
if hangiyol == "sol":
    hasar = random.randint(1,10)
    ödul = random.randint(1,10)
    result = (can-hasar)
    print(f"sol yolu sectiniz aldığınız hasar {hasar} aldığınız ödül {ödul} kalan canınız {result}")
    if result == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
        print(f"kalan canınız {result} 0'dan yukarı olduğu için bu seviyeye katılmaya hak kazandınız")
        if hangiyol == "sol":
            hasar = random.randint(1,10)
            ödul = random.randint(1,10)
            result=can-hasar
            print(f"sol yolda kayaya çarptın aldığın hasar{hasar} kalan can {result} oyunu tamamladın: tebrikler")


