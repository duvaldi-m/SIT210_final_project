#!/usr/bin/env python3
import psutil
import time
import piir

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

check = True
while check:
	for i in range(10):
		check =checkIfProcessRunning('kodi')
		time.sleep(1)

print('now turn projector off')

remote = piir.Remote('light.json',17)
#remote.send('on')
remote.send_data('83 55 90 6F')
time.sleep(4)
remote.send_data('83 55 90 6F')


