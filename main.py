import random
import threading
from temp import Timer
import on 
import off
import time
t =Timer
stop=True
def simulacion(): 
    while stop:
        state=random.randint(1,2)
        if(state==1):
            on.isOn()
            time.sleep(2)
        else:
            off.isOff()
            time.sleep(2)
    print("fin de la simulacion")


if __name__== '__main__':
    thread = threading.Thread(target=simulacion)
    thread.start()
    stop=t.istime(t ,10)