import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_triangle(event, x, y, flags, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (255,0,0), thickness=5)

def main():
    img = cv2.imread(fr"C:\Algo\Playground\03 - Learn CV Python\DATA\disabled_pixels_map.png")

    cv2.namedWindow('Testing')

    scale_ratio = 1000 / img.shape[0]
    img_small = cv2.resize(img, None, fx=scale_ratio, fy=scale_ratio)

    cv2.setMouseCallback('Testing', draw_triangle, param=img_small)

    while True:
        cv2.imshow('Testing', img_small)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()