#!/usr/bin/python

import runner
import sys
import os
import commons
import random
import numpy as np
import tensorflow as tf
#path init
ADNET_MODEL_PATH = "/home/yuwing/2018CK2/adnet/tf-adnet-tracking/models/adnet-original/net_rl_weights.mat"
VOT_PATH = "/home/yuwing/2018CK2/vot/vot-toolkit"
#VOT_PATH = "/home/yuwing/2018CK2/tracking/source/fakekit"

from boundingbox import BoundingBox, Coordinate
from tracker.example.python import vot
import runner
from configs import ADNetConf

#init runner
init_err = False
_environ = dict(os.environ)  # or os.environ.copy()
ADNetConf.get('/home/yuwing/2018CK2/adnet/tf-adnet-tracking/conf/repo.yaml')
random.seed(1258)
np.random.seed(1258)
tf.set_random_seed(1258)

try:
    os.environ['ADNET_MODEL_PATH'] = ADNET_MODEL_PATH
    adnet = runner.ADNetRunner()
except:
    print("init error")
    init_err = True
finally:
    os.environ.clear()
    os.environ.update(_environ)
if init_err:
    sys.exit(0)

#start tracking
handle = vot.VOT("rectangle")
imagefile = handle.frame()
if not imagefile:
    sys.exit(0)
img = commons.imread(imagefile)
adnet.imgwh = Coordinate.get_imgwh(img)
selection = handle.region()
bbox = BoundingBox(selection.x,selection.y,selection.width,selection.height)

adnet.initial_finetune(img, bbox)

while(True):
    imagefile = handle.frame()
    if not imagefile:
        sys.exit(0)
    img = commons.imread(imagefile)
    adnet.imgwh = Coordinate.get_imgwh(img)

    bbox, confidence = adnet.tracking(img,bbox)
    selection = vot.Rectangle(bbox.xy.x, bbox.xy.y, bbox.wh.x, bbox.wh.y)
    #TODO: mapping confidence to 0~1 (if not in 0~1 range)
    #confidence = 1

    handle.report(selection, confidence)
