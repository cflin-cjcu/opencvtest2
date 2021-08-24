from contextlib import suppress
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2
import pafy

np.set_printoptions(suppress=True)
# Load the model
model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
# image = Image.open('<IMAGE_PATH>')
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
url="https://www.youtube.com/watch?v=3TVkWo8GY1g"
videoPafy = pafy.new(url)
best = videoPafy.getbest()
# cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(best.url)
list = ['OPPO','Google','None']
while True:
    ret, img = cap.read()
    # size = (224, 224)
    # image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image = cv2.resize(img,(224,224))
    
    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    index = np.argmax(prediction)
    if np.max(prediction) > 0.8:
        print(prediction,list[index])

    cv2.imshow('test',image)
    if cv2.waitKey(10) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()    
