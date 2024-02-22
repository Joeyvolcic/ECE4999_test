from picamera2 import Picamera2 
import time
import cv2

picam0 = Picamera2(0)
picam0.preview_configuration.main.size = (2304,1296)
picam0.preview_configuration.main.format = "RGB888"
picam0.configure("preview")
picam0.start()


picam1 = Picamera2(1)
picam1.preview_configuration.main.size = (2304,1296)
picam1.preview_configuration.main.format = "RGB888"
picam1.configure("preview")
picam1.start()

posy = 0
posx = 1



while True:

	if cv2.waitKey(1) == ord('2'):
		posx = 2
	if cv2.waitKey(1) == ord('3'):
		posx = 3
	if cv2.waitKey(1) == ord('1'):
		posx = 1

		
	im0 = picam0.capture_array()
	
	im1 = picam1.capture_array()
	stiched_image = cv2.hconcat([im0,im1])
	image_zoomed = stiched_image[0:400*posx,500:500+  400*posx]
	image_zoomed = cv2.resize(image_zoomed, (1000,1000))
	
	
	#cv2.imshow("Camera", im0)
	#cv2.imshow("Camera2", im1)
	cv2.imshow("Stiched", stiched_image)
	cv2.imshow("zoomed", image_zoomed)
	


	
	if cv2.waitKey(1) == ord('q'):
		break
cv2.destroyAllWindows()

 
