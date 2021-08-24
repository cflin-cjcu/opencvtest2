from FaceDetectionModule import FaceDetector
import cv2
import cvzone.Utils
import pafy
url="https://www.youtube.com/watch?v=fvRiroJlFrw"
videoPafy = pafy.new(url)
best = videoPafy.getbest()
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(best.url)

detector = FaceDetector(model_selection=1)
heartimg = cv2.imread('./image/heart.png',cv2.IMREAD_UNCHANGED)
heartimg = cv2.resize(heartimg, (0,0),None,0.5,0.5)
while True:
    success, img = cap.read()
    img1 = cv2.imread('./image/akb.jpg')
    img, bboxs = detector.findFaces(img)
    # center = bboxs[0]["center"]
    #cv2.circle(img, center, 20, (0, 0, 255), cv2.FILLED)
    #cvzone.overlayPNG(img,heartimg,center)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()