# ARuCo Tag Scanning Module

This module scanns ARuCo tags from the auxiliary camera mounted on the ShoppingBot and sends messages to the [WebServer](../WebServer/README.MD) to update the budget stored by that server.

Whenever a tag is recognized, there is a 3 second delay wherein no other tags will be scanned this is to ensure that items are not scanned multiple times per second and the budget stays correct. This delay can be changed in the constructor call on line 10: `_is = ItemScanner("10.20.94.117", remote_port="8080")` -> `_is = ItemScanner("10.20.94.117", remote_port="8080", scan_delay=<new_scan_delay>)`.

NOTE: This module requires the opencv-contrib library, which is different from the standard opencv library. This can be installed by running `pip install opencv-contrib-python`

## Usage
1. Change the value of `ip_address` on line 9 to the ip address of the computer running the web server. This computer can either be the laptop on the turtlebot or it can be remote.
2. Run `python item_scanner.py`
 
