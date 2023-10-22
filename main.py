# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 18:25:40 2023

@author: muham
"""
#%%
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from AnaSayfaUI import*
from PyQt5.QtCore import QDate

from PyQt5 import QtWidgets, QtCore

#%%
uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()


#%%
import sqlite3
global curs
global conn

conn = sqlite3.connect('veritabani_muze.db')
curs = conn.cursor()


sorguCreTblMuze = ("CREATE TABLE IF NOT EXISTS MUZE2023(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,    \
                 KayitKodu TEXT NOT NULL UNIQUE,                        \
                 KayitliBolum TEXT NOT NULL,                       \
                 Gorevli TEXT NOT NULL,                           \
                 GirisTarihi TEXT NOT NULL,                              \
                 PassKodu INTEGER NOT NULL,                           \
                 SergiDonemi TEXT NOT NULL,                            \
                 Rg1izni TEXT NOT NULL,                               \
                 Rg2izni TEXT NOT NULL,                               \
                 Rg3izni TEXT NOT NULL,                               \
                 Fikra1izni TEXT NOT NULL,                               \
                 Fikra2izni TEXT NOT NULL,                               \
                 Rg4izni TEXT NOT NULL,                               \
                 Mulga1izni TEXT NOT NULL,                       \
                 Mulga2izni TEXT NOT NULL)")

    
curs.execute(sorguCreTblMuze)
conn.commit()


sorguCreTblSilinen = ("CREATE TABLE IF NOT EXISTS SilinenKayitlar(                 \
                      Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,    \
                      KayitKodu TEXT NOT NULL,                        \
                      KayitliBolum TEXT NOT NULL,                       \
                      Gorevli TEXT NOT NULL,                           \
                      GirisTarihi TEXT NOT NULL,                              \
                      PassKodu INTEGER NOT NULL,                           \
                      SergiDonemi TEXT NOT NULL,                            \
                      Rg1izni TEXT NOT NULL,                               \
                      Rg2izni TEXT NOT NULL,                               \
                      Rg3izni TEXT NOT NULL,                               \
                      Fikra1izni TEXT NOT NULL,                               \
                      Fikra2izni TEXT NOT NULL,                               \
                      Rg4izni TEXT NOT NULL,                               \
                      Mulga1izni TEXT NOT NULL,                       \
                      Mulga2izni TEXT NOT NULL)")
    
curs.execute(sorguCreTblSilinen)
conn.commit()
#%%

def ekle():
    _leKayitKodu=ui.lineEdit.text()
    _comboKayitliBolum=ui.comboBox.currentText()
    _comboGorevli=ui.comboBox_2.currentText()
    _deGirisTarihi=ui.dateEdit.date().toString(QtCore.Qt.ISODate)
    _lePassKodu=ui.lineEdit_2.text()
    _comboSergiDonemi=ui.comboBox_3.currentText()
    
    if ui.checkBox_izin1.isChecked():
        _checkBox_izin1="evet"
    else:
        _checkBox_izin1="hayir"
        
    if ui.checkBox_izin2.isChecked():
        _checkBoxizin2="evet"
    else:
        _checkBoxizin2="hayir"
        
    if ui.checkBox_izin3.isChecked():
        _checkBoxizin3="evet"
    else:
        _checkBoxizin3="hayir"
    
    if ui.checkBox_izin4.isChecked():
        _checkBoxizin4="evet"
    else:
        _checkBoxizin4="hayir"
        
    if ui.checkBox_izin5.isChecked():
        _checkBoxizin5="evet"
    else:
        _checkBoxizin5="hayir"
        
    if ui.checkBox_izin6.isChecked():
        _checkBoxizin6="evet"
    else:
        _checkBoxizin6="hayir"
        
    if ui.checkBox_izin7.isChecked():
        _checkBoxizin7="evet"
    else:
        _checkBoxizin7="hayir"
        
    if ui.checkBox_izin8.isChecked():
        _checkBoxizin8="evet"
    else:
        _checkBoxizin8="hayir"
        
    
    _leKayitKodu = ui.lineEdit.text()     #
    # Diğer kodlar...                      #
    
    curs.execute("DELETE FROM SilinenKayitlar WHERE KayitKodu=?", (_leKayitKodu,))  #
    conn.commit()  #
    
    curs.execute("INSERT INTO MUZE2023 (KayitKodu,KayitliBolum,Gorevli,GirisTarihi,PassKodu,SergiDonemi,Rg1izni,Rg2izni,Rg3izni,Fikra1izni,Fikra2izni,Rg4izni,Mulga1izni,Mulga2izni) \
             VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
             (_leKayitKodu,_comboKayitliBolum,_comboGorevli,_deGirisTarihi,_lePassKodu,_comboSergiDonemi,_checkBox_izin1,_checkBoxizin2,_checkBoxizin3,_checkBoxizin4,_checkBoxizin5,_checkBoxizin6,_checkBoxizin7,_checkBoxizin8))
   


    conn.commit()
    LISTELE()
     
    
    
#%%

def LISTELE():
    
    ui.tableWidget.clear()
    
    ui.tableWidget.setHorizontalHeaderLabels(('No','KayitKodu','kayitliBolum','gorevli', \
                                                  'giristarihi', 'passkodu', 'Sergidonemi', 'rg1izni', \
                                            'rg2izni', 'rg3izni', 'fikra1izni', 'fikra2izni', \
                                            'rg4izni', 'mulga1izni', 'mulga2izni'))
    
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    
    curs.execute("SELECT * FROM MUZE2023")
    
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
            
    ui.comboBox.setCurrentIndex(-1)
    ui.comboBox_2.setCurrentIndex(-1)
    ui.comboBox_3.setCurrentIndex(-1)
    ui.lineEdit.clear()
    ui.lineEdit_2.clear()
    tarih = QDate(2023, 1, 1)
    ui.dateEdit.setDate(tarih)
    ui.checkBox_izin1.setChecked(False)
    ui.checkBox_izin2.setChecked(False)
    ui.checkBox_izin3.setChecked(False)
    ui.checkBox_izin4.setChecked(False)
    ui.checkBox_izin5.setChecked(False)
    ui.checkBox_izin6.setChecked(False)
    ui.checkBox_izin7.setChecked(False)
    ui.checkBox_izin8.setChecked(False)
            
            
 


LISTELE()



#%%

def ESERCIKISI():
    cevap = QMessageBox.question(pencere, "KAYIT SİL", "Kaydı silmek istediğinize emin misiniz?", QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        secili = ui.tableWidget.selectedItems()
        silinecek = secili[0].text()
        try:
            
            curs.execute("INSERT INTO SilinenKayitlar SELECT * FROM MUZE2023 WHERE KayitKodu='%s'" % (silinecek))
            conn.commit()
            
            curs.execute("DELETE FROM MUZE2023 WHERE KayitKodu='%s'" % (silinecek))
            conn.commit()

           

            LISTELE()
            ui.statusbar.showMessage("Kayıt silme işlemi başarılı bir şekilde gerçekleşti...")
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı: " + str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi...")



#%%
def ARA():
    aranan1=ui.lineEdit.text()     #kayitkodu
    aranan2=ui.comboBox.currentText()  #kayitli bölüm
    aranan3=ui.comboBox_2.currentText() #görevli
    curs.execute("SELECT * FROM MUZE2023 WHERE KayitKodu=? OR KayitliBolum=? OR Gorevli=?",  \
                 (aranan1,aranan2,aranan3))
    conn.commit()
    ui.tableWidget.clear()
    
    ui.tableWidget.setHorizontalHeaderLabels(('No','KayitKodu','kayitliBolum','gorevli', \
                                                  'giristarihi', 'passkodu', 'Sergidonemi', 'rg1izni', \
                                            'rg2izni', 'rg3izni', 'fikra1izni', 'fikra2izni', \
                                            'rg4izni', 'mulga1izni', 'mulga2izni'))
        
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
#%%
def DOLDUR():
    selected_items = ui.tableWidget.selectedItems()
    if len(selected_items) == 0 or len(selected_items) < 15:  #IndexError: olmasın diye
        return
    
    ui.comboBox.setCurrentText(selected_items[2].text())
    ui.lineEdit.setText(selected_items[1].text())
    ui.comboBox_2.setCurrentText(selected_items[3].text())
    

    giris_tarihi_str = selected_items[4].text()
    giris_tarihi = QtCore.QDate.fromString(giris_tarihi_str, "yyyy-MM-dd")
    ui.dateEdit.setDate(giris_tarihi)
    
    ui.lineEdit_2.setText(selected_items[5].text())
    ui.comboBox_3.setCurrentText(selected_items[6].text())
    

    rg1_izin = selected_items[7].text()
    ui.checkBox_izin1.setChecked(rg1_izin == "evet")
    
    rg2_izin = selected_items[8].text()
    ui.checkBox_izin2.setChecked(rg2_izin == "evet")
    
    rg3_izin = selected_items[9].text()
    ui.checkBox_izin3.setChecked(rg3_izin == "evet")
    
    fikra1_izin = selected_items[10].text()
    ui.checkBox_izin4.setChecked(fikra1_izin == "evet")
    
    fikra2_izin = selected_items[11].text()
    ui.checkBox_izin5.setChecked(fikra2_izin == "evet")
    
    rg4_izin = selected_items[12].text()
    ui.checkBox_izin6.setChecked(rg4_izin == "evet")
    
    mulga1_izin = selected_items[13].text()
    ui.checkBox_izin7.setChecked(mulga1_izin == "evet")
    
    mulga2_izin = selected_items[14].text()
    ui.checkBox_izin8.setChecked(mulga2_izin == "evet")
        


#%%
def guncelle():
    # Seçili öğeleri al
    selected_items = ui.tableWidget.selectedItems()
    if len(selected_items) == 0 or len(selected_items) < 15:  # IndexError önlemi
        return

    
    kayit_kodu = selected_items[1].text()
    kayitli_bolum = ui.comboBox.currentText()
    gorevli = ui.comboBox_2.currentText()
    giris_tarihi = ui.dateEdit.date().toString(QtCore.Qt.ISODate)
    pass_kodu = ui.lineEdit_2.text()
    sergi_donemi = ui.comboBox_3.currentText()
    rg1_izin = "evet" if ui.checkBox_izin1.isChecked() else "hayir"
    rg2_izin = "evet" if ui.checkBox_izin2.isChecked() else "hayir"
    rg3_izin = "evet" if ui.checkBox_izin3.isChecked() else "hayir"
    fikra1_izin = "evet" if ui.checkBox_izin4.isChecked() else "hayir"
    fikra2_izin = "evet" if ui.checkBox_izin5.isChecked() else "hayir"
    rg4_izin = "evet" if ui.checkBox_izin6.isChecked() else "hayir"
    mulga1_izin = "evet" if ui.checkBox_izin7.isChecked() else "hayir"
    mulga2_izin = "evet" if ui.checkBox_izin8.isChecked() else "hayir"

    
    curs.execute(
        "UPDATE MUZE2023 SET KayitliBolum=?, Gorevli=?, GirisTarihi=?, PassKodu=?, SergiDonemi=?, Rg1izni=?, Rg2izni=?, Rg3izni=?, Fikra1izni=?, Fikra2izni=?, Rg4izni=?, Mulga1izni=?, Mulga2izni=? WHERE KayitKodu=?",
        (kayitli_bolum, gorevli, giris_tarihi, pass_kodu, sergi_donemi, rg1_izin, rg2_izin, rg3_izin, fikra1_izin,
         fikra2_izin, rg4_izin, mulga1_izin, mulga2_izin, kayit_kodu))
    conn.commit()

    LISTELE()  # Güncelleme sonrası tabloyu yeniden listele


    
    


    
    
#%%


ui.pushButton_ekle.clicked.connect(ekle)
ui.pushButton_listele.clicked.connect(LISTELE)
ui.pushButton_sil.clicked.connect(ESERCIKISI)
ui.pushButton_2.clicked.connect(ARA)
def tableItemClicked():
    DOLDUR()


ui.tableWidget.itemSelectionChanged.connect(tableItemClicked)
ui.pushButton_guncelle.clicked.connect(guncelle)





sys.exit(uygulama.exec_())