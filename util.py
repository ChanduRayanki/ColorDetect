import cv2
import numpy as np
def color_limit(color):
    c = np.uint8([[color]])
    #d = c = np.uint8([[color]])
    #print ("c",c)

    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    #print("hsvC: ",hsvC)
    lowerLimit = hsvC[0][0][0] - 10,100,100
    upperLimit = hsvC[0][0][0] + 10,255,255

    #print(f"\nlowerLimit: {lowerLimit}, upperLimit: {upperLimit}")

    lowerLimit = np.array(lowerLimit,dtype = np.uint8)
    upperLimit = np.array(upperLimit, dtype = np.uint8)

    return lowerLimit,upperLimit