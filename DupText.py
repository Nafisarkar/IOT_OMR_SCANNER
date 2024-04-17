import cv2 as cv
import numpy as np
import utils
from imutils import contours

frame = cv.imread("F:\CodeBase\IOT_OMR_SCANNER\img\image.png", cv.IMREAD_COLOR)

normal_frame = frame.copy()

gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
blur_frame = cv.GaussianBlur(gray_frame, (17, 17), 0)
edged = cv.Canny(blur_frame, 75, 200)

circles = cv.HoughCircles(
    blur_frame,
    cv.HOUGH_GRADIENT,
    1,
    20,
    param1=50,
    param2=30,
    minRadius=12,
    maxRadius=40,
)

# Initialize counter
lineCirclesCounter = 1

ans_list = [1,2,3,4,1,2,3,4,0]
ans_list_couter = 0

# Check if circles are detected before sorting
if circles is not None:
    circles = np.uint16(np.around(circles))
    
    # Sort circles based on y-coordinate (top to bottom) and then x-coordinate (left to right)
    circles = sorted(circles[0], key=lambda x: (x[1], x[0]))
    
    counter = 1 
    match = ans_list[ans_list_couter]
    for i in circles:
        if counter == match:
            print("Matched " , counter , " : " , match)
            cv.circle(normal_frame, (i[0], i[1]), i[2], (0, 0, 255), 2)
        else:
            cv.circle(normal_frame, (i[0], i[1]), i[2], (0, 255,0), 2)
            print(counter , " : " , match)
            
        if counter%4 == 0:
            print("counter ",counter, match)
            print("--------------------")
            ans_list_couter+=1
            match = ans_list[ans_list_couter]
            counter = 0
            
        counter+=1
        
        
        # if lineCirclesCounter%4 == 0:
        #     match = ans_list[ans_list_couter]+lineCirclesCounter
        #     ans_list_couter+=1
        
        # if lineCirclesCounter == match:
        #     cv.putText(blur_frame, str(ans_list[0]), (i[0], i[1]), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
        #     match = 0
            
        # else:
        #     cv.circle(blur_frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # lineCirclesCounter += 1
        
        

print("Number Of Circles : ", lineCirclesCounter)

resized_frame = cv.resize(normal_frame, (600, 800))
utils.show_imagescv(resized_frame)
