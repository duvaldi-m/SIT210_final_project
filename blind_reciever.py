from microbit import*
import radio 

radio.on()
radio.config(channel=20)
myIp = 'RC'

while True: 
   
    if button_a.was_pressed():
        display.clear()
        display.show(Image.ARROW_N)
        blinds_down = False
    try:    
        mreceived = radio.receive()
    except Exception:
        radio.off()
        radio.on()
        continue

    if mreceived and mreceived.startswith(myIp):
        secondIpPos = 1
        mreceived = mreceived.split(':')
        senderIp = mreceived[secondIpPos]
        #header = TO IP : FROM IP
        header = senderIp + ':' + myIp + ':'
    
        if mreceived[2] == 'blind_down':
            display.show(Image.ARROW_S)
            radio.send(header + '1')
        
        if mreceived[2] == '1':
            blinds_down = True
        
    if not mreceived:
        display.clear()
        display.show(Image.ARROW_N)
        blinds_down = False 
                    
                    
                    