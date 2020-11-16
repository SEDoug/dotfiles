from djitellopy import Tello
import time
from PIL import Image

######################################################################
patrol_width = 120  # WIDTH OF THE Patrol (normally set to 120 cm for 4 feet (121.92)
patrol_height = 180  # HEIGHT OF THE Patrol (normally set to 180 cm for 4 feet (182.88)
drone_width = 15  # Normally set to 15 cm (7 inches)
drone_pauses = 5 # number of seconds at each corner
######################################################################

# CONNECT
me = Tello()
time.sleep(drone_pauses)
me.connect()

time.sleep(drone_pauses)
me.takeoff()
time.sleep(drone_pauses)

print(me.get_battery())

me.move_forward(patrol_height-drone_width)
time.sleep(drone_pauses)
me.move_left(patrol_width-drone_width)
time.sleep(drone_pauses)
me.move_back(patrol_height-drone_width)
time.sleep(drone_pauses)
me.move_right(patrol_width-drone_width)
time.sleep(drone_pauses)
me.move_forward(patrol_height-drone_width)
time.sleep(drone_pauses)
me.move_left(patrol_width-drone_width)
time.sleep(drone_pauses)
me.move_back(patrol_height-drone_width)
time.sleep(drone_pauses)
me.move_right(patrol_width-drone_width)
time.sleep(drone_pauses)
me.move_forward(patrol_height-drone_width)
time.sleep(drone_pauses)
me.move_left(patrol_width-drone_width)
time.sleep(drone_pauses)
me.move_back(patrol_height-drone_width)
time.sleep(drone_pauses)
me.move_right(patrol_width-drone_width)
time.sleep(drone_pauses)

me.land()
