class pizza():
    def __init__(self,fiyat,isim):
        self.fiyat = int(fiyat)
        self.isim=isim
    def fiyatcheck(self):
        print("Pizza Fiyat : "+self.fiyat)   
        
class sos():
    def __init__(self, isim, fiyat):
        self.fiyat = int(fiyat)
        self.isim=isim
    def fiyat(self):
        print("Sos Fiyat : "+ self.fiyat)
        
class TurkPizza(pizza):
    def __init__(self):
        self.fiyat= "105"
        
class MargarittaPizza(pizza):
    def __init__(self):
        self.fiyat= "100"
        
class KlasikPizza(pizza):
    def __init__(self):
        self.fiyat = "110"
        
class SadePizza(pizza):
    def __init__(self):
        self.fiyat= "95"

class ZeytinSos(sos):
    def __init__(self):
        self.fiyat= "10"
class SoganSos(sos):
    def __init__(self):
        self.fiyat= "10"
class MisirSos(sos):
    def __init__(self):
        self.fiyat= "10"
class MantarSos(sos):
    def __init__(self):
        self.fiyat= "15"
class KeciPeynirSos(sos):
    def __init__(self):
        self.fiyat= "15"
class EtSos(sos):
    def __init__(self):
        self.fiyat= "20"

def main():        
    try:      
        menu=open("menu.txt",encoding='utf-8')
        print(menu.read())
        tempTrue=True
        while tempTrue:
            secenek=int(input("Pizza Tabanı İçin Seçim Yapınız:"))
            if secenek >=1 and secenek<=4:
                #tempTrue=False    
                if secenek == 1:
                    pizza=KlasikPizza()
                    pizza.fiyatcheck()
                elif secenek == 2:
                    pizza=MargarittaPizza()
                    pizza.fiyatcheck()
                elif secenek == 3:
                    pizza=TurkPizza()
                    pizza.fiyatcheck()
                elif secenek == 4:
                    pizza=SadePizza()
                    pizza.fiyatcheck()
            elif secenek >=5:
                print("Pizza Tabanı Türü Seçmelisiniz!!!")
                tempTrue2=True
                while tempTrue2:
                    devam=input("Tekrar Seçim Yapmak İster Misiniz? E/H")
                    if devam =='E'or devam =='e':
                        tempTrue=True
                        tempTrue2=False
                    elif devam =='H'or devam =='h':
                        tempTrue=False
                        tempTrue2=False
                        break
                    else:
                        print("Hatalı Giriş Yaptınız!!!")
                        tempTrue=True
    except:
        print("Hatalı Giriş Yaptınız Sayı Girmelisiniz!!!")
    finally:
        menu.close()
if __name__=="__main__":
    main()