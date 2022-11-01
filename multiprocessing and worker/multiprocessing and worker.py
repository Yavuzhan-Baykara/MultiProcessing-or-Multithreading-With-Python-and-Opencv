import multiprocessing
from multiprocessing import Queue, Pool
from webcamcamera import FPS, WebcamVideoStream
import cv2

def cam_loop(cap):
    return cap

def worker(input_q,output_q):
    fps = FPS().start()
    while True:
        fps.update()
        frame = input_q.get()
        output_q.put(cam_loop(frame))

if __name__ == '__main__':
    logger = multiprocessing.log_to_stderr()
    logger.setLevel(multiprocessing.SUBDEBUG)
    input_q = Queue(maxsize=10)
    output_q = Queue(maxsize=10)
    #A process pool via the multiprocessing.
    #We choose a process to run the task, start the process, or wait for the task to complete. 
    #They Wait for the task to complete.
    pool = Pool(10, worker, (input_q,output_q))
    #grab a pointer to the wideo steam and initialize the FPS counter
    video_capture =  WebcamVideoStream().start()
    fps = FPS().start()
    #loop over same frames
    while True:
        # grab the frame from the WebcamvideoStream and imageshow
        frame = video_capture.read()
        # put keep all frame vectors in queue
        input_q.put(frame)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.imshow("Live",output_q.get())
        fps.update()
        # shutdown of mainwindow by pressing "q" with user
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    #do a bit of cleanup
    fps.stop()
    pool.terminate()
    video_capture.stop()
    cv2.destroyAllWindows()
