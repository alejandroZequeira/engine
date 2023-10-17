import random
import threading
from temp import Timer
import time 
global t
t =Timer

global stop
global statsTime,statsPkt
statsTime=[]
statsPkt=[]
stop=True
def dado(max,min):
    return random.randint(max,min)
def pktGenerator(max , min):
    pktSize=random.randint(min,max)
    return pktSize

def on(tOn,t):
    tActual= t.timeNow()
    print("ento en on")
    while tActual<tOn:
        print("pedir paquete")
        tActual= t.timeNow()
        print("tiempo actual",tActual)

def set_stats_time(etq,t_incial,t_final):
    global statsTime
    statsTime.append({
            "tiempo_inicial": t_incial,
            "tiempo_final":t_final,
            "etiqueta":etq
        })

def simulacion():
    global stop,t
    conton=0 
    tSimulacion=10
    contoff=0
    ton=dado(1,3)*1000
    toff=dado(1,3)
    state=dado(0,2)
    if(state==1):
        on(ton+t.timeNow(),t)
        set_stats_time("on",t.timeNow()/1000,(t.timeNow()/1000)+ton/1000)
        conton+=1
    else:
        print("entro en off")
        contoff+=1
        time.sleep(toff)
        set_stats_time("on",t.timeNow()/1000,(t.timeNow()/1000)+toff)
    tOn=ton+(t.timeNow()/1000)
    tOff=toff+t.timeNow()/1000   
    while stop:
        if(state==1):
            if tOff<tSimulacion:
                time.sleep(toff)
                print("duro en off: ",toff)
                contoff+=1
                set_stats_time("off",tOn,tOff)
            if tOn<tSimulacion:
                on(ton+t.timeNow(),t)
                print("duro en on: ",ton)
                set_stats_time("on",tOff,tOn)
                conton+=1
        else:
            if tOff<tSimulacion:
                time.sleep(toff)
                print("duro en off: ",toff)
                set_stats_time("off",tOn,tOff)
                contoff+=1
            if tOn<tSimulacion:
                on(ton+t.timeNow(),t)
                set_stats_time("on",tOff,tOn)
                print("duro en on: ",ton)
                conton+=1
        ton=dado(1,3)*1000
        toff=dado(1,3)
        tOn=(ton+t.timeNow())/1000
        tOff=toff+tOn
       # print("simulando")
    print("entro a on: ",conton)
    print("entro a off: ",contoff)
        
def service():
    global stop
    cont=0
    while(stop):
        #print("procesando paquete")
        cont+=1

if __name__== '__main__':
    thread = threading.Thread(target=simulacion)
    thread.start()
    #thread2= threading.Thread(target=service)
    #thread2.start()
    stop=t.istime(10)
    print(statsTime)