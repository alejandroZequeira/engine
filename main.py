import random
import threading
from temp import Timer
import on 
import time 
t =Timer
global stop
stop=True

def simulacion():
    global stop
    nodOn=on.on()
    conton=0 
    contoff=0
    ton=random.randint(1,3)
    toff=random.randint(1,3)
    state=random.randint(0,2)
    if(state==1):
        nodOn.isOn(ton)
        conton+=1
    else:
        print("entro en off")
        contoff+=1
        time.sleep(toff)
       
    while stop:
        if(state==1):
            time.sleep(toff)
            print("duro en off: ",toff)
            nodOn.isOn(ton)
            print("duro en on: ",ton)
            contoff+=1
            conton+=1
        else:
            nodOn.isOn(ton)
            print("duro en on: ",ton)
            time.sleep(toff)
            print("duro en off: ",toff)
            contoff+=1
            conton+=1
        ton=random.randint(1,3)
        toff=random.randint(1,3)
        print("simulando")
    print("entro a on: ",conton)
    print("entro a off: ",contoff)
        

if __name__== '__main__':
    thread = threading.Thread(target=simulacion)
    thread.start()
    stop=t.istime(t ,30)