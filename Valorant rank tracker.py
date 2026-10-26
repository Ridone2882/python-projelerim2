
print("===== VALORANT RANK SISTEMI =====")
print()

ranklar = ["Iron", "Bronze", "Silver", "Gold",
           "Platinum", "Diamond", "Ascendant",
           "Immortal", "Radiant"]

print("Hangi ranktasin?")
print()

for i in range(len(ranklar)):
    print(i + 1, "-", ranklar[i])

rank_no = int(input("Rank numaran: "))

while rank_no < 1 or rank_no > 9:
    print("Hatali secim yaptin!")
    rank_no = int(input("Rank numaran: "))

puan = int(input("Mevcut RR puanin (0-99): "))

while puan < 0 or puan > 99:
    print("Puan 0 ile 99 arasinda olmali!")
    puan = int(input("Mevcut RR puanin (0-99): "))

galibiyet = 0
maglubiyet = 0
kill_toplam = 0
death_toplam = 0
maclar = []

while True:
    print()
    print("========== ANA MENU ==========")
    print()
    print("1 - Mac sonucu gir")
    print("2 - Istatistiklerime bak")
    print("3 - Gecmis maclari gor")
    print("4 - Cikis")
    print()

    secim = input("Ne yapmak istiyorsun? ")
    print()

    if secim == "1":
        sonuc = input("Mac sonucu (kazandi/kaybetti): ").lower()

        if sonuc != "kazandi" and sonuc != "kaybettş":
            print("Hatali mac sonucu!")
            continue

        kill = int(input("Kac kill aldin? "))
        death = int(input("Kac kere oldun? "))
        rr = int(input("Bu macta kac RR degisti? "))

        if kill < 0 or death < 0 or rr < 0:
            print("Degerler negatif olamaz")
            continue

        kill_toplam += kill
        death_toplam += death

        if sonuc == "kazandi":
            galibiyet += 1
            puan += rr

            maclar.append(
                "Kazandi | Kill: " + str(kill) +
                " | Death: " + str(death) +
                " | +" + str(rr) + " RR"
            )

        else:
            maglubiyet += 1
            puan -= rr

            maclar.append(
                "Kaybetti | Kill: " + str(kill) +
                " | Death: " + str(death) +
                " | -" + str(rr) + " RR"
            )

        while puan >= 100 and rank_no < 9:
            puan -= 100
            rank_no += 1

        while puan < 0 and rank_no > 1:
            rank_no -= 1
            puan += 100

        if puan < 0:
            puan = 0

        if rank_no == 9 and puan >= 100:
            puan = 100

        print()
        print("Maç kaysedildi!")
        print("Guncel rank:", ranklar[rank_no - 1])
        print("Guncel RR:", puan)

        if death > 0:
            print("Bu macin K/D orani:", round(kill / death, 2))
        else:
            print("Bu macta hic olmedin!")

    elif secim == "2":
        toplam_mac = galibiyet + maglubiyet

        print("======= ISTATISTIKLER =======")
        print()
        print("Rank:", ranklar[rank_no - 1])
        print("RR puani:", puan)
        print("Toplam mac:", toplam_mac)
        print("Galibiyet:", galibiyet)
        print("Maglubiyet:", maglubiyet)
        print("Toplam kill:", kill_toplam)
        print("Toplam death:", death_toplam)

        if toplam_mac > 0:
            oran = galibiyet / toplam_mac * 100
            print("Kazanma orani: %", round(oran, 2))

        if death_toplam > 0:
            kd = kill_toplam / death_toplam
            print("Genel K/D orani:", round(kd, 2))
        elif kill_toplam > 0:
            print("Genel K/D: Hic olum yok!")
        else:
            print("K/D hesaplamak icin mac verisi yok.")

    elif secim == "3":
        print("======= GECMIS MACLAR =======")
        print()

        if len(maclar) == 0:
            print("Henuz mac gecmisin yok.")
        else:
            for i in range(len(maclar)):
                print(i + 1, "-", maclar[i])

    elif secim == "4":
        print("Programdan cikiliyor. Iyi oyunlar!")
        break

    else:
        print("Hatali secim yaptin, tekrar dene!")

