import random
import sqlite3

kelime_listesi = list()
liste = list()

######## TABLO FONKSİYONLARI #################################################
class Kütüphane():

    def __init__(self):

        self.bağlantı_oluştur()

    def bağlantı_oluştur(self):
        self.bağlantı = sqlite3.connect("kütüphane.db")
        self.cursor = self.bağlantı.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (ingilizce TEXT,türkçe TEXT,zorluk INT)")
        self.bağlantı.commit()

    def veri_ekle(self,ingilizce,türkçe,zorluk):
        self.cursor.execute("Insert into kitaplık Values(?,?,?)",(ingilizce,türkçe,zorluk))
        self.bağlantı.commit()

    def verileri_al(self):
        self.cursor.execute("Select * From kitaplık")
        liste = self.cursor.fetchall()
        for i in liste:
            kelime = Kelime(i[0],i[1],i[2])
            kelime_listesi.append(kelime)
        return kelime_listesi

    def verileri_güncelle(self,eski,yeni):
        self.cursor.execute("Update kitaplık set ingilizce = ? where ingilizce = ?",(eski,yeni))
        self.bağlantı.commit()

    def verileri_sil(self,silinecek):
        self.cursor.execute("Delete from kitaplık where ingilizce = ?",(silinecek,))
        self.bağlantı.commit()

    def verileri_göster(self):
        self.cursor.execute("Select * From kitaplık")
        liste_sil = self.cursor.fetchall()
        for i in liste_sil:
            print(i)
###############################################################################
class Kelime():
    def __init__(self,ingilizce,türkçe,zorluk):
        self.ingilizce = ingilizce
        self.türkçe = türkçe
        self.zorluk = zorluk
    def __del__(self):
        print("Kelime Siliniyor...")

    def __str__(self):
        return self.ingilizce+ "="+ self.türkçe


##### ANA MENÜ FONKSİYONLARI ##################################################
class Oyun():
    kütüphane = Kütüphane()
    def __init__(self):
        self.kütüphane.bağlantı_oluştur()

    def kelime_ekle(self):
        while True:
            ingilizce = input("Eklemek istediğiniz ingilizce kelimeyi giriniz. Çıkış için (q): ")
            if(ingilizce=="q"):
                break
            türkçe = input("Türkçe anlamını giriniz: ")
            zorluk = input("Zorluk derecesini giriniz[1-5] : ")
            self.kütüphane.veri_ekle(ingilizce,türkçe,zorluk)
            print("Kelime Eklendi")

    def oyun(self):
        self.kütüphane.verileri_al()
        puan = 0
        self.kelime_sayisi = len(kelime_listesi)
        if (self.kelime_sayisi < 2):
            print("UYARI.. Kelime Sayısı yeterli değil..Lütfen Kelime Ekleyiniz.")
        else:
            while True:
                self.kelime_sayisi = len(kelime_listesi)
                if (self.kelime_sayisi == 0):
                    print("OYUN BİTTİ..Toplam Puanınız = ", puan)
                    break
                else:
                    random_index = random.randint(0, self.kelime_sayisi) - 1
                    random_kelime = kelime_listesi[random_index]
                    print("""
                                ***************************
                                {}
                                ***************************""".format(random_kelime.ingilizce))
                    türkçe_anlam = input("Kelimenin türkçe anlamını giriniz:")
                    if (türkçe_anlam == random_kelime.türkçe):
                        puan += (int(random_kelime.zorluk) * 10)
                        print("""
                                    Doğru cevap...
                                    Toplam puan = {}
                                    """.format(puan))
                        del kelime_listesi[random_index]

                    elif (türkçe_anlam == "q"):
                        break
                    else:
                        puan -= (int(random_kelime.zorluk) * 10)
                        print("""
                                        Yanlış Cevap...
                                        Toplam puan = {}
                                        """.format(puan))
                        del kelime_listesi[random_index]

    def kelime_sil(self):
        while True:
            self.kütüphane.verileri_göster()
            silinecek = input("(Çımak için:q) Silinecek ingilizce kelimeyi yazın : ")
            if(silinecek == "q"):
                break
            self.kütüphane.verileri_sil(silinecek)

###############################################################################
kütüphane = Kütüphane()
kütüphane.bağlantı_oluştur()
#oyun = Oyun()

