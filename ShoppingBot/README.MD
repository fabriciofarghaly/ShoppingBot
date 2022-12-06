# ShoppingBot

This is a basic iOS app for tracking the total cost of items scanned by a ShoppingBot. This app allows a user to input a budget and see the remaining available budget after items are scanned. The user can also remove the last scanned item, as well as clear the budget to reset its state.

NOTE: This app requires Xcode running on a Mac computer to compile.

## Usage
1. In Xcode open ItemServerAPI.swift.
2. Change the signing team and bundle identifier.
    1. Click on the top level directory Named "ShoppingBot" with the app store icon next to it. 
    2. Click on "Signing & Capabilities"
    3. Change the team to your Apple Developer account and the bundle identifier to something that reflects your account (i.e. testperson.ShoppingBot)
3. Change the placeholder in the line `private static let baseURLString = "http://<#T##IP_Address#>:8080"` to the ip address of the computer running the web server. 
    1. To get this ip address you can run the web server according to the usage instructions listed in the web server README.
4. Press the play button in the top left corner to build and run the app on a simulated iOS device. The app can also be run on a physical device by plugging it into the computer and selecting the device as the project's build target.

