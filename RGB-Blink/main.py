import pycom
import time

pycom.heartbeat(False)


while True:
    pycom.rgbled(0xFF0000)
    time.sleep(1)
    pycom.rgbled(0x00FF00)
    time.sleep(1)
    pycom.rgbled(0x0000FF)
    time.sleep(1)

# while True:
#     t = 0
#     color = 0xf0
#     for i in range(0,15):
#         for j in range(0,15):
#             t = color + j
#             # t = t + j
#         # print(hex(t))
#             pycom.rgbled(t)

#             time.sleep(0.001)