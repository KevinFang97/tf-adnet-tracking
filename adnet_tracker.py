import runner

#path init
ADNET_MODEL_PATH = ""
VOT_PATH = "/home/yuwing/2018CK2/vot/vot-toolkit"

#import toolkit
sys.path.insert(0,VOT_PATH)
from tracker.examples.python import vot

#init runner
init_err = False
_environ = dict(os.environ)  # or os.environ.copy()
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
selection = handle.region()
bbox = boundingbox.BoundingBox(selection.x,selection.y,selection.width,selection.height)

#TODO: Redetection
while(True):
    imagefile = handle.frame()
    if not imagefile:
        sys.exit(0)
    img = commons.imread(imagefile)

    bbox = adnet.tracking(img,bbox)
    selection = vot.Rectangle(bbox.xy.x, bbox.xy.y, bbox.wh.x, bbox.wh.y)
    #TODO: Retrieve confidence from model (add return value in adnet.tracking)
    confidence = 1

    handle.report(selection, confidence)