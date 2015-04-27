#understand size
import caffe
import numpy as np
import skimage.io
import sys
import time

model = "check_speed/A0.conv.prototxt"
pretrained = "check_speed/A0.conv.caffemodel"
BATCH = 1
net = caffe.Classifier(model, pretrained, gpu=True, input_scale=0.0078125, image_dims=[256,256], batch=BATCH)
IMAGE_FILE="../cat.jpg"
input_image = caffe.io.load_image(IMAGE_FILE)
data = np.asarray([net.preprocess('data', input_image)]*BATCH)
print(data.shape)
for i in range(20):
    prediction = net.forward_all(data=data)
t1 = time.time()
prediction = net.forward_all(data=data)
t2 = time.time()
print(t2-t1)
print(prediction['conv1'].shape)



