import time

class Timer:
    def __init__(self):
        self.t=0
        print("soy un objeto")
    def istime(self, t):
        while(t>0):
            time.sleep(1)
            t-=1
        return False