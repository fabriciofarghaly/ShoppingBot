# ARuCo Tag Scanning Module

This module scanns ARuCo tags from the auxiliary camera mounted on the ShoppingBot and sends messages to the [WebServer](../WebServer/README.MD) to update the budget stored by that server.

Whenever a tag is recognized, there is a 3 second delay wherein no other tags will be scanned this is to ensure that items are not scanned multiple times per second and the budget stays correct. This delay can be changed in the constructor call on line 10: `_is = ItemScanner("10.20.94.117", remote_port="8080")` -> `_is = ItemScanner("10.20.94.117", remote_port="8080", scan_delay=<new_scan_delay>)`.

It is possible that this package will try to use the wrong camera when first run on the turtlebot. This is because of how different operating systems enumerate capture devices and present them to OpenCV, although it __should__ work on Ubuntu 16 and ROS Kinetic. The main symptom of this problem will be OpenCV trying to use the webcam on the turtlebot's netbook. If this is the case, a good place to start troubleshooting is by changeing line 25 of `item_scanner.py` from `self.feed = cv2.VideoCapture(1)` to `self.feed = cv2.VideoCapture(0)`. If this solution does not work, another workaround may just be to stop the script and rerun it with the original code, this may cause the OS to reenumerate the devices and present them in a different order to openCV.

NOTE: This module requires the opencv-contrib library, which is different from the standard opencv library. This can be installed by running `pip install opencv-contrib-python`

## Usage
1. Change the value of `ip_address` on line 9 to the ip address of the computer running the web server. This computer can either be the laptop on the turtlebot or it can be remote.
2. Run `python item_scanner.py`
 
