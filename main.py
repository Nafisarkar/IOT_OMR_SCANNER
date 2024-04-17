import cv2 
import numpy as np 
  
# Read image. 
img = cv2.imread('F:\CodeBase\IOT_OMR_SCANNER\img\Accurecy_testing.png', cv2.IMREAD_COLOR) 

# Convert to grayscale. 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Blur using 3 * 3 kernel. 
gray_blurred_frame = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray_blurred_frame, 75, 200)

cv2.imshow("Edged", edged)

# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(
    gray_blurred_frame,
    cv2.HOUGH_GRADIENT,
    1,
    20,
    param1=50,
    param2=30,
    minRadius=5,
    maxRadius=40,
)
  
# Draw circles that are detected. 
if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        # Draw the circumference of the circle. 
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
  
        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 


# Display the output.
cv2.imshow("Detected Circle", img)
cv2.waitKey(0)