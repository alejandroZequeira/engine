class Pkt:
    global pyload
    pyload=0
    def __init__(self):
        self.pyload

    def setPkt(pktZise):
        global pyload
        pyload=pktZise
    def getPkt():
        return pyload