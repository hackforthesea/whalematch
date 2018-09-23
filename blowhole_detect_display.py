#!/usr/bin/python
# -*- coding: utf-8 -*-

from cv2 import (CascadeClassifier, imread, cvtColor, rectangle, imshow, imwrite,
                 waitKey, destroyAllWindows, COLOR_BGR2GRAY)

cascade = CascadeClassifier('trainingdata/cascade.xml')
whalepic = 'Other/DJI_0009/whale01978.jpg'
# whalepic = 'Other/DJI_0014/whale00238.jpg'
# whalepic = 'Alaska 2017 (Fall)/6AK2017_BlowholeCompilation_0930/whale00169.jpg'
img = imread(whalepic)
gray = cvtColor(img, COLOR_BGR2GRAY)
blowholes = cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in blowholes:
    print("{} {} {} {}".format(x, y, w, h))
    rectangle(img, (x, y), (x + w, y + h), (0, 204, 204), 2)
imwrite('output.jpg', img)
imshow(whalepic, img)
waitKey(0)
destroyAllWindows()
