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
me.enable_mission_pads()
time.sleep(drone_pauses)

mission_status =me.get_mission_pad_id()
print(me.get_mission_pad_id())
time.sleep(drone_pauses)

# while mission_status < 8:
#     time.sleep(drone_pauses)
#     if (mission_status==1)
#         print()
