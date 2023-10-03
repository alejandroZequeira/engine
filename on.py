from temp import Timer
import threading
t=Timer
global stop
stop=True
def timeInOn():
    while(stop):
        print("pido paquete")
    print("se acabo el tiempo en on")

def isOn():
    global stop
    thread = threading.Thread(target=timeInOn)
    thread.start()
    stop=t.istime(t,2)
