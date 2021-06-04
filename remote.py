#!/usr/bin/env python3
import subprocess
import time


subprocess.Popen("sudo systemctl enable pigpiod", shell=True)
subprocess.Popen("sudo systemctl enable pigpiod",shell=True)

time.sleep(2)

import piir


remote = piir.Remote('light.json',17)


remote.send('on')
remote.send_data('83 55 90 6F')
remote.send_data('83 55 90 6F')
time.sleep(3)

