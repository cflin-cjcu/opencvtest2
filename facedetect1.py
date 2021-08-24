from FaceDetectionModule import FaceDetector
import cv2
import cvzone.Utils

cap = cv2.VideoCapture(0)

detector = FaceDetector(model_selection=1)
heartimg = cv2.imread('./image/heart.png',cv2.IMREAD_UNCHANGED)
while True:
    success, img = cap.read()
    img1 = cv2.imread('./image/akb.jpg')
    img, bboxs = detector.findFaces(img1)
    center = bboxs[0]["center"]
    # cv2.circle(img, center, 30, (0, 0, 255), cv2.FILLED)
    cvzone.Utils.overlayPNG(img,heartimg,center)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()