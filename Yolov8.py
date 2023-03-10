from ultralytics import YOLO
#import cv2
#import time
#import os


# Object Detection Models

#model = YOLO("yolov8x.pt")          # Detection ( Extra Large )
#model = YOLO("yolov8l.pt")           # Detection ( Large Model )
#model = YOLO("yolov8m.pt")          # Detection ( Medium Model)
#model = YOLO("yolov8s.pt")          # Detection ( Small Model )
model = YOLO("yolov8n.pt")          # Detection ( Nano Model  ) 


# Segmentation Model

#model = YOLO("yolov8m-seg.pt")       # Segmentation (Medium Model)



# Predictions for  Directory Folder, videos, images, and webcam

model.predict(source="C:/Users/zeeshan/Downloads/yolov8/Data/Images", show=True, save=True) # Images Directory Folder
#model.predict(source="C:/Users/zeeshan/Desktop/yolov8/Data/Videos", show=True, save=True) # Videos Directory Folder
#model.predict(source= '0', show=True, save=True) # Webcam


#model.predict(source="C:/Users/zeeshan/Desktop/yolov8", save=True) 




#model.info(verbose=True)  '                     # Print model information
#model.export(format="onnx")                    #export model into ONXX



