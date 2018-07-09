import os
import random
import commons
import numpy as np
import tensorflow as tf
import sys
sys.path.insert(0,"/home/fang/vot/vot-toolkit")

from boundingbox import BoundingBox, Coordinate
from tracker.example.python import vot
import runner
from configs import ADNetConf

#init runner
#init_err = False
#_environ = os.environ.copy()  # or os.environ.copy()
#print(os.environ)
#try:
    #os.environ["ADNET_MODEL_PATH"] = "/home/fang/vot/adnet/tf-adnet-tracking/models/adnet-original/net_rl_weights.mat"
    #adnet = runner.ADNetRunner()
#except Exception as e:
    #print("init error")
    #print(e)
    #init_err = True
#finally:
    #os.environ.clear()
    #os.environ.update(_environ)
#if init_err:
    #sys.exit(0)
ADNetConf.get('./conf/repo.yaml')
random.seed(1258)
np.random.seed(1258)
tf.set_random_seed(1258)

adnet = runner.ADNetRunner()

#start tracking
handle = vot.VOT("rectangle")
imagefile = handle.frame()
if not imagefile:
    sys.exit(0)
selection = handle.region()
bbox = BoundingBox(selection.x,selection.y,selection.width,selection.height)

while(True):
    imagefile = handle.frame()
    if not imagefile:
        sys.exit(0)
    img = commons.imread(imagefile)

    bbox, confidence = adnet.tracking(img,bbox)
    selection = vot.Rectangle(bbox.xy.x, bbox.xy.y, bbox.wh.x, bbox.wh.y)
    #TODO: mapping confidence to 0~1 (if not in 0~1 range)
    confidence = 1

    handle.report(selection, confidence)
