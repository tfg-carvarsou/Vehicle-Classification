from enum import Enum

class VDModel(Enum):
    YOLOV5S = "YOLOv5s"
    RCNN = "R-CNN"

class VCModel(Enum):
    EFFNETB1 = "EfficientNetB1"
    X = "X"

class VDLabel(Enum):
    BIG_BUS = "0;big bus"
    BIG_TRUCK = "1;big truck"
    BUS_L = "2;bus-l-"
    BUS_S = "3;bus-s-"
    CAR = "4;car"
    MID_TRUCK = "5;mid truck"
    SMALL_BUS = "6;small bus"
    SMALL_TRUCK = "7;small truck"
    TRUCK_L = "8;truck-l-"
    TRUCK_M = "9;truck-m-"
    TRUCK_S = "10;truck-s-"
    TRUCK_XL = "11;truck-xl-"