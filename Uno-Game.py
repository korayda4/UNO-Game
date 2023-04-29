import random
import colorama
from colorama import Fore
print(Fore.GREEN+"UNO oyununa hoşgeldiniz!")
renkler = ['Kırmızı', 'Sarı', 'Mavi', 'Yeşil']
kartlar = [f'{renk} {sayı}' for renk in renkler for sayı in range(0, 10)]

oyuncu1_destesi = []
oyuncu2_destesi = []
masa = []

# Kartları karıştır
random.shuffle(kartlar)

for i in range(14):
    if i % 2 == 0:
        oyuncu1_destesi.append(kartlar[i])
    else:
        oyuncu2_destesi.append(kartlar[i])

masa.append(kartlar[14])

# Oyun başlangıcı
sıradaki_oyuncu = 1
while True:
    print(f"\nMasa: {masa[-1]}")
    print(Fore.YELLOW+f"1. oyuncunun elindeki kartlar: {oyuncu1_destesi}")
    print(Fore.CYAN+f"2. oyuncunun elindeki kartlar: {oyuncu2_destesi}")

    if len(oyuncu1_destesi) == 0:
        print("1. oyuncu kazandı!")
        break
    elif len(oyuncu2_destesi) == 0:
        print("2. oyuncu kazandı!")
        break

    if sıradaki_oyuncu == 1:
        secilen_kart = input(Fore.GREEN+"1. oyuncu, masaya atmak istediğiniz kartı seçin: ")
        while secilen_kart not in oyuncu1_destesi:
            print(Fore.RED+"Seçtiğiniz kart elinizde bulunmamaktadır. Lütfen tekrar deneyin.")
            secilen_kart = input(Fore.GREEN+"1. oyuncu, masaya atmak istediğiniz kartı seçin: ")
        oyuncu1_destesi.remove(secilen_kart)
        
    else:
        secilen_kart = input(Fore.GREEN+"2. oyuncu, masaya atmak istediğiniz kartı seçin: ")
        while secilen_kart not in oyuncu2_destesi:
            print(Fore.RED+"Seçtiğiniz kart elinizde bulunmamaktadır. Lütfen tekrar deneyin.")
            secilen_kart = input(Fore.GREEN+"2. oyuncu, masaya atmak istediğiniz kartı seçin: ")
        oyuncu2_destesi.remove(secilen_kart)

    #split ile değerleri ayır ve kontrol et
    if secilen_kart.split()[0] == masa[-1].split()[0] or secilen_kart.split()[1] == masa[-1].split()[1]:
        masa.append(secilen_kart)
        print(Fore.GREEN+f"{sıradaki_oyuncu}. oyuncu, {secilen_kart} kartını masaya attı.")
        if sıradaki_oyuncu == 1:
            sıradaki_oyuncu = 2
        else:
            sıradaki_oyuncu = 1

    else:
        print(Fore.RED+"Seçtiğiniz kart masaya atılamaz. İlk dağıtılan kart elinize ekleniyor.")
        if sıradaki_oyuncu == 1:
            oyuncu1_destesi.append(kartlar[len(oyuncu1_destesi)]); sıradaki_oyuncu = 2

