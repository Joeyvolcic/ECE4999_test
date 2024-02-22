import cv2
from picamera2 import Picamera2

picam0 = Picamera2(0)
picam0.preview_configuration.main.format = "RGB888"
picam0.preview_configuration.align()
picam0.configure("preview")
picam0.start()

picam1 = Picamera2(1)
picam1.preview_configuration.main.format = "RGB888"
picam1.preview_configuration.align()
picam1.configure("preview")
picam1.start()




while True:
    im0 = picam2.capture_array()
    im1 = picam2.capture_array()
    stiched_image = cv2.hconcat([im0, im1])
    
    cv2.imshow("Camera", stiched_image)
    #cv2.imshow("Camera", im0)
    #cv2.imshow("Camera", im1)
  
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()
