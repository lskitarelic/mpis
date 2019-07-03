#!/usr/bin/python
#23534950
from tkinter import *
import tkinter


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


    def odrediStanje(self):
        return self.stanje

    def iskljuci(self):
        self.stanje = "iskljucen"

    def ukljuci(self):
        self.stanje = "ukljucen"

class Rastavljac:
    def __init__(self, stanje):
        self.stanje = stanje

    def odrediStanje(self):
        return self.stanje

    def iskljuci(self):
        self.stanje = "iskljucen"

    def ukljuci(self):
        self.stanje = "ukljucen"

class Mjerenja:
    def __init__(self):
        self.radna_snaga = 0.0
        self.jalova_snaga = 0.0
        self.struja = 0.0
        self.frekvencija = 0.0
        self.radna_energija = 0.0
           
    def getRadna_snaga(self):
        return self.radna_snaga

    def getJalova_snaga(self):
        return self.jalova_snaga

    def getStruja(self):
        return self.struja

    def getFrekvencija(self):
        return self.frekvencija

    def getRadna_energija(self):
        return self.radna_energija
    
class Zastita():
    def __init__(self, stanje):
        self.stanje = stanje
    
    def odrediStanje(self):
        return self.stanje

    def iskljuci(self):
        self.stanje = "iskljucen"

    def ukljuci(self):
        self.stanje = "ukljucen"    

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

class NadstrujnaZastita(Zastita):
    def __init__(self, stanje):
        Zastita.__init__(self, stanje)
        self.NPČ_isključenje = False
        self.VPČ_isključenje = False
        self.zemljospojna_iskljucenje = False
        self.od_preopterećenja_upozorenje = False
        self.od_preopterećenja_iskljucenje = False
        self.relej_kvar = False

class APU:
    def __init__(self, stanje):
        self.stanje = stanje
        self.APU_1p = False
        self.APU_3p = False
        self.blokada = False

    def odrediStanje(self):
        return self.stanje

    def iskljuci(self):
        self.stanje = "iskljucen"

    def ukljuci(self):
        self.stanje = "ukljucen"    

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
        if(self.prekidac.odrediStanje() == 'iskljucen' and self.rastavljacSab1.odrediStanje() == 'iskljucen' and self.rastavljacSab2.odrediStanje() == 'iskljucen'):
            self.rastavljacSab1.ukljuci()
            self.rastavljacSab2.ukljuci()
            self.prekidac.ukljuci()
            self.stanje = 'ukljucen'
            can.itemconfigure(s1_path2, fill = 'green')
            can.itemconfigure(s2_path2, fill = 'green')
            can.itemconfigure(s1_con2, fill = 'green')
            can.itemconfigure(s_rastavljac1, fill = 'green')
            can.itemconfigure(s_rastavljac2, fill = 'green')
            can.itemconfigure(s_prekidac, fill = 'green')
        else:
            self.rastavljacSab1.iskljuci()
            self.rastavljacSab2.iskljuci()
            self.prekidac.iskljuci()
            self.stanje = 'iskljucen'
            can.itemconfigure(s1_path2, fill = 'red')
            can.itemconfigure(s2_path2, fill = 'red')
            can.itemconfigure(s1_con2, fill = 'red')
            can.itemconfigure(s_rastavljac1, fill = 'black')
            can.itemconfigure(s_rastavljac2, fill = 'black')
            can.itemconfigure(s_prekidac, fill = 'black')
            return

class DPPolje(Polje):
    def __init__(self, naponski_nivo, naziv, stanje, prekidac, rastavljacSab1, rastavljacSab2, rastavljacUzemljenja, rastavljacIzlazni, NadstrujnaZastita, DistantnaZastita, APU, Mjerenja):
        Polje.__init__(self, naponski_nivo, naziv, stanje)
        self.prekidac = prekidac
        self.rastavljacSab1 = rastavljacSab1
        self.rastavljacSab2 = rastavljacSab2
        self.rastavljacUzemljenja = rastavljacUzemljenja
        self.rastavljacIzlazni = rastavljacIzlazni
        self.NadstrujnaZastita = NadstrujnaZastita
        self.DistantnaZastita = DistantnaZastita
        self.APU = APU
        self.Mjerenja = Mjerenja

    def ukljuci_iskljuci(self):
        if(self.prekidac.odrediStanje() == 'iskljucen' and self.rastavljacSab1.odrediStanje() == 'iskljucen' and self.rastavljacSab2.odrediStanje() == 'iskljucen'):
            self.rastavljacUzemljenja.iskljuci()
            self.rastavljacSab1.ukljuci()
            self.rastavljacIzlazni.ukljuci()
            self.prekidac.ukljuci()
            self.stanje = 'ukljucen'
            can.itemconfigure(s1_path, fill = 'green')
            can.itemconfigure(s1_con, fill = 'green')
            can.itemconfigure(d_rastavljac1, fill = 'green')
            can.itemconfigure(d_prekidac, fill = 'green')
            can.itemconfigure(d_uzemljenje, fill = 'red')
            can.itemconfigure(d_izlazni, fill = 'green')
            can.itemconfigure(main_path, fill = 'green')
        else:
            self.prekidac.iskljuci()
            self.rastavljacSab1.iskljuci()
            self.rastavljacIzlazni.iskljuci()
            self.rastavljacUzemljenja.ukljuci()
            self.stanje = 'iskljucen'
            can.itemconfigure(s1_path, fill = 'red')
            can.itemconfigure(s1_con, fill = 'red')
            can.itemconfigure(d_rastavljac1, fill = 'black')
            can.itemconfigure(d_prekidac, fill = 'black')
            can.itemconfigure(d_uzemljenje, fill = 'green')
            can.itemconfigure(d_izlazni, fill = 'black')
            can.itemconfigure(main_path, fill = 'red')
            return
        
class Napajanje() :
    def __init__(self):
        self.snaga: 0.0
        self.napon: 0.0

    def ukljuci_napajanje(self, snaga, napon):
        self.snaga: snaga
        self.napon: napon

    def iskljuci_napajanje(self):
        self.snaga: 0.0
        self.napon: 0.0

SpojnoPolje = SPPolje(110, "Spojno Polje", "iskljucen", Prekidac("iskljucen"), Rastavljac("iskljucen"), Rastavljac("iskljucen"))
DalekovodnoPolje = DPPolje(110, "Dalekovodno Polje", "ukljucen", Prekidac("ukljucen"), Rastavljac("ukljucen"), Rastavljac("iskljucen"), Rastavljac("ukljucen"), Rastavljac("iskljucen"), NadstrujnaZastita("iskljucen"), DistantnaZastita("iskljucen"), APU("iskljucen"), Mjerenja())

master = Tk()
master.title("Karlo")
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
c1 = Checkbutton(master, text = "Prorada", variable = CheckVar1, onvalue = 1, offvalue = 0, height=1, width = 6)
c1.pack()
c1.place(x = 300, y = 800)


distantna_label = Label(master, text = "Distantna zastita")
distantna_label.pack()
distantna_label.place(x = 450, y = 780)

CheckVar2 = IntVar()
c2 = Checkbutton(master, text = "Prorada", variable = CheckVar2, onvalue = 1, offvalue = 0, height=1, width = 6)
c2.pack()
c2.place(x = 450, y = 800)


napajanje_label = Label(master, text = "Napajanje")
napajanje_label.pack()
napajanje_label.place(x = 600, y = 780)

CheckVar3 = IntVar()
c3 = Checkbutton(master, text = "Prorada", variable = CheckVar3, onvalue = 1, offvalue = 0, height=1, width = 6)
c3.pack()
c3.place(x = 600, y = 800)

#Mjerenja

prvomjerenje_label = Label(master, text = "Mjerenje")
prvomjerenje_label.pack()
prvomjerenje_label.place(x = 750, y = 780)

unos1 = Entry(master, width = 9)
unos1.pack()
unos1.place(x = 750, y = 800)


drugomjerenje_label = Label(master, text = "Mjerenje")
drugomjerenje_label.pack()
drugomjerenje_label.place(x = 850, y = 780)

unos2 = Entry(master, width = 9)
unos2.pack()
unos2.place(x = 850, y = 800)

trecemjerenje_label = Label(master, text = "Mjerenje")
trecemjerenje_label.pack()
trecemjerenje_label.place(x = 950, y = 780)

unos3 = Entry(master, width = 9)
unos3.pack()
unos3.place(x = 950, y = 800)

#Prekidac
dpprekidac_label = Label(master, text = "Prekidac")
dpprekidac_label.pack()
dpprekidac_label.place(x = 320, y = 300)

CheckVar4 = IntVar()
c4 = Checkbutton(master, text = "APU ukljucenje", variable = CheckVar4, onvalue = 1, offvalue = 0, height=1, width = 10)
c4.pack()
c4.place(x = 320, y = 320)


spprekidac_label = Label(master, text = "Prekidac")
spprekidac_label.pack()
spprekidac_label.place(x = 750, y = 300)

#Gumbici
kontrola_gumb = Button(master, text = "Lokalno upravljanje")
kontrola_gumb.pack()
kontrola_gumb.place(x = 100, y = 800)

dal_gumb = Button(master, text = "Iskljuci", command = DalekovodnoPolje.ukljuci_iskljuci, width = 10)
dal_gumb.pack()
dal_gumb.place(x = 300, y = 700)

prebaci_gumb = Button(master, text = "Prebaci", width = 10)
prebaci_gumb.pack()
prebaci_gumb.place(x = 450, y = 700)

sp_gumb = Button(master, text = "Iskljuci", command = SpojnoPolje.ukljuci_iskljuci,width = 10)
sp_gumb.pack()
sp_gumb.place(x = 900, y = 700)


#Terminal
text = Text(master, width = 85, height = 45, state = DISABLED, bg = 'gray')
text.pack()
text.place(x = 1100, y = 0)

commandline = Entry(master, width = 85, bg = 'gray')
commandline.pack()
commandline.place(x = 1100, y = 800)

master.mainloop()



