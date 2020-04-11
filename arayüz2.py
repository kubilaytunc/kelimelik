from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import random
import sonsözlük

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
        self.table.setColumnCount(4)

        self.v_box2.addWidget(self.getir)
        self.v_box2.addWidget(self.sil)
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

        for i in range (0, self.kelime_sayisi - 1):
            kelime = self.kelime_listesi_tmp[i]
            self.check = QCheckBox()
            self.table.setRowCount(self.kelime_sayisi)
            self.table.setCellWidget(i, 0, self.check)
            self.table.setItem(i,1, QTableWidgetItem(kelime.ingilizce))
            self.table.setItem(i,2, QTableWidgetItem(kelime.türkçe))
            self.table.setItem(i,3, QTableWidgetItem(str(kelime.zorluk)))


    def silme_function(self):
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                item = self.table.item(i,j)
                if item.checkState() == QCheckBox.isChecked(True):
                    self.sil = self.table.item(i,1).text()
                    sonsözlük.kütüphane.verileri_sil(self.sil)

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
        t1 = QLabel("Türkçe")
        i2 = QLabel("İngilizce")
        z3 = QLabel("Zorluk")
        self.kaydet = QPushButton("Kaydet")
        self.kelime_list_info = QLabel()

        v_box1 = QVBoxLayout()
        v_box1.addWidget(t1)
        v_box1.addWidget(i2)
        v_box1.addWidget(z3)
        v_box1.addWidget(self.kaydet)


        v_box2 = QVBoxLayout()
        v_box2.addWidget(self.türkce)
        v_box2.addWidget(self.ingilizce)
        v_box2.addWidget(self.zorluk)
        v_box2.addWidget(self.kelime_list_info)

        h_box = QHBoxLayout()
        h_box.addLayout(v_box1)
        h_box.addLayout(v_box2)


        grup.setLayout(h_box)

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
            self.degerlendirme.setText("Değerlendirme: Doğru Cevap Aldığınız Puan:" + str(self.x))
            self.yeni_kelime_function()
        elif (self.cevap.text() != self.kelime.türkçe):
            self.puan = self.puan - 10 * self.kelime.zorluk
            self.toplam_puan.setText("Toplam Puan:" + str(self.puan))
            self.degerlendirme.setText("Değerlendirme: Yanlış Cevap Kaybettiğiniz Puan:" + str(self.x) + "    DOĞRU CEVAP: " + self.kelime.türkçe)
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