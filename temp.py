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
        tsim=ts*1000
        for i in range(1,tsim+1):
            time.sleep(1/1000)
            #print(i)
            t=i
        return False