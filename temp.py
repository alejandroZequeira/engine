import time

class Timer:
    def __init__(self):
        self.t=0
    def timeNow(self):
        return self.t    
    def istime(self, t):
        while(t>0):
            time.sleep(1)
            t-=1
        print("acabo el tiempo")
        return False