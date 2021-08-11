#Import only if not previously imported
import cv2

# Create a Video Reader Object.
cap = cv2.VideoCapture(0)


#Define the codec for the Video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#Create Video Writer Object
writer = cv2.VideoWriter('output1.avi',fourcc, 30, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        writer.write(frame)
        cv2.imshow("Frame",frame)
        # Exit on pressing esc
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()
