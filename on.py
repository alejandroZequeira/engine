from temp import Timer
import threading
class on:
    t=Timer
    global fin
    fin=True
    def __init__(self):
        pass
    def timeInOn():
        global fin
        cont=0
        while(fin):
            cont+=1
            print("pido paquete",cont)
        cont=0

    def isOn(ton):
        global fin
        fin=t.istime(t,ton)
