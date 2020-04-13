from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import random
import sonsözlük
from sonsözlük import *

class Pencere2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(600,100,700,700)
        self.setWindowTitle("Kelime Listesi")
        self.anawidget = self.anaWidget()
        self.setCentralWidget(self.anawidget)
        self.centralWidget()

    def anaWidget(self):
        widget = QWidget()
        self.grup1 = QGroupBox()
        self.h_box2 = QHBoxLayout()
        self.v_box2 =QVBoxLayout()
        self.v_box3 =QVBoxLayout()
        self.alan = QGroupBox()
        self.getir = QPushButton("Kelimeleri Getir")
        self.sil = QPushButton("Kelimeleri Sil")
        self.table = QTableWidget()
        #self.table.setRowCount(4)
        self.table.setColumnCount(3)
        self.bilgi = QLabel()

        self.v_box2.addWidget(self.getir)
        self.v_box2.addWidget(self.sil)
        self.v_box2.addWidget(self.bilgi)
        self.grup1.setLayout(self.v_box2)

        self.h_box2.addWidget(self.grup1)
        self.alan.setLayout(self.v_box3)
        self.v_box3.addWidget(self.table)
        self.h_box2.addWidget(self.alan)
        widget.setLayout(self.h_box2)

        self.getir.clicked.connect(self.liste_getir_function)
        self.sil.clicked.connect(self.silme_function)

        return widget

    def liste_getir_function(self):
        kelime_listesi = sonsözlük.kütüphane.verileri_al()
        self.kelime_listesi_tmp = kelime_listesi
        self.kelime_sayisi = len(self.kelime_listesi_tmp)
        self.bilgi.setText("""
        #######################
        Kelimeler başarılı bir şekilde çekildi.
        Lütfen CTRL tuşuna baslılı 
        tutarak silmek istediğiniz
        kelime numaralarını işaretleyiniz..
        #######################
        """)

        for i in range (0, self.kelime_sayisi - 1):
            kelime = self.kelime_listesi_tmp[i]
            #self.check = QCheckBox()
            self.table.setRowCount(self.kelime_sayisi)

            self.table.setItem(i,0, QTableWidgetItem(kelime.ingilizce))
            self.table.setItem(i,1, QTableWidgetItem(kelime.türkçe))
            self.table.setItem(i,2, QTableWidgetItem(str(kelime.zorluk)))

    def silme_function(self):
        indexs=[] # silinecek indexleri range ile alıyoruz.
        for item in self.table.selectedRanges():
            indexs.extend(range(item.topRow(),item.bottomRow()+1))
        for i in indexs:
            kelime = self.kelime_listesi_tmp[i]
            sonsözlük.kütüphane.verileri_sil(kelime.ingilizce)
        self.bilgi.setText("""
        ##########################
        Kelimeler başarılı bir şekilde silindi.
        Ekranı güncellemek için Getir butonuna basınız.
        ##########################
        """)


class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Kelime Oyunu")
        self.anawidget = self.anaWidget()
        self.setCentralWidget(self.anawidget)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.show()

########################################################################################################################
    def kelime_ekle(self):
        grup = QGroupBox("Kelime Ekle")
        self.türkce = QLineEdit()
        self.ingilizce = QLineEdit()
        self.zorluk = QLineEdit()
        i1 = QLabel("İngilizce:")
        t2 = QLabel("Türkçe:  ")
        z3 = QLabel("Zorluk:   ")
        self.kaydet = QPushButton("Kaydet")
        self.kelime_list_info = QLabel()

        v_box1 = QVBoxLayout()
        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()
        h_box4 = QHBoxLayout()

        h_box1.addWidget(i1)
        h_box1.addWidget(self.ingilizce)
        h_box2.addWidget(t2)
        h_box2.addWidget(self.türkce)
        h_box3.addWidget(z3)
        h_box3.addWidget(self.zorluk)
        h_box4.addWidget(self.kaydet)
        h_box4.addWidget(self.kelime_list_info)

        v_box1.addLayout(h_box1)
        v_box1.addLayout(h_box2)
        v_box1.addLayout(h_box3)
        v_box1.addLayout(h_box4)



        grup.setLayout(v_box1)

        self.kaydet.clicked.connect(self.kelime_kaydet_function)
        return grup

    def anaWidget(self):
        widget = QWidget()

        self.menu = self.menuBar()
        self.Oyun = self.menu.addMenu("Oyun")
        self.Ekleme = self.Oyun.addAction("Kelime Ekle")
        self.Cıkar = self.Oyun.addAction("Kelime Sil")

        self.grup = QGroupBox("KELİME OYUNU")
        yazi1 = QLabel("Zorluk Seçiniz:")
        yazi1.setMaximumWidth(150)
        self.zorluklistesi = QComboBox()
        for i in range(1, 6):
            self.zorluklistesi.addItem(str(i))

        self.kelime_getir = QPushButton("Getir")
        self.kelime_getir.setMaximumWidth(50)
        self.random_kelime = QLabel()
        self.cevap = QLineEdit()
        self.gönder = QPushButton("Cevabı Gönder")
        self.degerlendirme = QLabel("Degerlendirme")
        self.toplam_puan = QLabel("Toplam Puan")
        self.pencere2 = Pencere2()

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(yazi1)
        self.h_box.addWidget(self.zorluklistesi)
        self.h_box.addWidget(self.kelime_getir)
        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.random_kelime)
        self.v_box.addWidget(self.cevap)
        self.v_box.addWidget(self.gönder)
        self.v_box.addWidget(self.degerlendirme)
        self.v_box.addWidget(self.toplam_puan)
        self.grup.setLayout(self.v_box)


        self.gönder.clicked.connect(self.gonder_function);
        self.kelime_getir.clicked.connect(self.getir_function);
        self.Ekleme.triggered.connect(self.kelime_ekle_function)
        self.Cıkar.triggered.connect(self.kelime_cikar_function)
        self.kelimeekleme = self.kelime_ekle()

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.grup)
        self.v_box.addWidget(self.kelimeekleme)
        self.kelimeekleme.setVisible(False)
        widget.setLayout(self.v_box)
        return widget

#########################################################################################################################
    def yeni_kelime_function(self):
        self.index = random.randint(0, self.kelime_sayisi) - 1
        self.kelime = self.kelime_listesi_tmp[self.index]
        self.random_kelime.setText(self.kelime.ingilizce)

    def gonder_function(self):
        if (self.cevap.text() == self.kelime.türkçe):
            self.puan = self.puan + 10 * self.kelime.zorluk
            self.toplam_puan.setText("Toplam Puan:" + str(self.puan))
            self.degerlendirme.setText("Değerlendirme: Doğru Cevap Aldığınız Puan:" + str(10 * self.kelime.zorluk))
            self.yeni_kelime_function()
        elif (self.cevap.text() != self.kelime.türkçe):
            self.puan = self.puan - 10 * self.kelime.zorluk
            self.toplam_puan.setText("Toplam Puan:" + str(self.puan))
            self.degerlendirme.setText("Değerlendirme: Yanlış Cevap Kaybettiğiniz Puan:" + str(10 * self.kelime.zorluk) + "    DOĞRU CEVAP: " + self.kelime.türkçe)
            self.yeni_kelime_function()

    def kelime_ekle_function(self):
        self.kelimeekleme.setVisible(True)

    def kelime_kaydet_function(self):
        self.i1 = self.ingilizce.text()
        self.i2 = self.türkce.text()
        self.i3 = self.zorluk.text()
        sonsözlük.kütüphane.veri_ekle(self.i1, self.i2, self.i3)
        kelimeList=sonsözlük.kütüphane.verileri_al()
        self.kelime_list_info.setText("Kelime Başarı ile eklendi. Toplam Kelime Sayısı : "+str(len(kelimeList)))

    def kelime_cikar_function(self):
        self.pencere2.show()

    def getir_function(self):
        self.puan = 0
        kelime_listesi = sonsözlük.kütüphane.verileri_al()
        self.kelime_listesi_tmp = kelime_listesi
        self.kelime_sayisi = len(self.kelime_listesi_tmp)
        self.yeni_kelime_function()
        #self.random_index = random.randint(0, self.kelime_sayisi) - 1
        #self.random_kelime_dogru = self.kelime_listesi_tmp[self.random_index]
        #self.random_kelime.setText(self.random_kelime_dogru.ingilizce)

########################################################################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #sonsözlük.kütüphane.bağlantı_oluştur()
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())