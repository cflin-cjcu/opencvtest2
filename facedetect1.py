from FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(0)

detector = FaceDetector(model_selection=1)

while True:
    success, img = cap.read()
    img1 = cv2.imread('./image/akb.jpg')
    img, bboxs = detector.findFaces(img1)
    #center = bboxs[0]["center"]
    # cv2.circle(img, center, 20, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()