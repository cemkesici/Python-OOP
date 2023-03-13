class pizza():
    def __init__(self,Pizzafiyat,Pizzaisim):
        self.Pizzafiyat = int(Pizzafiyat)
        self.Pizzaisim=Pizzaisim
    def Pizzacheck(self):
        print(f"{self.Pizzaisim} Pizzası Fiyatı : {self.Pizzafiyat}")   
        
class sos():
    def __init__(self, Sosisim, Sosfiyat):
        self.Sosfiyat = int(Sosfiyat)
        self.Sosisim=Sosisim
    def Soscheck(self):
        print(f"{self.Sosisim} Sosu Fiyatı : {self.Sosfiyat} ")
        
class TurkPizza(pizza):
    def __init__(self):
        self.Pizzafiyat= "105"
        self.Pizzaisim="Türk"
class MargarittaPizza(pizza):
    def __init__(self):
        self.Pizzafiyat= "100"
        self.Pizzaisim="Margeritta"
class KlasikPizza(pizza):
    def __init__(self):
        self.Pizzafiyat = "110"
        self.Pizzaisim="Klasik"
class SadePizza(pizza):
    def __init__(self):
        self.Pizzafiyat= "95"
        self.Pizzaisim="Sade"

class ZeytinSos(sos):
    def __init__(self):
        self.Sosfiyat= "10"
        self.Sosisim="Zeytin"
class SoganSos(sos):
    def __init__(self):
        self.Sosfiyat= "10"
        self.Sosisim="Sogan"
class MisirSos(sos):
    def __init__(self):
        self.Sosfiyat= "10"
        self.Sosisim="Misir"
class MantarSos(sos):
    def __init__(self):
        self.Sosfiyat= "15"
        self.Sosisim="Mantar"
class KeciPeynirSos(sos):
    def __init__(self):
        self.Sosfiyat= "15"
        self.Sosisim="Keci Peyniri"
class EtSos(sos):
    def __init__(self):
        self.Sosfiyat= "20"
        self.Sosisim="Et"

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
                    pizza.Pizzacheck()
                elif secenek == 2:
                    pizza=MargarittaPizza()
                    pizza.Pizzacheck()
                elif secenek == 3:
                    pizza=TurkPizza()
                    pizza.Pizzacheck()
                elif secenek == 4:
                    pizza=SadePizza()
                    pizza.Pizzacheck()
                else:
                    print("Hatalı Seçim Yaptınız!!!")   
                                        
                SosSecenek=int(input("Sos İçin Seçim Yapınız:"))                
                if SosSecenek==11:
                    sos=ZeytinSos()
                    sos.Soscheck()
                elif SosSecenek==12:
                    sos=MantarSos()
                    sos.Soscheck()              
                elif SosSecenek==13:
                    sos=KeciPeynirSos()
                    sos.Soscheck()  
                elif SosSecenek==14:
                    sos=EtSos()
                    sos.Soscheck()  
                elif SosSecenek==15:
                    sos=SoganSos()
                    sos.Soscheck()
                elif SosSecenek==16:
                    sos=MisirSos()
                    sos.Soscheck()
                else:
                    print("Hatalı Seçim Yaptınız!!!")          
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