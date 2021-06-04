from microbit import*
import radio 
import random


radio.on()
radio.config(channel=20)

#sender
myIp = 'SD'
recieverIp = 'RC' 

header = recieverIp + ':' + myIp + ':'
    

while True: 
    
    radio.send(header + 'blind_down')
    mReceived = radio.receive()
                            
    if mReceived:
        mReceived = mReceived.split(':')              
        if (str(mReceived[0]) == myIp and str(mReceived[1]) == recieverIp and str(mReceived[2])=='1'):
             while True:
                 radio.send(header + '1')
                 
                 
                 
                        
                        
                    
          



