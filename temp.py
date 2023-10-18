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
        tsim=ts
        for i in range(1,tsim):
            t=i*1000
            time.sleep(1)
            #print(i)
        return False