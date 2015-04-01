# proto server
import sys
import SocketServer
import struct
import request_pb2
import caffe
import numpy as np
import time
import os
import cv2
import sys
from PIL import Image
from img_util import load_image_from_memory, load_face_from_memory
labels = {"arvind+krishnamurthy":0, "haichen+shen":1, "matthai+philipose":2, "seungyeop+han":3}
caffe_dir = "../caffe"
#MODEL_FILE="../../haichen/models/caffe/A0.prototxt"
#PRETRAINED="../../haichen/models/caffe/A0.caffemodel"
MODEL_FILE="../vggnet/VGG_ILSVRC_19_layers.prototxt"
PRETRAINED="../vggnet/VGG_ILSVRC_19_layers.caffemodel"
net = caffe.Classifier(MODEL_FILE, PRETRAINED, 
        mean=np.load(caffe_dir + '/python/caffe/imagenet/ilsvrc_2012_mean.npy'),
        gpu=True, channel_swap=(2,1,0), image_dims=(256,256), raw_scale=255, batch=10)
caffe.set_phase_test()
caffe.set_mode_gpu()
#with open("synset_words.txt") as f:
#    words = f.readlines()
with open("/home/haichen/datasets/imagenet/meta/2012/synset_words_caffe.txt") as f:
    words = f.readlines()
words = map(lambda x: x.strip(), words)

model_path = "face_models"
data_path = "/home/haichen/datasets/MSRBingFaces/"
from example import * 
#lbl = face_recognition(os.path.join(data_path, "iu/112.jpg"), [152,152], [152,152], os.path.join(model_path, "D0.prototxt"), os.path.join(model_path, "D0.caffemodel"))
#net = face_net([152,152], [152,152], os.path.join(model_path, "D0.bottom.prototxt"), os.path.join(model_path, "D0.bottom.caffemodel"))
face_net1 = face_net([152,152], [152,152], os.path.join(model_path, "D0.prototxt"), os.path.join(model_path, "D0.caffemodel"))
"""
input_image = skimage.io.imread(sys.argv[1])
prepared = face_input_prepare(net, [input_image]) 
out = net.forward_all(**{net.inputs[0]: prepared})
"""

#face_net2 = caffe.Net(os.path.join(model_path, "D0.test2.prototxt"), os.path.join(model_path, "face_retarget2_train_iter_20000.caffemodel"))
#out2 = net2.forward_all(**{net2.inputs[0]: out["Result"]})

import os
import psutil
#p = psutil.Process(os.getpid())
#p.set_cpu_affinity(range(12,24))

class MyTCPHandler(SocketServer.StreamRequestHandler):
    def read_n(self, n):
        buf = ''
        while n > 0:
            data = self.rfile.read(n)
            if data == '':
                raise RuntimeError('unexpected connection close')
            buf += data
            n -= len(data)
        return buf

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        beg = time.time()
        len_buf = self.rfile.read(4)
        length = struct.unpack('>L', len_buf)[0]
        print("len" + str(length))
        payload = self.read_n(length)
        req = request_pb2.DNNRequest()
        req.ParseFromString(payload)

        t1 = time.time()
        """
        with open("test.jpg", "wb") as f:
            f.write(req.data)
        input_image = caffe.io.load_image("test.jpg")
        """
        t2 = time.time()
        if(req.type == request_pb2.FACE):
            print("starting prediction")
            input_image = load_face_from_memory(req.data)
            prepared = face_input_prepare(face_net1, [input_image]) 
            out = face_net1.forward_all(**{face_net1.inputs[0]: prepared})
            #out2 = face_net2.forward_all(**{face_net2.inputs[0]: out["Result"]})
            print(out2["prob"].argmax())
            return
        else:
        #prediction = net.forward_all(data=np.asarray([net.preprocess('data', input_image)]))
            input_image = load_image_from_memory(req.data)
            prediction = net.predict([input_image])
            print(prediction)
            t3 = time.time()
            i = prediction.argmax()
            label = words[i]
            print(i, label)

        print "{} wrote:".format(self.client_address[0])
        response = request_pb2.DNNResponse()
        response.success = True
        response.result = i
        response.result_str = label
        s = response.SerializeToString()
        packed_len = struct.pack('>L', len(s))
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(packed_len + s)

if __name__ == "__main__":
    #HOST, PORT = "", 9999
    HOST, PORT = "", int(sys.argv[1])

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print("SERVER started")

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

