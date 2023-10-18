import time 

class Timer:
    global t
    t=0
    def __init__(self):
        self.t=0
    
    def timeNow():
        global t
        return t    
    
    def istime(ts):
        global t
        sigue=True
        tsim=ts*1000
        start_time=time.time()
        while sigue:
            elapsed_time = time.time() - start_time
            milisegundos = int(elapsed_time * 1000)
            if tsim>milisegundos:
                t=milisegundos
            else:
                sigue=False
            time.sleep(0.001)
        print("termino el tiempo")
        return False