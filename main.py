import random
import threading
from temp import Timer
t =Timer
stop=True
def simulacion(): 
    while stop:
        state=random.randint(0,2)
        if(state==1):
            print("entra en on")
        else:
            print("entro en off")


if __name__== '__main__':
    thread = threading.Thread(target=simulacion)
    thread.start()
    stop=t.istime(t ,10)