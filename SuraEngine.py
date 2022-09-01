import numpy as np
ver_a = ''
ver_c = ''
def ify(degisken,operator,deger):
    dogru_mu = 0
    if degisken == 'a':
        if operator == '=':
            if ver_a == deger:
                dogru_mu = 1
        if operator == '!=':
            if ver_a != deger:
                dogru_mu = 1
        if operator == '<':
            if ver_a < deger:
                dogru_mu = 1
        if operator == '>':
            if ver_a > deger:
                dogru_mu = 1
    if degisken == 'b':
        if operator == '=':
            if ver_b == deger:
                dogru_mu = 1
        if operator == '!=':
            if ver_b != deger:
                dogru_mu = 1
        if operator == '<':
            if ver_b < deger:
                dogru_mu = 1
        if operator == '>':
            if ver_b > deger:
                dogru_mu = 1
    if degisken == 'c':
        if operator == '=':
            if ver_c == deger:
                dogru_mu = 1
        if operator == '!=':
            if ver_c != deger:
                dogru_mu = 1
        if operator == '<':
            if ver_c < deger:
                dogru_mu = 1
        if operator == '>':
            if ver_c > deger:
                dogru_mu = 1
    return dogru_mu

print("© Bütün hakları Sahiptir Sura Games 2022")
print("1.8 sürümündeki yenilikler bazı uygunsuz hatalar düzeltildi ve string ve numpy fonksiyonunu ekledik ")
print("https://suragames.tr.gg/ web sitesine gidebilirsiniz")
print("merhaba Sura Script programlama diline hoşgeldiniz")
print("Güvenlik Denetliniyor Lütfen Bekliyiniz")
print("Güvenlik denetlendi")
def fonksiyonum(ad, soyad):
  print("Adınız: " + ad + ", Soyadınız: " + soyad)
fonksiyonum("mehmet", "a1k")
def fonksiyonum(): print("Bir fonksiyondan merhaba!") 
fonksiyonum()
string = "yemreak"
tek_metin = "yemre"
metinler = ['emre', 'ak']
x = np.array([1, 2, 3])
print(x)
#array([1, 2, 3])
y = np.arange(10)
print(y)
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a = 200
b = 33
if b > a:
  print("b büyüktür.")
elif a == b:
  print("a ve b eşittir")
else:
  print("a büyüktür.")
işlem = input('Oluştur - 1, Çalıştır -2   :')
if işlem == '1':
    ad = input('Dosya Adı:')
    şifre = input('Şifre:')
    with open(ad + '.ss','a') as dosya:
        dosya.write('passcode = ' + şifre + "\n\n.")
if işlem == '2':
    ad = input('Dosya Adı:')
    with open(ad + '.ss') as dosya:
        print('Çalıştırılıyor........\n---------------------------------------------------')
        read = dosya.readlines()
        i = 1
        while True:
            try:
                read[i] = read[i].replace('\n','')
                read[i + 1] = read[i + 1].replace('\n','')
                rood = read[i]
                if 'sys.output = ' in rood:
                    rood = rood.replace('sys.output = ','')
                    rood = rood.replace('\n','')
                    print(rood)
                if 'str; = ' in rood:
                    rood = rood.replace('str; = ','')
                    if 'a' in rood:
                        ver_a = read[i + 1]
                    if 'b' in rood:
                        ver_b = read[i + 1]
                    if 'c' in rood:
                        ver_c = read[i + 1]
                if 'int; = ' in rood:
                    rood = rood.replace('int; = ','')
                    if 'a' in rood:
                        ver_a = int(read[i + 1])
                    if 'b' in rood:
                        ver_b = int(read[i + 1])
                    if 'c' in rood:
                        ver_c = int(read[i + 1])
                if 'sys.output with ver = ' in rood:
                    read[i + 1] = read[i + 1].replace('\n','')
                    rood = rood.replace('sys.output with ver = ','')
                    rood = rood.replace('\n','')
                    if 'a' in read[i + 1]:
                        rood = rood.replace('&',ver_a)
                    if 'b' in read[i + 1]:
                        rood = rood.replace('&',ver_b)
                    if 'c' in read[i + 1]:
                        rood = rood.replace('&',ver_c)
                    print(rood)
                if 'sys.input = ' in rood:
                    rood = rood.replace('sys.input = ','')
                    rood = rood.replace('\n','')
                    if 'a' in read[i + 1]:
                        ver_a = input(rood)
                    if 'b' in read[i + 1]:
                        ver_b = input(rood)
                    if 'c' in read[i + 1]:
                        ver_c = input(rood)
                if 'sys.output if = ' in rood:
                    rood2 = read[i + 1]
                    rood2 = rood2.split()
                    if ify(rood2[0],rood2[1],rood2[2]) == 1:
                        rood = rood.replace('sys.output if = ','')
                        rood = rood.replace('\n','')
                        print(rood)
                if 'sys.input if = ' in rood:
                    rood2 = read[i + 2]
                    rood2 = rood2.split()
                    if ify(rood2[0],rood2[1],rood2[2]) == 1:
                        rood = rood.replace('sys.input if = ','')
                        rood = rood.replace('\n','')
                        if 'a' in read[i + 1]:
                            ver_a = input(rood)
                        if 'b' in read[i + 1]:
                            ver_b = input(rood)
                        if 'c' in read[i + 1]:
                            ver_c = input(rood)
                i += 1
            except:
                break
print("sura programlama dilini kullandığınz için teşekkürler")
