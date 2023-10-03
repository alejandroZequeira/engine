from temp import Timer
import threading
t=Timer
stop=True

def timeInOn():
    while(stop):
        print("pido paquete")


def isOn():
    thread = threading.Thread(target=timeInOn)
    thread.start()
    stop=t.istime(t,2)
