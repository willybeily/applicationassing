# applicationassing
This is an explanation of the assignment that I was given. First I converted the avi video file to mp4 video and then captured the frame of mp4 file using cv2.VideoCapture and 
then stored it in image. 
Now I got multiple frames of the video. This program I have done in frame.py file.
In second part, I have stored different frames in different folder and Now I am iterating to each folder and resizing each image of that folder after reading it and 
then storing it in a list called images. Now creating the instance of cv2.Stitcher.create and pass the images list to stitcher.stitch this will do the stitching of images and 
the result will be stored in answer and then I am storing it in a form of jpg image
