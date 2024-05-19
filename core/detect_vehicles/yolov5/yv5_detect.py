import subprocess

def detect_vehicles(model_path, weights, img_size, conf, list_images):
    """
    python /home/carvarsou/.cache/torch/hub/ultralytics_yolov5_master/detect.py 
    --weights /home/carvarsou/Vehicle-Classification/models/detect_vehicles/yolov5/exp/weights/best.pt 
    --img 224 
    --conf 0.3 
    --source /home/carvarsou/Vehicle-Classification/images/detect_vehicles/yolov5/coches.jpg
    """
    for img in list_images:
        subprocess.run([
            "python",
            f"{model_path}/detect.py",
            "--weights", weights,
            "--img", str(img_size),
            "--conf", str(conf),
            "--source", img
        ])