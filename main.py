import random
import threading
from temp import Timer
import time 
t =Timer

global stop
global statsTime,statsPkt
statsTime=[]
statsPkt=[]
stop=True

def pktGenerator():
    pktSize=random.randint(1,20)
    return pktSize

def on(tOn,t):
    tActual= t.timeNow(t)
    print("ento en on")
    while tActual<tOn:
        print("pedir paquete")
        tActual= t.timeNow(t)
        print("tiempo actual",tActual)

def simulacion():
    global stop
    conton=0 
    tSimulacion=30
    contoff=0
    ton=random.randint(1,3)
    toff=random.randint(1,3)
    state=random.randint(0,2)
    if(state==1):
        on(ton+t.timeNow(t),t)
        conton+=1
    else:
        print("entro en off")
        contoff+=1
        time.sleep(toff)
    tOn=ton+t.timeNow(t)
    tOff=toff+t.timeNow(t)   
    while stop:
        if(state==1):
            if tOff<tSimulacion:
                time.sleep(toff)
                print("duro en off: ",toff)
                contoff+=1
            if tOn<tSimulacion:
                on(ton+t.timeNow(t),t)
                print("duro en on: ",ton)
                conton+=1
        else:
            if tOff<tSimulacion:
                time.sleep(toff)
                print("duro en off: ",toff)
                contoff+=1
            if tOn<tSimulacion:
                on(ton+t.timeNow(t),t)
                print("duro en on: ",ton)
                conton+=1
        ton=random.randint(1,3)
        toff=random.randint(1,3)
        tOn=ton+t.timeNow(t)
        tOff=toff+tOn
        print("simulando")
    print("entro a on: ",conton)
    print("entro a off: ",contoff)
        
def service():
    global stop
    while(stop):
        print("procesando paquete")

if __name__== '__main__':
    thread = threading.Thread(target=simulacion)
    thread.start()
    thread2= threading.Thread(target=service)
    thread2.start()
    stop=t.istime(t ,30)