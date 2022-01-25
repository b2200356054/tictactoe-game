oyun_tahtası = [[' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']]
from time import sleep

def tahta():
    print("    1    2    3")
    for satır_numarası, satırlar in enumerate(oyun_tahtası, start=1):
        print(satır_numarası, satırlar)

tahta()

def kazananyatay():
    for yatay in oyun_tahtası:
        if yatay.count(yatay[0]) == len(yatay) and yatay[0] == "X":
            oyunbitisX()          
        if yatay.count(yatay[0]) == len(yatay) and yatay[0] == "O":
            oyunbitisO()   

def oyunsonu():
    global oyun_tahtası
    oyun_tahtası = [[' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]

def oyunbitisX():
    print("Oyun bitti. Birinci oyuncu kazandı.")
    sleep(2)
    print("Tebrikler.")
    sleep(1)
    oyunsonu()

def oyunbitisO():
    print("Oyun bitti. İkinci oyuncu kazandı.")    
    sleep(2)
    print("Tebrikler.")
    sleep(1)
    oyunsonu()

def kazanandikey():                
    for x in range(3):
        kontroldikey = []
        for dikey in oyun_tahtası:
            kontroldikey.append(dikey[x])
        if kontroldikey.count(dikey[x]) == len(dikey) and kontroldikey[0] == "X":
            oyunbitisX()
            return False
        elif kontroldikey.count(dikey[x]) == len(dikey) and kontroldikey[0] == "O":
            oyunbitisO()
            return False

def kazanancapraz():
    caprazliste = []
    for i, h in zip(reversed(range(len(oyun_tahtası))), range(len(oyun_tahtası))):
        caprazliste.append(oyun_tahtası[i][h])
    if caprazliste.count(caprazliste[0]) == len(caprazliste) and caprazliste[0] == "X":
        oyunbitisX()
    elif caprazliste.count(caprazliste[0]) == len(caprazliste) and caprazliste[0] == "O":
        oyunbitisO()
    caprazliste = []
    for p in range(len(oyun_tahtası)):
        caprazliste.append(oyun_tahtası[p][p])
    if caprazliste.count(caprazliste[0]) == len(caprazliste) and caprazliste[0] == "X":
        oyunbitisX()
    elif caprazliste.count(caprazliste[0]) == len(caprazliste) and caprazliste[0] == "O":
        oyunbitisO()

def kontrol():
    kazanancapraz()
    kazanandikey()
    kazananyatay()

def hamle_genel():
        while True:
            b = int(input("\nHangi satır?\n"))
            c = int(input("\nHangi sütun?\n"))
            oyun_tahtası[b-1][c-1] = "X"
            tahta()   
            kontrol()
            print("\nOyuncu = O")
            b = int(input("\nHangi satır?\n"))
            c = int(input("\nHangi sütun?\n"))
            oyun_tahtası[b-1][c-1] = "O"
            tahta()
            kontrol()
            print("\nOyuncu = X")
        
    
hamle_genel()




''' Oyunu tamamladıktan sonra optimizasyon için hamle_genel() fonksiyonunu 
itertools kullanarak yeniden düzenle. Videoda şunlar gösterildi:'''

#x = [1, 2, 3, 4, 5]
#yineleme = itertools.cycle(x)#

'''Iter'in kelime anlamı "yinelemek". itertools çeşitli yineleme araçlarını barındıran
bir modül. itertools.cycle(x) ise x listesini yinelemeye alan kod. Iterable ve Iterator 
adı verilen iki adet nesnemiz var. Iterable, yenilebilir nesne. Iterator ise next() fonksiyonu
barındıran ve bir nesneyi yinelemeye yarayan nesne. Örnek:'''

#x = [1, 2, 3, 4]
#z = itertools.cycle(x)
#for i in z:
#    print(i)

'''Yukarıdaki kod dizisi, x listesini sonsuza kadar tekrar tekrar yazdırır.'''

#x = [1, 2, 3, 4]
#y = iter(x)
#for i in y:
#    print(i)

'''Yukarıdaki kod dizisi ise x listesinde 1'er 1'er ilerler ve çıktı "1, 2, 3, 4" olur.
"Next" komutunun kullanımı ise şu şekildedir. Bir iterable içerisindeki son konumunu
Phyton aklında tutabilir. Next komutu bir sonraki elemana geçişi sağlar.'''

#x = [1, 2, 3, 4]
#z = itertools.cycle(x)
#print(next(z))
#print(next(z))
#print(next(z))

'''Yukarıdaki kod dizisi x listesinin 1, 2 ve 3. elemanlarını yazdırır. Sırayla bir bir ilerler.
Aynı zamanda bu iterator loop içerisine de alınabilir.Aşağıdaki kod dizisi x listesini
sonsuza kadar alt alta yazdırarak tekrar ettirir.'''

#x = [1, 2, 3, 4]
#z = itertools.cycle(x)
#for i in z:
#   print(i)

'''Ya da belli sayıda tekrar ettirip daha sonra kaldığı yerden tek tek devam ettirilebilir.'''

#x = [1, 2, 3, 4]
#z = itertools.cycle(x)
#for i in range(10):
#   print(next(z))

'''Örneğin yukarıdaki kod dizisi 10 elemanı sırayla tekrar ederek yazdıktan sonra durmaya programlıdır.'''


