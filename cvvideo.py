# import cv2

# cap = cv2.VideoCapture(0)

# # Check if webcam is accessible
# if not cap.isOpened():
#     print("Error: Cannot access webcam")
#     exit()

# # Get the frame size dynamically
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))

# # Use 'mp4v' codec and .mp4 extension for macOS
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame")
#         break

#     out.write(frame)
#     cv2.imshow('Live', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release everything
# cap.release()
# out.release()
# cv2.destroyAllWindows()



#---------------------

#video starting

import cv2
import numpy as np

# Open the video file
cap = cv2.VideoCapture('output.avi')  # Change to 'output.mp4' if needed

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()

while True:
    ret, frame = cap.read()

    # Break if end of video or frame read fails
    if not ret:
        print("Reached end of video or failed to read frame.")
        break

    # Display the frame
    cv2.imshow("Video Playback", frame)

    # Press 'q' to quit playback
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release video file and close windows
cap.release()
cv2.destroyAllWindows()


  
