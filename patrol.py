from datetime import datetime
import time
from djitellopy import Tello
t1 = datetime.now() # initialize 'timer'
waitTime = 2 #seconds
patrolCommands = ["forward 50",
                  "ccw 90",
                  "forward 50",
                  "ccw 90",
                  "forward 50",
                  "ccw 90",
                  "forward 50",
                  "forward 50",
                  "ccw 90"]
i = 0
def resetTimer():
    t1 = datetime.now()
tello = Tello()
tello.connect()
tello.takeoff()
time.sleep(0.5)
while True:    
    t2 = datetime.now()
    delta = t2 - t1
    #print(delta.seconds)
    if delta.seconds > waitTime:
        for retry in range(3):
            ret = tello.send_command_with_return(patrolCommands[i])
            print("{}: {}".format(ret, patrolCommands[i]))
            if ret == "ok":
                break
            else:
                print("retry")
            if retry == 3:
                tello.land()
        i = i+1
        t1 = datetime.now()
    if i >= len(patrolCommands):
        break
tello.land()
