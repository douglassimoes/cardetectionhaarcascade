import cv2 as cv 
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

videocap = cv.VideoCapture('car_video_cut.mp4')

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4',fourcc, 20.0, (562,562))

# Load the trained model
cascade = cv.CascadeClassifier('cascade/cascade.xml')

# Read until video is completed
while(videocap.isOpened()):
  # Capture frame-by-frame
  ret, frame = videocap.read()
  if ret == True:

    detected_cars = cascade.detectMultiScale(frame,minNeighbors=4,minSize=(64,64));
    for (column, row, width, height) in detected_cars:
        cv.rectangle(
        frame,
        (column, row),
        (column + width, row + height),
        (0,255,0),
        2
    )

    # Save frames on the video file
    out.write(frame)

    # Display the resulting frame
    cv.imshow('Frame',frame)

    # Press Q on keyboard to finish the program
    if cv.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object and the VideoWriter object
videocap.release()
out.release()

# Closes all the frames
cv.destroyAllWindows()

print('Done.')