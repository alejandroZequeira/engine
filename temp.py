import time 

class Timer:
    global ms,sg, mn,stop
    ms=0
    sg=0
    mn=0
    stop=False
    def __init__(self):
        self.ms=0
        self.sg=0
        self.mn=0
    def now_seg():
        global sg
        return sg
    
    def now_min():
        global mn
        return mn
    
    def now():
        global ms
        return ms    
    def sleep_ms(s):
        global ms
        while True:
            if stop:
                break
            if s<ms:
                break
        
    def sleep_sg(s):
        global sg
        while True:
            if stop:
                break
            if s<sg:
                break
    def istime(ts):
        global ms,sg,mn,stop
        sigue=True
        tsim=ts*60
        milisegundos=0
        #start_time=time.time()
        while sigue:
            #elapsed_time=time.time()-start_time
             #int (elapsed_time*1000)
            segundos=milisegundos/1000
            minutos=segundos/60
            if tsim>segundos:
                ms=milisegundos                
                sg=segundos
                mn=minutos
                #print("tiempo actual ", segundos)
            else:
                print("se acabo el tiempo")
                sigue=False
                stop=True
            #elapsed_time+=1
            time.sleep(0.000001)
            milisegundos +=1
        print("termino el tiempo")
        return False