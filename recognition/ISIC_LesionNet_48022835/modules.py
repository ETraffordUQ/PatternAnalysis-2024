"""
Can be called explicitly to install commonly used weights for different model sizes.
Imported into other scripts to access a YOLO model w/ given weights.

@author Ewan Trafford
"""

from ultralytics import YOLO

def YOLOv11(weights_path):

    return YOLO(weights_path)

# Only run modules.py to pre-install weights for useful models | not required
if __name__ == "__main__":
    model_s = YOLOv11("yolo/yolo11n.pt")
    model_m = YOLOv11("yolo/yolo11m.pt")
    model_l = YOLOv11("yolo/yolo11l.pt")