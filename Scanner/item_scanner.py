"""
ItemScanner scans items from a connected camera and send requests to a webserver to get price and update budget.
"""

import time
import numpy as np
import cv2
import requests
from camera_feed import CameraFeed


def main():
    """
    Main function for the item_scanner.
    """
    ip_address = "10.20.94.117" # Change this value to the correct IP
    _is = ItemScanner("10.20.94.117", remote_port="8080")

    _is.start(show_feed=True)



class ItemScanner:
    """
    An class to scan ar tags and report them to a remote server
    """

    def __init__(self, remote_ip, remote_port="5000", scan_delay=3.0):
        """
        Constructor for the ItemScanner class 

        :param remote_ip: The remote ip_address of the computer running the web server.
        :param remote_port: The port the remote webserver listening for requests on.
        :param scan_delay: The minimum delay between items will be scanned and processed. 
        """
        self.feed = CameraFeed(1)
        self.remote_addr = "http://" + remote_ip + ":" + str(remote_port)
        self.isScanning = False
        self.isRunning = False
        self.scanDelay = scan_delay
        self.hasMadeRequestForScan = False
        self.lastScanTime = None

    def start(self, show_feed=False):
        """
        Starts the scanning loop to scan and process items.

        :param show_feed: Unused in the current functionality. 
        """
        self.isRunning = True
        self.isScanning = True


        while (self.isRunning):
            frame = self.feed.get_frame()
            if (frame is None):
                print("Error accessing camera framem, quitting")
                return
            if (self.isScanning):

                markers = self.feed.find_ar_tags(frame)[:2]

                if (markers[1] == None):
                    # No markers found, don't do anything
                    continue

                id = markers[1][0][0] # Get first marker, assumes there is only 1 
                                   # valid ar tag in the frame
                self.lastScanTime = time.time()
                self.isScanning = False

                                if (self.hasMadeRequestForScan):
                                    continue

                self._make_request(id)
                                self.hasMadeRequestForScan = True
                                frame = None

            else:
                if (time.time() - self.lastScanTime > self.scanDelay):
                    self.isScanning = True
                                        self.hasMadeRequestForScan = False


    def _make_request(self, id):
        """
        Makes a request to the server to update the budget.

        :param id: id of the item in the server's database. 
        """
        url = self.remote_addr + "/update?item_id={0}".format(id)

        res = requests.post(url)

        print(res.json)




if __name__ == "__main__":
    main()
