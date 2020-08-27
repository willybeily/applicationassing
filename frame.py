import cv2

vedio=cv2.VideoCapture('stitch.mp4')
success, image=vedio.read()

count=0
val=True
while val:
    cv2.imwrite("frame%d.jpg" % count, image)
    val, image=vedio.read()
    print('image frame of vedio', val)
    count +=1