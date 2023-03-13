class pizza():
    def __init__(self,Pizzafiyat,isim):
        self.Pizzafiyat = int(Pizzafiyat)
        self.isim=isim
    def Pizzafiyatcheck(self):
        print("Pizza Fiyat : "+self.Pizzafiyat)   
        
class sos():
    def __init__(self, isim, Sosfiyat):
        self.Sosfiyat = int(Sosfiyat)
        self.isim=isim
    def Sosfiyatcheck(self):
        print("Sos Fiyat : "+ self.Sosfiyat)
        
class TurkPizza(pizza):
    def __init__(self):
        self.Pizzafiyat= "105"
        
class MargarittaPizza(pizza):
    def __init__(self):
        self.Pizzafiyat= "100"
        
class KlasikPizza(pizza):
    def __init__(self):
        self.Pizzafiyat = "110"
        
class SadePizza(pizza):
    def __init__(self):
        self.Pizzafiyat= "95"

class ZeytinSos(sos):
    def __init__(self):
        self.Sosfiyat= "10"
class SoganSos(sos):
    def __init__(self):
        self.Sosfiyat= "10"
class MisirSos(sos):
    def __init__(self):
        self.Sosfiyat= "10"
class MantarSos(sos):
    def __init__(self):
        self.Sosfiyat= "15"
class KeciPeynirSos(sos):
    def __init__(self):
        self.Sosfiyat= "15"
class EtSos(sos):
    def __init__(self):
        self.Sosfiyat= "20"

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
                    pizza.Pizzafiyatcheck()
                elif secenek == 2:
                    pizza=MargarittaPizza()
                    pizza.Pizzafiyatcheck()
                elif secenek == 3:
                    pizza=TurkPizza()
                    pizza.Pizzafiyatcheck()
                elif secenek == 4:
                    pizza=SadePizza()
                    pizza.Pizzafiyatcheck()
                else:
                    print("Hatalı Seçim Yaptınız!!!")   
                                        
                SosSecenek=int(input("Sos İçin Seçim Yapınız:"))                
                if SosSecenek==11:
                    sos=ZeytinSos()
                    sos.Sosfiyatcheck()
                elif SosSecenek==12:
                    sos=MantarSos()
                    sos.Sosfiyatcheck()              
                elif SosSecenek==13:
                    sos=KeciPeynirSos()
                    sos.Sosfiyatcheck()  
                elif SosSecenek==14:
                    sos=EtSos()
                    sos.Sosfiyatcheck()  
                elif SosSecenek==15:
                    sos=SoganSos()
                    sos.Sosfiyatcheck()
                elif SosSecenek==16:
                    sos=MisirSos()
                    sos.Sosfiyatcheck()
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