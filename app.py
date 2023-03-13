class pizza():
    def __init__(self,fiyat,isim):
        self.fiyat = fiyat
        self.isim=isim
    def start(self):
        print("Pizza is starting")         
class sos():
    def __init__(self):
        pass
    def start(self):
        print("Sos is starting")
    def fiyat(fiyat):
        print("Sos Fiyat : "+ fiyat)
        
class TurkPizza(pizza):
    def __init__(self):
        fiyat= 105
        super().__init__(fiyat)  
class MargarittaPizza(pizza):
    def __init__(self):
        fiyat= 100
        super().__init__(fiyat)
class KlasikPizza(pizza):
    def __init__(self,fiyat):
        self.fiyat = fiyat
    def fiyatcheck(self):
        print("Pizza Fiyat : "+self.fiyat)   
class SadePizza(pizza):
    def __init__(self):
        fiyat= 95

class ZeytinSos(sos):
    def __init__(self):
        self.__fiyat= 10
class SoganSos(sos):
    def __init__(self):
        self.__fiyat= 10
class MisirSos(sos):
    def __init__(self):
        self.__fiyat= 10
class MantarSos(sos):
    def __init__(self):
        self.__fiyat= 15
class KeciPeynirSos(sos):
    def __init__(self):
        self.__fiyat= 15
class EtSos(sos):
    def __init__(self):
        self.__fiyat= 20

def main():        
    try:      
        menu=open("menu.txt",encoding='utf-8')
        print(menu.read())
        tempTrue=True
        while tempTrue:
            secenek=int(input("Pizza Tabanı İçin Seçim Yapınız:"))
            if secenek >=1 and secenek<=4:
                tempTrue=False    
                if secenek == 1:
                    pizza=KlasikPizza()
                    pizza.start()
                    pizza.fiyatcheck(10)
                elif secenek == 2:
                    pizza=MargarittaPizza()
                    pizza.start()
                elif secenek == 3:
                    pizza=TurkPizza()
                    pizza.start()
                elif secenek == 4:
                    pizza=SadePizza()
                    pizza.start()
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