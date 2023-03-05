#Hesap Makinesi

def toplama(sayi1, sayi2):
    toplam = sayi1+sayi2
    return toplam

def cikartma(sayi1, sayi2):
    return sayi1-sayi2

def carpma(sayi1, sayi2):
    return sayi1*sayi2

def bolme(sayi1, sayi2):
    return sayi1/sayi2

def ussu(sayi1, sayi2):
    return sayi1**sayi2

def hesapla():
    print("Hesap makinesine hoşgeldiniz")
    a = int(input("İlk sayıyı giriniz: "))
    b = int(input("İkinci sayıyı giriniz: "))
    operasyon = int(input(" toplama için 1\n çıkartma için 2\n çarpma için 3\n bölme için 4\n üssü için 5\n Giriniz: "))
    
    if operasyon == 1:
        print("Toplam: ", toplama(a, b))
        return
    if operasyon == 2:
        print("Fark: ", cikartma(a, b))
        return
    if operasyon == 3:
        print("Çarpım: ", carpma(a, b))
        return
    if operasyon == 4:
        print("Bölüm: ", bolme(a, b))
        return
    if operasyon == 5:
        print("Üssü: ", ussu(a, b))
        return
    else:
        print("Böyle bir işlem yoktur. Lütfen geçerli bir işlem giriniz\n\n")
        hesapla()
        
    
hesapla()
