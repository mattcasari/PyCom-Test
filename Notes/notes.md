# Notes from installation

Date: 10/24/2018
Author: Matt Casari

I followed the instructions provided by PyCom to load new firmware on the 

https://docs.pycom.io/

## Loading Firmware on Expansion Board v3.0

Using the instructions found here:
https://docs.pycom.io/pytrackpysense/installation/firmware

I found the notes for Windows to be missing a few key pieces of information.  My first attempt resulted in me spending nearly 2 hours spinning wheels, and no closer to the solution.  On my second attempt, I figured a couple of key pieces out.

1. When the instruction say to "Press the button", that means button "S1", **NOT** "Safe Boot".
1. Quick quick quick!  When it loads in DFU mode, you have 7 seconds to get things started.
1. 


## Connecting to the WiPy over WiFi
Once I reflashed the Expansion Board v3.0, I disconnected the USB and installed the WiPy into the board.  I reinserted the USB and followed the instructions to connect ot the WiPy over WiFi.  

Device Name: wipy-wlan-xxxx
Password: www.wipy.io

Received the message: Can't connect to this network

## Pymakr on Visual Studio Code

Plugin instruction are here:
https://docs.pycom.io/pymakr/installation/vscode

I'm using Visual Studio Code for development and the Pymakr plugin.  It tells you in the plugin instructions, but make sure to install NodeJS before starting VSCode, otherwise you'll get infinite errors.


## Connecting with Pymakr

Once I had VSCode up and running, I had to change the **address** field in the pymakr.json file to the address of my device.  

First, from the command pallet (Ctrl-Shift-P) run
```
Pymakr > Extra's > List Serial Port
```

Figure out which is the WiPy (Mine was identified with the Microchip tag which is a USB chip).  Copy that COM port (COM6)

Next, open the pymakr.json file by going back into the command pallet and running:
```
Pymakr > Global Settings
```

Change the **address** field:

Was: **"address": "192.168.4.1"**<br>
Now: **"address": "COM6"**
