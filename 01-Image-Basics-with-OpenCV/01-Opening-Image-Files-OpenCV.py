import cv2

img = cv2.imread('DATA/00-puppy.jpg')

while True:

    cv2.imshow('Puppy',img)

    # EXPLANATION FOR THIS LINE OF CODE:
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    # 0xFF is a hexadecimal constant which is 11111111 in binary. By using bitwise AND (&) 
    # with this constant, it leaves only the last 8 bits of the original (in this case, whatever cv2.waitKey(0) is).
    # 27 is the ASCII value for the Esc key
    # IF we've waited at least 1 ms AND we've pressed the Esc
    if (cv2.waitKey(1) & 0xFF == 27) or (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()
