# import the necessary package
from __future__ import print_function
import cv2
import imutils
import argparse
from webcamcamera import FPS, WebcamVideoStream

if __name__ == "__main__":
    # grab a pointer to the video stream and initialize the FPS counter
    print ("[INFO] sampling frames from webcam")
    stream = WebcamVideoStream().start()
    fps = FPS().start()

    # loop over some frames
    while True:
        # grab the frame from the stream and resize it to have a maximum 
        # width of 400 pixels
        frame = stream.read()
        frame = imutils.resize(frame, width=400)
        # check to see if the frame should be displayed on screen
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xff
        # update the fps counter
        fps.update()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # stop the timer and display the information
    fps.stop()
    print ("[INFO] elapsed time : {:.2f}".format(fps.elapsed()))
    print ("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    stream.stop()
    cv2.destroyAllWindows()



