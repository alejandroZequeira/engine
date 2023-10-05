import pkt
class stats:
    class timesOnOff:
        t_initial=0
        t_final=0
        tipo=""
        def __init__(self,tI,tF,tip):
            self.t_initial=tI
            self.t_final=tF
            self.tipo=tip
    class pktStats:
        paquete=pkt.Pkt
