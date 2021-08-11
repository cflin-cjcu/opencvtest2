import cv2 

#讀圖        
img = cv2.imread('./image/test2.png',cv2.IMREAD_GRAYSCALE)
#秀圖
cv2.imshow('abcd',img)
#等待按鍵，關閉視窗
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
#寫檔案
elif k==ord('s'):
    cv2.imwrite('output.png',img)
    cv2.destroyAllWindows()    
