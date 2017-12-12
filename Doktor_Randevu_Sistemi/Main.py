class Kullanici:
    def __init__(self, ad, soyad, id, password):
        self.ad = ad
        self.soyad = soyad
        self.id = id
        self.password = password

class Doktor(Kullanici):
    def __init__(self, ad, soyad, id, password):
        self.randevu = []
        super(Doktor, self).__init__(ad, soyad, id, password)

class Hasta(Kullanici):
    def __init__(self, ad, soyad, id, password):
        super(Hasta, self).__init__(ad, soyad, id, password)
        print("asdasd")