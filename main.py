import random
import threading
from temp import Timer
import time 
import matplotlib.pyplot as plt
import json
global t
t =Timer

global stop
#variables de control
global stats_time,stats_pkt,cola,t_arribo,pkr_size_max,pkt_size_min, m_vEnlace,time_simulacion
pkt_size_max=20000
pkt_size_min=10000
time_simulacion=20
t_arribo=20
stats_time=[]
stats_pkt=[]
cola=[]
stop=True
#funcion generadora de numeros aleatorios
def dado(max,min):
    return random.randint(max,min)
#generador de paquetes
def pktGenerator(max , min):
    pktSize=random.randint(min,max)
    return pktSize
#funcion on
def on(time_on):
    global cola,pkt_size_max,pkt_size_min,stop,t
    tActual= t.timeNow()
    print("ento en on y durara hasta el segundo", time_on/1000)
    while tActual >0:
        if stop==False:
            break
        if (tActual+t_arribo)<time_on:
            pktsize=pktGenerator(pkt_size_max,pkt_size_min)
            cola.append(pktsize)
            set_stats_pkt(t.timeNow()/1000)
        time.sleep((t_arribo)/1000)
        tActual=time_on -t.timeNow()
        #print("tiempo actual",tActual/1000)

#funciones para reuinir estadisticas
def set_stats_pkt(t_creacion):
    global stats_pkt,cola
    stats_pkt.append({
        "id_pkt": len(cola)-1,
        "tiempo_creacion":t_creacion,
        "tiempo_espera_servicio":0,
        "status":"",
        "tiempo_total":0,
        "size_kb":cola[len(cola)-1]
    })

def set_stats_time(etq,t_incial,t_final):
    global stats_time
    stats_time.append({
            "tiempo_inicial": t_incial,
            "tiempo_final":t_final,
            "etq":etq
        })
#generador de trafico
def trafic_generator():
    global stop,t,time_simulacion
    cont_time_on=0 
    cont_time_off=0
    time_on=dado(1,3)
    time_off=dado(1,3)
    state=dado(0,2)  
    while stop:
        if(state!=1):
            if time_off<time_simulacion:
                set_stats_time("off",t.timeNow()/1000,(t.timeNow()/1000)+time_off)
                time.sleep(time_off)
                print("duro hasta el segundo en off: ",(t.timeNow()/1000)+time_off)
                cont_time_off+=1    
            if time_on<time_simulacion:
                set_stats_time("on",t.timeNow()/1000,(t.timeNow()/1000)+time_on)
                on((time_on*1000)+t.timeNow())
                print("duro hasta el segundo en on: ",(t.timeNow()/1000)+time_on)
                cont_time_on+=1
        else:
            if time_on<time_simulacion:
                set_stats_time("on",t.timeNow()/1000,(t.timeNow()/1000)+time_on)
                on((time_on*1000)+t.timeNow())
                print("duro en on: ",time_on)
                cont_time_on+=1

            if time_off<time_simulacion:
                set_stats_time("off",t.timeNow()/1000,(t.timeNow()/1000)+time_off)
                time.sleep(time_off)
                print("duro en off: ",time_off)
                cont_time_off+=1
        time_on=dado(1,3)
        time_off=dado(1,3)
       # print("simulando")
    print("entro a on: ",cont_time_on)
    print("entro a off: ",cont_time_off)

#cola de servicio
def service():
    global stop
    cont=0
    while(stop):
        #print("procesando paquete")
        cont+=1

#simulador
if __name__== '__main__':
    thread = threading.Thread(target=trafic_generator)
    thread.start()
    #thread2= threading.Thread(target=service)
    #thread2.start()
    stop=t.istime(time_simulacion)
    #print(stats_time)
    #print(stats_pkt)
    argx=[]
    argy=[]
    for s in stats_time:
        print(s)
        if s['etq'] =="on":
            argx.append( s['tiempo_inicial'])
            argy.append(10)
            argx.append( s['tiempo_final'])
            argy.append(10)
        else:
            argx.append( s['tiempo_inicial'])
            argy.append(0)
            argx.append( s['tiempo_final'])
            argy.append(0)
    plt.subplot().plot(argx,argy)
    plt.xlabel('tiempos')
    plt.ylabel("estado en on")
    plt.show()