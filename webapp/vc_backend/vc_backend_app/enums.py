from enum import Enum

class VDModel(Enum):
    YOLOV5S = "YOLOv5s"
    RCNN = "R-CNN"

class VCModel(Enum):
    EFFNETB1 = "EfficientNetB1"
    X = "X"