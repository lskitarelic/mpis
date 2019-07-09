#!/usr/bin/python
#23534950
from tkinter import *
import tkinter


def signal(trenutno):
    if (trenutno == True):
        return "prorada"
    else:
        return "prestanak"

class Prekidac:
    def __init__(self, stanje):
        self.stanje = stanje
        self.SF6_N2_ulje_blokada_rada = False
        self.gubitak_N2_blokada_rada = False
        self.gubitak_SF6_upozorenje = False
        self.nesklad_polova_3P_isklop = False
        self.gubitak_N2_upozorenje = False
        self.gubitak_ulje_blokada_uklopa = False
        self.APU_blokada = False
        self.gubitak_SF6_blokada_rada = False
        self.gubitak_ulja_blokada_rada = False
        self.grijanje_kvar = False

    def ispis_svih(self): 
        text.insert(INSERT, "PREKIDAC\n")
        text.insert(INSERT, "stanje     medupolozaj\n")
        text.insert(INSERT,"stanje     ukljucen\n")
        text.insert(INSERT,"stanje     iskljucen\n")
        text.insert(INSERT,"stanje     kvar signalizacije\n")
        text.insert(INSERT,"SF6;N2;ulje - blokada rada      prorada\n")
        text.insert(INSERT,"SF6;N2;ulje - blokada rada      prestanak\n")
        text.insert(INSERT,"gubitak N2 - blokada rada      prorada\n")
        text.insert(INSERT,"gubitak N2 - blokada rada      prestanak\n")
        text.insert(INSERT,"gubitak SF6 - upozorenje      prorada\n")
        text.insert(INSERT,"gubitak SF6 - upozorenje      prestanak\n")
        text.insert(INSERT,"nesklad polova - 3P isklop      prorada\n")
        text.insert(INSERT,"nesklad polova - 3P isklop      prestanak\n")
        text.insert(INSERT,"gubitak N2 - upozorenje      prorada\n")
        text.insert(INSERT,"gubitak N2 - upozorenje      prestanak\n")
        text.insert(INSERT,"gubitak ulje - blokada uklopa      prorada\n")
        text.insert(INSERT,"gubitak ulje - blokada uklopa      prestanak\n")
        text.insert(INSERT,"APU - blokada      prorada\n")
        text.insert(INSERT,"APU - blokada      prestanak\n")
        text.insert(INSERT,"gubitak SF6 - blokada rada      prorada\n")
        text.insert(INSERT,"gubitak SF6 - blokada rada      prestanak\n")
        text.insert(INSERT,"gubitak ulja - blokada rada      prorada\n")
        text.insert(INSERT,"gubitak ulja - blokada rada      prestanak\n")
        text.insert(INSERT,"grijanje - kvar      prorada\n")
        text.insert(INSERT,"grijanje - kvar      prestanak\n\n\n")
    
    def ispis(self):
        if (self.odrediStanje == True):
            ispis_stanje = "ukljucen"
        else:
            ispis_stanje = "iskljucen"
        text.insert(INSERT, "PREKIDAC\n")
        text.insert(INSERT, "stanje      " + ispis_stanje + "\n")
        text.insert(INSERT, "SF6;N2;ulje - blokada rada      " + signal(self.SF6_N2_ulje_blokada_rada) + "\n")
        text.insert(INSERT, "gubitak N2 - blokada rada      " + signal(self.gubitak_N2_blokada_rada) + "\n")
        text.insert(INSERT, "gubitak SF6 - upozorenje      " + signal(self.gubitak_SF6_upozorenje) + "\n")
        text.insert(INSERT, "nesklad polova - 3P isklop      " + signal(self.nesklad_polova_3P_isklop) + "\n")
        text.insert(INSERT, "gubitak N2 - upozorenje      " + signal(self.gubitak_N2_upozorenje) + "\n")
        text.insert(INSERT, "gubitak ulje - blokada uklopa      " + signal(self.gubitak_ulja_blokada_rada) + "\n")
        text.insert(INSERT, "APU - blokada      " + signal(self.APU_blokada) + "\n")
        text.insert(INSERT, "gubitak SF6 - blokada rada      " + signal(self.gubitak_SF6_blokada_rada) + "\n")
        text.insert(INSERT, "gubitak ulja - blokada rada      " + signal(self.gubitak_ulja_blokada_rada) + "\n")
        text.insert(INSERT, "grijanje - kvar      " + signal(self.grijanje_kvar) + "\n\n\n")


    def odrediStanje(self):
        return self.stanje

    def iskljuci(self):
        text.insert(INSERT,  "Isključujem Prekidač...\n")
        self.stanje = False

    def ukljuci(self):
        text.insert(INSERT,  "Uključujem Prekidač...\n")
        self.stanje = True



class Rastavljac:
    def __init__(self, stanje, name):
        self.stanje = stanje
        self.name = name

    def odrediStanje(self):
        return self.stanje

    def iskljuci(self):
        text.insert(INSERT,  "Isključujem Rastavljač " + self.name + "...\n")
        self.stanje = False

    def ukljuci(self):
        text.insert(INSERT,  "Uključujem Rastavljač " + self.name + "...\n")
        self.stanje = True

    def ispis_svih(self):
        text.insert(INSERT, "RASTAVLJAC\n")
        text.insert(INSERT, "stanje     medupolozaj\n")
        text.insert(INSERT,"stanje     ukljucen\n")
        text.insert(INSERT,"stanje     iskljucen\n")
        text.insert(INSERT,"stanje     kvar signalizacije\n")

    def ispis(self):
        if (self.odrediStanje):
            ispis_stanje = "ukljucen"
        else:
            ispis_stanje = "iskljucen"
        text.insert(INSERT, "PREKIDAC\n")
        text.insert(INSERT, "stanje      " + ispis_stanje + "\n\n\n")


class Mjerenja:
    def __init__(self):
        self.U = "10.5 MW"
        self.Q = "-5.0 HZ"
        self.JT = "2500.0 kVArh"
           
    def ukljuci(self):
        self.U = "10.5 MW"
        self.Q = "-5.0 HZ"
        self.JT = "2500.0 kVArh"
        unos1.insert(INSERT,  self.U)
        unos2.insert(INSERT,  self.Q)
        unos3.insert(INSERT,  self.JT)
    
    def iskljuci(self):
        self.U = "0.0 MW"
        self.Q = "0.0 HZ"
        self.JT = "2500.0 kVArh"
        unos1.insert(INSERT,  self.U)
        unos2.insert(INSERT,  self.Q)
        unos3.insert(INSERT,  self.JT)

    def ispis_svih(self): 
        text.insert(INSERT, "Mjerenja\n")
        text.insert(INSERT, "radna snaga (MW)     mjerena vel.\n")
        text.insert(INSERT, "Frekvencija (Hz)     mjerena vel.\n")
        text.insert(INSERT, "jalova snaga (kVArh)     mjerena vel.\n")
        text.insert(INSERT, "alarm     prorada\n")
        text.insert(INSERT, "alarm     prestanak\n\n\n")
    

class Zastita():
    def __init__(self, stanje):
        self.stanje = stanje
    
    def odrediStanje(self):
        return self.stanje

    def iskljuci(self):
        self.stanje = False

    def ukljuci(self):
        self.stanje = True

    def postaviZastituNad(self):
        if (CheckVar1.get() == 1 ):
            if (DalekovodnoPolje.odrediStanje() == True):
                DalekovodnoPolje.kojaSab()
            text.insert(INSERT,  "Uključujem Nadstrujnu Zaštitu...\n")
            self.ukljuci()
        else:
            text.insert(INSERT,  "Isključujem Nadstrujnu Zaštitu...\n")
            self.iskljuci()

    def postaviZastituDis(self):
        if (CheckVar2.get() == 1 ):
            if (DalekovodnoPolje.odrediStanje() == True):
                DalekovodnoPolje.kojaSab()
            text.insert(INSERT,  "Uključujem Distantnu Zaštitu...\n")
            self.ukljuci()
        else:
            text.insert(INSERT,  "Isključujem Distantnu Zaštitu...\n")
            self.iskljuci()      

class DistantnaZastita(Zastita):
    def __init__(self, stanje):
        Zastita.__init__(self, stanje)
        self.faza_L1_poticaj = False
        self.faza_L2_poticaj = False
        self.faza_L3_poticaj = False
        self.zemljospoj_poticaj = False
        self.drugi_stupanj_isključenje = False
        self.treci_stupanj_isključenje = False
        self.cetvrti_stupanj_isključenje = False
        self.uredaj_kvar = False
        self.TK_signal_iskljucenje = False

    def ispis_svih(self): 
        text.insert(INSERT, "DISTANTNA ZASTITA\n")
        text.insert(INSERT, "isključenje     prorada\n")
        text.insert(INSERT, "isključenje     prestanak\n")
        text.insert(INSERT, "faza L1 poticaj     prorada\n")
        text.insert(INSERT, "faza L1 poticaj     prestanak\n")
        text.insert(INSERT, "faza L2 poticaj     prorada\n")
        text.insert(INSERT, "faza L2 poticaj     prestanak\n")
        text.insert(INSERT, "faza L3 poticaj     prorada\n")
        text.insert(INSERT, "faza L3 poticaj     prestanak\n")
        text.insert(INSERT, "zemljospoj poticaj     prorada\n")
        text.insert(INSERT, "zemljospoj poticaj     prestanak\n")
        text.insert(INSERT, "2.stupanj - isključenje     prorada\n")
        text.insert(INSERT, "2.stupanj - isključenje     prestanak\n")
        text.insert(INSERT, "3.stupanj - isključenje     prorada\n")
        text.insert(INSERT, "3.stupanj - isključenje     prestanak\n")
        text.insert(INSERT, "4.stupanj - isključenje     prorada\n")
        text.insert(INSERT, "4.stupanj - isključenje     prestanak\n")
        text.insert(INSERT, "uređaj - kvar     prorada\n")
        text.insert(INSERT, "uređaj - kvar     prestanak\n\n\n")

    def ispis_grupnih(self): 
        text.insert(INSERT, "DISTANTNA ZASTITA\n")
        text.insert(INSERT, "isključenje     prorada\n")
        text.insert(INSERT, "isključenje     prestanak\n")
        text.insert(INSERT, "2.stupanj - isključenje     prorada\n")
        text.insert(INSERT, "2.stupanj - isključenje     prestanak\n")
        text.insert(INSERT, "3.stupanj - isključenje     prorada\n")
        text.insert(INSERT, "3.stupanj - isključenje     prestanak\n")
        text.insert(INSERT, "4.stupanj - isključenje     prorada\n")
        text.insert(INSERT, "4.stupanj - isključenje     prestanak\n")
        text.insert(INSERT, "TK signal - isključenje     prorada\n")
        text.insert(INSERT, "TK signal - isključenje     prestanak\n")



class NadstrujnaZastita(Zastita):
    def __init__(self, stanje):
        Zastita.__init__(self, stanje)
        self.NPČ_isključenje = False
        self.VPČ_isključenje = False
        self.zemljospojna_iskljucenje = False
        self.od_preopterećenja_upozorenje = False
        self.od_preopterećenja_iskljucenje = False
        self.relej_kvar = False


    def ispis_svih(self): 
        text.insert(INSERT, "NADSTRUJNA ZASTITA\n")
        text.insert(INSERT, "NPČ - isključenje     prorada\n")
        text.insert(INSERT, "NPČ - isključenje     prestanak\n")
        text.insert(INSERT, "VPČ isključenje     prorada\n")
        text.insert(INSERT, "VPČ isključenje     prestanak\n")
        text.insert(INSERT, "zemljospojna isključenje     prorada\n")
        text.insert(INSERT, "zemljospojna isključenje     prestanak\n")
        text.insert(INSERT, "od preopterećenja upozorenje     prorada\n")
        text.insert(INSERT, "od preopterećenja upozorenje     prestanak\n")
        text.insert(INSERT, "od preopterećenja isključenje     prorada\n")
        text.insert(INSERT, "od preopterećenja isključenje     prestanak\n")
        text.insert(INSERT, "relej - kvar     prorada\n")
        text.insert(INSERT, "relej - kvar     prestanak\n\n\n")



class APU:
    def __init__(self, stanje):
        self.stanje = stanje
        self.APU_1p = True
        self.APU_3p = True
        self.blokada = False

    def odrediStanje(self):
        return self.stanje

    def iskljuci(self):
        text.insert(INSERT,  "Isključujem APU...\n")
        self.stanje = False

    def ukljuci(self):
        text.insert(INSERT,  "Uključujem APU...\n")
        self.stanje = True


    def ispis_svih(self): 
        text.insert(INSERT, "APU\n")
        text.insert(INSERT, "APU uključenje     prorada\n")
        text.insert(INSERT, "APU uključenje     prestanak\n")
        text.insert(INSERT, "APU 1p     prorada\n")
        text.insert(INSERT, "APU 1p     prestanak\n")
        text.insert(INSERT, "APU 3p     prorada\n")
        text.insert(INSERT, "APU 3p     prestanak\n")
        text.insert(INSERT, "APU blokada     prorada\n")
        text.insert(INSERT, "APU blokada     prestanak\n\n\n")
        
class Polje:
    def __init__(self,naponski_nivo, naziv, stanje):
        self.stanje = stanje
        self.naziv = naziv
        self.naponski_nivo = naponski_nivo

    def odrediStanje(self):
        return self.stanje

    def iskljuci_iskljuci(self):
        pass



class SPPolje(Polje):
    def __init__(self, naponski_nivo, naziv, stanje, prekidac, rastavljacSab1, rastavljacSab2):
        Polje.__init__(self, naponski_nivo, naziv, stanje)
        self.prekidac = prekidac
        self.rastavljacSab1 = rastavljacSab1
        self.rastavljacSab2 = rastavljacSab2

    def ukljuci_iskljuci(self):
        if (Napajanje.napajanje == False):
            text.insert(INSERT,  "Upalite napajanje...\n")
            return
        if(self.prekidac.odrediStanje() == False and self.rastavljacSab1.odrediStanje() == False and self.rastavljacSab2.odrediStanje() == False):
            text.insert(INSERT,  "UKLJUČUJEM SPOJNO POLJE...\n")
            self.rastavljacSab1.ukljuci()
            self.rastavljacSab2.ukljuci()
            self.prekidac.ukljuci()
            self.stanje = True
            can.itemconfigure(s1_path2, fill = 'green')
            can.itemconfigure(s2_path2, fill = 'green')
            can.itemconfigure(s1_con2, fill = 'green')
            can.itemconfigure(s_rastavljac1, fill = 'green')
            can.itemconfigure(s_rastavljac2, fill = 'green')
            can.itemconfigure(s_prekidac, fill = 'green')
            text.insert(INSERT,  "SPOJNO POLJE UKLJUČENO...\n")
        else:
            text.insert(INSERT,  "ISKLJUČUJEM SPOJNO POLJE...\n")
            self.rastavljacSab1.iskljuci()
            self.rastavljacSab2.iskljuci()
            self.prekidac.iskljuci()
            self.stanje = False
            can.itemconfigure(s1_path2, fill = 'red')
            can.itemconfigure(s2_path2, fill = 'red')
            can.itemconfigure(s1_con2, fill = 'red')
            can.itemconfigure(s_rastavljac1, fill = 'black')
            can.itemconfigure(s_rastavljac2, fill = 'black')
            can.itemconfigure(s_prekidac, fill = 'black')
            text.insert(INSERT,  "SPOJNO POLJE ISKLJUČENO...\n")
            return

class DPPolje(Polje):
    def __init__(self, naponski_nivo, naziv, stanje, sabirnica, prekidac, rastavljacSab1, rastavljacSab2, rastavljacUzemljenja, rastavljacIzlazni, NadstrujnaZastita, DistantnaZastita, APU, Mjerenja):
        Polje.__init__(self, naponski_nivo, naziv, stanje)
        self.sabirnica = sabirnica
        self.prekidac = prekidac
        self.rastavljacSab1 = rastavljacSab1
        self.rastavljacSab2 = rastavljacSab2
        self.rastavljacUzemljenja = rastavljacUzemljenja
        self.rastavljacIzlazni = rastavljacIzlazni
        self.NadstrujnaZastita = NadstrujnaZastita
        self.DistantnaZastita = DistantnaZastita
        self.APU = APU
        self.Mjerenja = Mjerenja



    def ukljuci_iskljuciS1(self):
        if(self.prekidac.odrediStanje() == False and self.rastavljacSab1.odrediStanje() == False and self.rastavljacUzemljenja.odrediStanje() == True and self.rastavljacIzlazni.odrediStanje() == False):
            text.insert(INSERT,  "UKLJUČUJEM DALEKOVODNO POLJE...\n")
            self.rastavljacUzemljenja.iskljuci()
            self.rastavljacSab1.ukljuci()
            self.rastavljacIzlazni.ukljuci()
            self.APU.ukljuci()
            self.prekidac.ukljuci()
            self.Mjerenja.ukljuci()
            self.stanje = True
            can.itemconfigure(s1_path, fill = 'green')
            can.itemconfigure(s1_con, fill = 'green')
            can.itemconfigure(d_rastavljac1, fill = 'green')
            can.itemconfigure(d_prekidac, fill = 'green')
            can.itemconfigure(d_uzemljenje, fill = 'black')
            can.itemconfigure(d_izlazni, fill = 'green')
            can.itemconfigure(main_path, fill = 'green')
            can.itemconfigure(path, fill = 'red')
            can.itemconfigure(box1, fill = 'red')
            can.itemconfigure(box2, fill = 'red')
            can.itemconfigure(box3, fill = 'red')
            text.insert(INSERT,  "DALEKOVODNO POLJE UKLJUČENO...\n")
        else:
            text.insert(INSERT,  "ISKLJUČUJEM DALEKOVODNO POLJE...\n")
            self.APU.iskljuci()
            self.prekidac.iskljuci()
            self.rastavljacSab1.iskljuci()
            self.rastavljacIzlazni.iskljuci()
            self.rastavljacUzemljenja.ukljuci()
            self.Mjerenja.iskljuci()
            self.stanje = False
            can.itemconfigure(s1_path, fill = 'red')
            can.itemconfigure(s1_con, fill = 'red')
            can.itemconfigure(d_rastavljac1, fill = 'black')
            can.itemconfigure(d_prekidac, fill = 'black')
            can.itemconfigure(d_uzemljenje, fill = 'green')
            can.itemconfigure(d_izlazni, fill = 'black')
            can.itemconfigure(main_path, fill = 'red')
            can.itemconfigure(path, fill = 'green')
            can.itemconfigure(box1, fill = 'green')
            can.itemconfigure(box2, fill = 'green')
            can.itemconfigure(box3, fill = 'green')
            text.insert(INSERT,  "DALEKOVODNO POLJE ISKLJUČENO...\n")
        return
    def ukljuci_iskljuciS2(self):
        if(self.prekidac.odrediStanje() == False and self.rastavljacSab2.odrediStanje() == False and self.rastavljacUzemljenja.odrediStanje() == True and self.rastavljacIzlazni.odrediStanje() == False):
            text.insert(INSERT,  "UKLJUČUJEM DALEKOVODNO POLJE...\n")
            self.rastavljacUzemljenja.iskljuci()
            self.rastavljacSab2.ukljuci()
            self.rastavljacIzlazni.ukljuci()
            self.APU.ukljuci()
            self.prekidac.ukljuci()
            self.Mjerenja.ukljuci()
            self.stanje = True
            can.itemconfigure(s2_path, fill = 'green')
            can.itemconfigure(d_rastavljac2, fill = 'green')
            can.itemconfigure(d_prekidac, fill = 'green')
            can.itemconfigure(d_uzemljenje, fill = 'black')
            can.itemconfigure(d_izlazni, fill = 'green')
            can.itemconfigure(main_path, fill = 'green')
            can.itemconfigure(path, fill = 'red')
            can.itemconfigure(box1, fill = 'red')
            can.itemconfigure(box2, fill = 'red')
            can.itemconfigure(box3, fill = 'red')
            text.insert(INSERT,  "DALEKOVODNO POLJE UKLJUČENO...\n")
        else:
            text.insert(INSERT,  "ISKLJUČUJEM DALEKOVODNO POLJE...\n")
            self.APU.iskljuci()
            self.prekidac.iskljuci()
            self.rastavljacSab2.iskljuci()
            self.rastavljacIzlazni.iskljuci()
            self.rastavljacUzemljenja.ukljuci()
            self.Mjerenja.iskljuci()
            self.stanje = False
            can.itemconfigure(s2_path, fill = 'red')
            can.itemconfigure(d_rastavljac2, fill = 'black')
            can.itemconfigure(d_prekidac, fill = 'black')
            can.itemconfigure(d_uzemljenje, fill = 'green')
            can.itemconfigure(d_izlazni, fill = 'black')
            can.itemconfigure(main_path, fill = 'red')
            can.itemconfigure(path, fill = 'green')
            can.itemconfigure(box1, fill = 'green')
            can.itemconfigure(box2, fill = 'green')
            can.itemconfigure(box3, fill = 'green')
            text.insert(INSERT,  "DALEKOVODNO POLJE ISKLJUČENO...\n")
        return
    def kojaSab(self):
        unos1.delete(1.0,END)
        unos2.delete(1.0,END)
        unos3.delete(1.0,END)
        if (Napajanje.napajanje == False):
            text.insert(INSERT,  "Upalite napajanje...\n")
            return
        if (DalekovodnoPolje.DistantnaZastita.odrediStanje() == True):
            text.insert(INSERT,  "Nemoguće upravljati uređajem dok radi distantna zaštita\n")
            return
        if (DalekovodnoPolje.NadstrujnaZastita.odrediStanje() == True):
            text.insert(INSERT,  "Nemoguće upravljati uređajem dok radi nadstrujna zaštita\n")
            return
        if(self.sabirnica == 'S1'):
            self.ukljuci_iskljuciS1()
        else:
            self.ukljuci_iskljuciS2()


    def prebaci(self):
       
        if (Napajanje.napajanje == False):
            text.insert(INSERT,  "Upalite napajanje...\n")
            return
        if (self.odrediStanje() == False):
            text.insert(INSERT, "Upalite dalekovodno polje...\n")
            return
        if (SpojnoPolje.odrediStanje() == False):
            text.insert(INSERT,  "Upalite spojno polje...\n")
            return
        if (self.sabirnica == 'S1'):
            text.insert(INSERT, "PREBACUJEM DALEKOVODNO POLJE NA S2...\n")
            self.ukljuci_iskljuciS1()
            unos1.delete(1.0,END)
            unos2.delete(1.0,END)
            unos3.delete(1.0,END)
            self.ukljuci_iskljuciS2()
            self.sabirnica = 'S2'
            text.insert(INSERT, "DALEKOVODNO POLJE PREBAČENO NA S2...\n")
        else:
            text.insert(INSERT, "PREBACUJEM DALEKOVODNO POLJE NA S1...\n")
            self.ukljuci_iskljuciS2()      
            unos1.delete(1.0,END)
            unos2.delete(1.0,END)
            unos3.delete(1.0,END)
            self.ukljuci_iskljuciS1()
            self.sabirnica = 'S1'
            text.insert(INSERT, "DALEKOVODNO POLJE PREBAČENO NA S1...\n")


class Napajanje() :
    def __init__(self):
        self.napajanje = True

    def ukljuci_napajanje(self):
        self.napajanje = True
    def iskljuci_napajanje(self):
        self.napajanje = False

    def postaviNapajanje(self):
        if (CheckVar3.get() == 0):
            self.ukljuci_napajanje()
            text.insert(INSERT,  "Uključujem napajanje...\n")
        else:
            if (DalekovodnoPolje.odrediStanje() == True):
                DalekovodnoPolje.kojaSab()
            if (SpojnoPolje.odrediStanje() == True):
                SpojnoPolje.ukljuci_iskljuci()
            self.iskljuci_napajanje()
            text.insert(INSERT,  "Isključujem napajanje...\n")


def clearTerm():
    text.delete(1.0, END)



def ispisListe():
    input = commandline.get()
    commandline.delete(0, END)
    if (input == "sve"):
        text.insert(INSERT, "Lista signala za sve\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")        
        DalekovodnoPolje.prekidac.ispis_svih()
        DalekovodnoPolje.rastavljacSab1.ispis_svih()
        DalekovodnoPolje.rastavljacSab2.ispis_svih()
        DalekovodnoPolje.rastavljacIzlazni.ispis_svih()
        DalekovodnoPolje.rastavljacUzemljenja.ispis_svih()
        DalekovodnoPolje.DistantnaZastita.ispis_svih()
        DalekovodnoPolje.NadstrujnaZastita.ispis_svih()
        DalekovodnoPolje.APU.ispis_svih()
        DalekovodnoPolje.Mjerenja.ispis_svih()
        text.insert(INSERT, "SPOJNO POLJE\n")
        SpojnoPolje.prekidac.ispis_svih()
        SpojnoPolje.rastavljacSab1.ispis_svih()
        SpojnoPolje.rastavljacSab2.ispis_svih()
        
    elif (input == "dalekovodno - sve"):
        text.insert(INSERT, "Lista signala za dalekovodno polje\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")        
        DalekovodnoPolje.prekidac.ispis_svih()
        DalekovodnoPolje.rastavljacSab1.ispis_svih()
        DalekovodnoPolje.rastavljacSab2.ispis_svih()
        DalekovodnoPolje.rastavljacIzlazni.ispis_svih()
        DalekovodnoPolje.rastavljacUzemljenja.ispis_svih()
        DalekovodnoPolje.DistantnaZastita.ispis_svih()
        DalekovodnoPolje.NadstrujnaZastita.ispis_svih()
        DalekovodnoPolje.APU.ispis_svih()
        DalekovodnoPolje.Mjerenja.ispis_svih()
    elif (input == "spojno - sve"):
        text.insert(INSERT, "Lista signala za spojno polje\n\n\n")
        text.insert(INSERT, "SPOJNO POLJE\n")
        SpojnoPolje.prekidac.ispis_svih()
        SpojnoPolje.rastavljacSab1.ispis_svih()
        SpojnoPolje.rastavljacSab2.ispis_svih()
    elif (input == "trenutni"):
        text.insert(INSERT, "Lista trenutnih signala za sve\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")        
        DalekovodnoPolje.prekidac.ispis()
        DalekovodnoPolje.rastavljacSab1.ispis()
        DalekovodnoPolje.rastavljacSab2.ispis()
        text.insert(INSERT, "SPOJNO POLJE\n")
        SpojnoPolje.prekidac.ispis()
        SpojnoPolje.rastavljacSab1.ispis()
        SpojnoPolje.rastavljacSab2.ispis()
    elif (input == "dalekovodno - trenutni"):
        text.insert(INSERT, "Lista trenutnih signala za dalekovodno polje\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")        
        DalekovodnoPolje.prekidac.ispis()
        DalekovodnoPolje.rastavljacSab1.ispis()
        DalekovodnoPolje.rastavljacSab2.ispis()
    elif (input == "spojno - trenutni"):
        text.insert(INSERT, "Lista trenutnih signala za spojno polje\n\n\n")
        text.insert(INSERT, "SPOJNO POLJE\n")
        SpojnoPolje.prekidac.ispis()
        SpojnoPolje.rastavljacSab1.ispis()
        SpojnoPolje.rastavljacSab2.ispis()
    elif (input == "dalekovodno - prekidac - sve"):
        text.insert(INSERT, "Lista signala za prekidac dalekovodnog polja\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")        
        DalekovodnoPolje.prekidac.ispis_svih()
    elif (input == "dalekovodno - rastavljac - sve"):
        text.insert(INSERT, "Lista signala za rastavljac dalekovodnog polja\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")        
        DalekovodnoPolje.rastavljacSab1.ispis_svih()    
    elif (input == "dalekovodno - rastavljac1 - trenutni"):
        text.insert(INSERT, "Lista trenutnih signala za prvi rastavljac dalekovodnog polja\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")
        DalekovodnoPolje.rastavljacSab1.ispis()
    elif (input == "dalekovodno - rastavljac2 - trenutni"):
        text.insert(INSERT, "Lista trenutnih signala za drugi rastavljac dalekovodnog polja\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")        
        DalekovodnoPolje.rastavljacSab2.ispis() 
    elif (input == "dalekovodno - prekidac - trenutni"):
        text.insert(INSERT, "Lista trenutnih signala za prekidac dalekovodnog polja\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")        
        DalekovodnoPolje.prekidac.ispis()
    elif (input == "spojno - prekidac - sve"):
        text.insert(INSERT, "Lista signala za prekidac spojnog polja\n\n\n")
        text.insert(INSERT, "SPOJNO POLJE\n")        
        SpojnoPolje.prekidac.ispis_svih()
    elif (input == "spojno - rastavljac - sve"):
        text.insert(INSERT, "Lista signala za rastavljac spojno polja\n\n\n")
        text.insert(INSERT, "SPOJNO POLJE\n")        
        SpojnoPolje.rastavljacSab1.ispis_svih()    
    elif (input == "spojno - rastavljac1 - trenutni"):
        text.insert(INSERT, "Lista trenutnih signala za prvi rastavljac spojnog polja\n\n\n")
        text.insert(INSERT, "SPOJNO POLJE\n")        
        SpojnoPolje.rastavljacSab1.ispis()
    elif (input == "spojno - rastavljac2 - trenutni"):
        text.insert(INSERT, "Lista trenutnih signala za drugi rastavljac spojnog polja\n\n\n")
        text.insert(INSERT, "SPOJNO POLJE\n")        
        SpojnoPolje.rastavljacSab2.ispis() 
    elif (input == "spojno - prekidac - trenutni"):
        text.insert(INSERT, "Lista trenutnih signala za prekidac dalekovodnog polja\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")        
        SpojnoPolje.prekidac.ispis()
    elif (input == "grupni - sve"):
        text.insert(INSERT, "Lista svih grupnih signala za dalekovodnog polja\n\n\n")
        text.insert(INSERT, "DALEKOVODNO POLJE\n")        
        DalekovodnoPolje.DistantnaZastita.ispis_grupnih()
    elif (input == "help"):
        text.insert(INSERT, "Lista svig naredbi za terminal\n\n\n")
        text.insert(INSERT, "sve\n")
        text.insert(INSERT, "dalekovodno - sve\n")
        text.insert(INSERT, "spojno - sve\n")
        text.insert(INSERT, "trenutni\n")
        text.insert(INSERT, "dalekovodno - trenutni\n")
        text.insert(INSERT, "spojno - trenutni\n")
        text.insert(INSERT, "dalekovodno - prekidac - sve\n")
        text.insert(INSERT, "dalekovodno - rastavljac - sve\n")
        text.insert(INSERT, "dalekovodno - rastavljac1 - trenutni\n")
        text.insert(INSERT, "dalekovodno - rastavljac2 - trenutni\n")
        text.insert(INSERT, "dalekovodno - prekidac - trenutni\n")
        text.insert(INSERT, "spojno - prekidac - sve\n")
        text.insert(INSERT, "spojno - rastavljac - sve\n")
        text.insert(INSERT, "spojno - rastavljac1 - trenutni\n")
        text.insert(INSERT, "spojno - rastavljac2 - trenutni\n")
        text.insert(INSERT, "spojno - prekidac - trenutni\n")
        text.insert(INSERT, "grupni - sve\n")   
    else:
        text.insert(INSERT, "Kriva ključna riječ\n")
        text.insert(INSERT, "Upisite help za listu naredbi\n")
        
    
    
SpojnoPolje = SPPolje(110, "Spojno Polje", False, Prekidac(False), Rastavljac(False, "S1"), Rastavljac(False, "S2"))
DalekovodnoPolje = DPPolje(110, "Dalekovodno Polje", True, "S1",Prekidac(True), Rastavljac(True, "S1"), Rastavljac(False, "S2"), Rastavljac(False, "Uzemljenja"), Rastavljac(True, "Izlazni"), NadstrujnaZastita(False), DistantnaZastita(False), APU(False), Mjerenja())
Napajanje = Napajanje();
master = Tk()
master.title("Elektrana")
master.geometry("1800x900")
master.resizable(False, False)
can = Canvas(master, width = 1800, height = 900)

#Dalekovodno
sab1 = can.create_rectangle(20, 30, 1000, 50, fill='green')
sab2 = can.create_rectangle(20, 80, 1000, 100, fill='green')

s1_con_points = [100, 51, 100, 80, 120, 80, 120, 51]
s1_con = can.create_polygon(s1_con_points, fill = 'green')

s1_path_points = [100, 101, 100, 250, 250, 250, 250, 230, 120, 230, 120, 101]
s1_path = can.create_polygon(s1_path_points, fill = 'green')

s2_path_points = [420, 101, 420, 230, 271, 230, 271, 250, 440, 250, 440, 101]
s2_path = can.create_polygon(s2_path_points, fill = 'red')

d_rastavljac1 = can.create_rectangle(80, 150, 140, 170, fill = 'green')
d_rastavljac2 = can.create_rectangle(400, 150, 460, 170, fill = 'black')
d_izlazni = can.create_rectangle(230, 480, 290, 500, fill = 'green')
d_uzemljenje = can.create_rectangle(150, 560, 170, 620, fill = 'black')
d_prekidac = can.create_rectangle(230, 300, 290, 360, fill = 'green')

#Spojno

s_rastavljac1 = can.create_rectangle(580, 150, 640, 170, fill = 'black')
s_rastavljac2 = can.create_rectangle(900, 150, 960, 170, fill = 'black')
s_prekidac = can.create_rectangle(740, 210, 800, 270, fill = 'black')

s1_con_points2 = [600, 51, 600, 80, 620, 80, 620, 51]
s1_con2 = can.create_polygon(s1_con_points2, fill = 'red')

s1_path_points2 = [600, 101, 600, 250, 750, 250, 750, 230, 620, 230, 620, 101]
s1_path2 = can.create_polygon(s1_path_points2, fill = 'red')

s2_path_points2 = [920, 101, 940, 100, 940, 250, 790, 250, 790, 230, 920, 230]
s2_path2 = can.create_polygon(s2_path_points2, fill = 'red')

#izmedu
main_path = can.create_rectangle(250, 230, 270, 600, fill = 'green')

#uzemljenje
path = can.create_rectangle(100,580, 250, 600,fill = 'red')
box1 = can.create_rectangle(75, 540, 95, 640, fill = 'red')
box2 = can.create_rectangle(50, 560, 70, 620, fill = 'red')
box3 = can.create_rectangle(25, 570, 45, 610, fill = 'red')

can.pack()
#Labeli
sab1_label = Label(master, text="S1")
sab1_label.pack()
sab1_label.place(x = 10, y = 8)

sab2_label = Label(master, text="S2")
sab2_label.pack()
sab2_label.place(x = 10, y = 58)

dp_label = Label(master, text="Dalekovodno polje", font = 70)
dp_label.pack()
dp_label.place(x = 100, y = 700)

sp_label = Label(master, text="Spojno polje", font = 70)
sp_label.pack()
sp_label.place(x = 750, y = 700)

dp_rastavljacS1 = Label(master, text = "Rastavljac S1")
dp_rastavljacS1.pack()
dp_rastavljacS1.place(x = 150, y = 150)

dp_rastavljacS2 = Label(master, text = "Rastavljac S2")
dp_rastavljacS2.pack()
dp_rastavljacS2.place(x = 300, y = 150)


sp_rastavljacS1 = Label(master, text = "Rastavljac S1")
sp_rastavljacS1.pack()
sp_rastavljacS1.place(x = 650, y = 150)

sp_rastavljacS2 = Label(master, text = "Rastavljac S2")
sp_rastavljacS2.pack()
sp_rastavljacS2.place(x = 950, y = 150)


dp_rastavljacIzlazni = Label(master, text = "Izlazni rastavljac")
dp_rastavljacIzlazni.pack()
dp_rastavljacIzlazni.place(x = 300, y = 450)

dp_rastavljacUzemljenje = Label(master, text = "Rastavljac uzemljenja")
dp_rastavljacUzemljenje.pack()
dp_rastavljacUzemljenje.place(x = 200, y = 620)




#Kvacice i labeli
nadstrujna_label = Label(master, text = "Nadstrujna zastita")
nadstrujna_label.pack()
nadstrujna_label.place(x = 300, y = 780)

CheckVar1 = IntVar()
c1 = Checkbutton(master, text = "Prorada", variable = CheckVar1, onvalue = 1, offvalue = 0, height=1, width = 6, command = DalekovodnoPolje.NadstrujnaZastita.postaviZastituNad)
c1.pack()
c1.place(x = 300, y = 800)


distantna_label = Label(master, text = "Distantna zastita")
distantna_label.pack()
distantna_label.place(x = 450, y = 780)

CheckVar2 = IntVar()
c2 = Checkbutton(master, text = "Prorada", variable = CheckVar2, onvalue = 1, offvalue = 0, height=1, width = 6, command = DalekovodnoPolje.DistantnaZastita.postaviZastituDis)
c2.pack()
c2.place(x = 450, y = 800)


napajanje_label = Label(master, text = "Napajanje")
napajanje_label.pack()
napajanje_label.place(x = 600, y = 780)

CheckVar3 = IntVar()
c3 = Checkbutton(master, text = "On/OFF", variable = CheckVar3, onvalue = 0, offvalue = 1, height=1, width = 6, command = Napajanje.postaviNapajanje)
c3.pack()
c3.place(x = 600, y = 800)

#Mjerenja

prvomjerenje_label = Label(master, text = "Mjerenje")
prvomjerenje_label.pack()
prvomjerenje_label.place(x = 750, y = 780)

unos1 = Text(master, width = 11, height = 1)
unos1.insert(END, "10.5 kV")
unos1.pack()
unos1.place(x = 750, y = 800)


drugomjerenje_label = Label(master, text = "Mjerenje")
drugomjerenje_label.pack()
drugomjerenje_label.place(x = 850, y = 780)

unos2 = Text(master, width = 11, height = 1)
unos2.insert(END, "-5.0 MVAr")
unos2.pack()
unos2.place(x = 850, y = 800)

trecemjerenje_label = Label(master, text = "Mjerenje")
trecemjerenje_label.pack()
trecemjerenje_label.place(x = 950, y = 780)

unos3 = Text(master, width = 11, height = 1)
unos3.insert(END, "2500.0 kWh")
unos3.pack()
unos3.place(x = 950, y = 800)

#Prekidac
dpprekidac_label = Label(master, text = "Prekidac")
dpprekidac_label.pack()
dpprekidac_label.place(x = 320, y = 300)

spprekidac_label = Label(master, text = "Prekidac")
spprekidac_label.pack()
spprekidac_label.place(x = 750, y = 300)

#Gumbici

dal_gumb = Button(master, text = "On/Off", command = DalekovodnoPolje.kojaSab, width = 10)
dal_gumb.pack()
dal_gumb.place(x = 300, y = 700)
prebaci_gumb = Button(master, text = "Prebaci", command = DalekovodnoPolje.prebaci,width = 10)
prebaci_gumb.pack()
prebaci_gumb.place(x = 450, y = 700)

sp_gumb = Button(master, text = "On/Off", command = SpojnoPolje.ukljuci_iskljuci,width = 10)
sp_gumb.pack()
sp_gumb.place(x = 900, y = 700)


clear = Button(master, text = "Očisti terminal", command = clearTerm, width = 10)
clear.pack()
clear.place(x = 1100, y = 810)
#Terminal
text = Text(master, width = 85, height = 45, bg = 'gray')
text.pack()
text.place(x = 1100, y = 0)

commandline = Entry(master, width = 75, bg = 'gray')
commandline.pack()
commandline.place(x = 1100, y = 780)

command_gumb = Button(master, text = "Enter", width = 6, command = ispisListe)
command_gumb.pack()
command_gumb.place(x = 1715, y = 775)

sp_gumb = Button(master, text = "On/Off", command = SpojnoPolje.ukljuci_iskljuci,width = 10)
sp_gumb.pack()
sp_gumb.place(x = 900, y = 700)

master.mainloop()



