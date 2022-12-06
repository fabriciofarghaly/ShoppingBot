#!/bin/env/python3
"""
This is a wrapper class for the cv2.VideoCapture class. It makes functions 
useful for item_scanner a little easier to access. It also incorporates
ARuCo tag scanning here so that the ItemScanner class can focus on
interpreting items and sending requests to the server.
"""

import cv2
import time
import numpy as np

def main():
    """
    main function for testing this class and the item scanning behavior.
    This function is unused in the final functionality.
    """

    feed = CameraFeed(1)

    while (True):
        frame = feed.get_frame()

        markers = feed.find_ar_tags(frame)

        print(markers[:2])

        tags = markers[0][:1]

        frame_o = frame
        if (len(tags) > 0):
            frame_o = cv2.aruco.drawDetectedMarkers(frame, tags)
           
        cv2.imshow("frame", frame_o)

        time.sleep(1.0)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    feed.destroy()

    cv2.destroyAllWindows()


class CameraFeed:

    def __init__(self, camera_id):
        """
        Initializer for the CameraFeed Object.

        :params camera_id: OpenCV accessible camera index. This is not a definite
        value and depends on how many camera devices are accessible to the computer
        """
        self.cap = cv2.VideoCapture(camera_id)

    def get_frame(self):
        """
        Gets a single frame from the capture object. 

        :returns: A single frame from the camera if it is available
        or None otherwise.
        """
        frame = self.cap.read()
        if (not frame[0]):
            return None

        return frame[1] 

    def get_frame_size(self):
        """
        Returns the size of the the frames captured by the VideoCapture
        object as a numpy shape.

        :returns: The size of the captured frame.
        """
        return self.cap.read().shape

    def destroy(self):
        """
        Releases the opencv pipe to the capture object. 
        """
        self.cap.release()

    def find_ar_tags(self, frame=None):
        """
        Finds (possibly multiple) ARuCo tags in the given frame. If 
        frame is None, this method uses the most recent frame.

        :param frame: captured frame to search for ARuCo tags.
        :returns: A tuple containing information on any tags found in the frame.
        """
        if frame is None:
            frame = self.get_frame()
        
        dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
         
        # Initialize the detector parameters using default values
        parameters = cv2.aruco.DetectorParameters_create()
          
        # Detect the markers in the image
        markers = cv2.aruco.detectMarkers(frame, dictionary, parameters=parameters)
        return markers

if __name__ == "__main__":
    main()
