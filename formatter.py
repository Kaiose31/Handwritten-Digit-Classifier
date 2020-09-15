import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf 
from tensorflow import keras  
import cv2
import numpy as np

model = keras.models.load_model('num_model.h5')

#formatting the input image to input to the model 
def classifier(path):
    test = cv2.imread(path,0)
    test=cv2.bitwise_not(test)
    test = cv2.resize(test,(28,28))
    test = test/255.0
    test = np.array(test)
    test = np.expand_dims(test,axis=0)
    
    prediction = model.predict(test) #Output from the model on the single image
    
    print(np.argmax(prediction)) 




path = input("enter image path: ")
classifier(path)    #input is path of the image. prints the predicted digit
