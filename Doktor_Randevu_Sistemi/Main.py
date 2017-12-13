from typing import List
class Kullanici:
    def __init__(self, ad, soyad, id, password):
        self.ad = ad
        self.soyad = soyad
        self.id = id
        self.password = password

class Dosya:
    def __init__(self, ad):
        self.ad = ad
        self.doktor_list = []
        self.hasta_list = []
    def kayit(self):
        with open(self.ad, "r+") as file:
            file.write(data.doktor_list)
            file.write(data.hasta_list)

data = Dosya("Data.txt")

class Doktor(Kullanici):
    def __init__(self, ad, soyad, id, password):
        self.randevu = []
        super(Doktor, self).__init__(ad, soyad, id, password)
        liste = []
        liste.append(self.id)
        liste.append(self.password)
        liste.append(self.ad)
        liste.append(self.soyad)
        liste.append(self.randevu)
        data.doktor_list.append(liste)

class Hasta(Kullanici):
    def __init__(self, ad, soyad, id, password):
        super(Hasta, self).__init__(ad, soyad, id, password)
        liste = []
        liste.append(self.id)
        liste.append(self.password)
        liste.append(self.ad)
        liste.append(self.soyad)
        data.hasta_list.append(liste)

doktor1 = Doktor("Arif","Deniz","id","şifre")
doktor2 = Doktor("Arifss","Denssiz","id","şifre")
hasta1 = Hasta("Hasta Arif","Deniz","id","şifre")
hasta2 = Hasta("Hasta Arif","Denissz","id","şifre")

print(data.hasta_list)
print(data.doktor_list)
data.kayit()
