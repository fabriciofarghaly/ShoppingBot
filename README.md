# ShoppingBot Installation Instructions

The sections below should be followed in order.

## Installing [robust_people_follower](https://github.com/sijanz/robust_people_follower)
* Follow instructions described in this github's README.md
* Note: your have to be __very__ specific and make sure everything installs properly
* This package can be run with the command `roslaunch robust_people_follower robust_people_follower.launch`

## Starting the WebServer
* This web server is necessary for the ShoppingBot to talk to the iOS App.
* This has only been tested running on a different computer, remote to the ShoppingBot, but it should also work running on the ShoppingBot's laptop. 
* To start the web server follow the usage instructions in the [/WebServer/README.md](WebServer/README.md)

## Starting the ItemScanner
* This program uses the auxiliary camera on the ShoppingBot to scan ARuCo Tags and send information to the WebServer.
* It is possible on different operating systems that this code will not use the correct camera by default. This is because of how different operating systems enumerate the capture devices connected to them and present them to openCV.
    * If this is the case a good place to start troubleshooting this is by changing line 25 of `item_scanner.py` from `self.feed = cv2.VideoCapture(0)` to `self.feed = cv2.VideoCapture(1)`.
* To start the ItemScanner, follow the usage instructions in [/Scanner/README.md](Scanner/README.md)

## ShoppingBot iOS App
* Using this part requires a Mac running Xcode
    * Xcode can be installed from [this link](https://apps.apple.com/us/app/xcode/id497799835?mt=12)
* To configure and run the app follow the usage instructions in the [/ShoppingBot/README.md](ShoppingBot/README.md)

## Turtlebot Bringup and running robust_people_follower
* On either the laptop on the turtlebot, a laptop SSHed into the turtlebot, or a laptop connected to the turtlebot through ROS's networking configuration:
    1. First, run `roslaunch turtlebot_bringup minimal.launch`
    2. Next, in a new terminal window, run `roslaunch robust_people_follower robust_people_follower.launch`
        * Optionally, this command can be substituted for `roslaunch turtlebot_follower follower.launch` for a simpler following algorithm that may not work as well, but will work if the install for [robust_people_follower](https://github.com/sijanz/robust_people_followers) failed.

