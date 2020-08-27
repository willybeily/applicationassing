import os
import cv2

Folder='stitches'
myfolders=os.listdir(Folder)
print(myfolders)
i=['a','b','c','d','e']
k=-1
for folder in myfolders:
    path = Folder + '/' + folder
    images = []
    mylist = os.listdir(path)
    print(f'Total no of images detected {len(mylist)}')
    for imgn in mylist:
        curImg = cv2.imread(f'{path}/{imgn}')
        curImg = cv2.resize(curImg, (0, 0), None, 1, 1)
        images.append(curImg)

    stitcher = cv2.Stitcher.create()
    (result, answer) = stitcher.stitch(images)
    if (result == cv2.STITCHER_OK):
        k=k+1
        print('image done')
        cv2.imshow(folder, answer)
        cv2.imwrite('imageoutput'+i[k]+'.jpg',answer)
        cv2.waitKey(1)
    else:
        print('showing error')

cv2.waitKey(0)