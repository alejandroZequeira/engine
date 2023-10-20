import random
import numpy as np
import threading
from temp import Timer
import time 
import matplotlib.pyplot as plt
import json
import os
#variable de tiempo de la  clase timer 
global t
t =Timer

global stop
#variables de control
global stats_time,stats_pkt,t_arribo,pkr_size_max,pkt_size_min, m_vEnlace
global time_simulacion,service_quee_size, quee_now, ocupacion_cola
pkt_size_max=20000 #bytes
pkt_size_min=10000 #bytes
time_simulacion=1 #min
t_arribo=20 #ms
m_vEnlace=5000 #kbyts/seg
service_quee_size=99999999*9999999999999999 #bits
stats_time=[]
stats_pkt=[]
quee_now=[]
ocupacion_cola=0
stop=True
#funcion generadora de numeros aleatorios
def dado(max,min):
    return random.randint(max,min)
#distribucion exponencial 
def dado_exp_cota(max,min,m):
    while True:
        time_exp=np.random.exponential(1/m,100)
        for s in time_exp:
            if (s>=min and s<=max):
                return s
def dado_exp(m):
    while True:
        time_exp=np.random.exponential(1/m,100)
       # print("antes del reacomodo",time_exp[0]*10)
        random.shuffle(time_exp)
        #print("despues del reacomodo",time_exp[0]*10)
        return (time_exp[0])
#generador de paquetes
def pktGenerator(max , min):
    pktSize=np.random.uniform(max,min,100)
    return int (pktSize[0])
#funcion on
def on(time_on):
    global pkt_size_max,pkt_size_min,stop,t,t_arribo
    #print("ento en on y durara hasta el segundo", time_on)
    while t.now_seg() < time_on:
        if (t.now_seg()+t_arribo/1000)<time_on:
            #print("genero paquete en el segundo: ",t.now_seg() )
            pktsize=pktGenerator(pkt_size_max,pkt_size_min)
            set_stats_pkt(t.now_seg() ,pktsize)
        #print("duerme en on")
        t.sleep_ms(t.now()+t_arribo)

#funciones para reuinir estadisticas
def set_stats_pkt(t_creacion,size):
    global stats_pkt
    stats_pkt.append({
        "id_pkt": len(stats_pkt),
        "tiempo_creacion":t_creacion,
        "service_waiting_time":0,
        "status":"",
        "tiempo_total":0,
        "size_kb":size
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
    state=dado(0,2) 
    while stop:
        if not stop:
            break
        time_on=dado_exp(3)
        time_off=dado_exp(3)
        #print("tiempo con distribucion exponencial ",time_on)
        if(state!=0):
            if (time_off/60+t.now_min())<time_simulacion:
                set_stats_time("off",t.now_seg() ,(t.now_seg()+time_off) )
                #print("valor de tiempo que debe durar en off (seg):",time_off )
                t.sleep_sg(t.now_seg()+time_off)
                #print("duro hasta el segundo en off: ",t.now_seg() )
                cont_time_off+=1    
            if (time_on/60+t.now_min())<time_simulacion:
                #print("tiempo en que inicia on en segundos",t.now_seg() )
                #print("valor de tiempo que debe durar en on (seg):",time_on )
                set_stats_time("on",t.now_seg() ,(t.now_seg()+time_on) )
                on(time_on+t.now_seg())
                #print("duro hasta el segundo en on: ",(t.now_seg()+time_on) )
                cont_time_on+=1
        else:
            if (time_on/60+t.now_min())<time_simulacion:
                set_stats_time("on",t.now_seg() ,(t.now_seg()+time_on) )
                on(time_on+t.now_seg())
                #print("duro en on: ",time_on )
                cont_time_on+=1

            if (time_off/60+t.now_min())<time_simulacion:
                set_stats_time("off",t.now_seg() ,(t.now_seg()+time_off) )
                t.sleep_sg(t.now_seg()+time_off)
                #print("duro en off: ",time_off )
                cont_time_off+=1
       # print("simulando...")
        #os.system ("cls") 	
    print("entro a on: ",cont_time_on)
    print("entro a off: ",cont_time_off)

#cola de servicio
def enviando():
    global  quee_now, ocupacion_cola,t
    id=0
    while(stop):
        if not stop:
            break
        if len(quee_now)>0:
            if quee_now[id]["size"]>0:
                print("indice del paquete: ",quee_now[id]["index"],"tamaño en bits: ",quee_now[id]["size"])
                quee_now[id]["size"]=quee_now[id]["size"]-(m_vEnlace*1000)
                print("tiempo actual en la cola",t.now_seg())

                t.sleep_sg(t.now_seg()+1)
            else:
                print("indice del paquete: ",quee_now[id]["index"],"tamaño en bits: ",quee_now[id]["size"])
                ocupacion_cola-=stats_pkt[quee_now[id]["index"]]["size_kb"]*8
                stats_pkt[quee_now[id]["index"]]["status"]="sent"
                stats_pkt[quee_now[id]["index"]]["tiempo_total"]=t.now_seg() 
                stats_pkt[quee_now[id]["index"]]["service_waiting_time"]=stats_pkt[quee_now[id]["index"]]["tiempo_total"]-stats_pkt[quee_now[id]["index"]]["tiempo_creacion"]
                quee_now.pop(id)

def service():
    global stop,service_quee_size,m_vEnlace,stats_pkt, ocupacion_cola
    cont=0
    thread = threading.Thread(target=enviando)
    thread.start()
    #print(stats_pkt)
    while(stop):
        if not stop:
            break
        if len(stats_pkt)>0:
            if ((stats_pkt[cont]["size_kb"]*8)+ocupacion_cola)<=service_quee_size:
                #print("entro a la condicion")
                if not any(objeto["index"] == cont for objeto in quee_now):
                    quee_now.append({"size":stats_pkt[cont]["size_kb"]*8,
                                     "index": cont})
                    ocupacion_cola+=stats_pkt[cont]["size_kb"]*8
            else:
                stats_pkt[cont]["status"]="lost"
            if cont<len(stats_pkt)-1:
                cont+=1
                print("contador de indices: ",cont)
#funcion cronometro 
def cronometro():
    global stop,time_simulacion
    stop=t.istime(time_simulacion)
#simulador
if __name__== '__main__':
    start=time.time()
    thread = threading.Thread(target=cronometro)
    thread.start()
    thread2= threading.Thread(target=service)
    thread2.start()
    trafic_generator()
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
    pktx=[]
    pkty=[]
    pkt_creados=0
    for p in stats_pkt:
       if p['status'] !="":
            print(p)
            pktx.append(p['tiempo_creacion'])
            pkty.append(p['service_waiting_time'])
            pkt_creados=p["id_pkt"]+1

    fig=plt.figure()
   # fig.subplots_adjust(hspace=1, wspace=1)
    ax=fig.add_subplot(1,2,1)
    ax.plot(argx, argy)
    ax.set_xlabel('tiempo (seg)')
    ax.set_ylabel('encendido')
    ax.set_title('grafica de los tiempos entre estados(On/Off)')
    ax2=fig.add_subplot(1,2,2)
    ax2.scatter(pktx, pkty)
    ax2.set_xlabel('tiempo (seg)')
    ax2.set_ylabel('tiempo de espera (seg)')
    ax2.set_title('grafica del tiempo de espera en la cola')
    plt.tight_layout()
    print("paquetes generados: ",pkt_creados)
    print("la simulacion duro: ",time.time()-start)
    plt.show() 