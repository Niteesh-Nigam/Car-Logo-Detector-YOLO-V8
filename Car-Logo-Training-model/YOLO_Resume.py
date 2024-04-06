from ultralytics import YOLO
import os


# new_directory = '/home/nitzz/PycharmProjects/Vehicle-Profiling-YOLOV8/Car-Logo-Detector-YOLO-V8/Car-Logo-Training-model/runs/detect/train12/'
# os.chdir(new_directory)

# Load a model
model = YOLO('./runs/detect/train12/weights/last.pt') # load a partial

# Resume training
results = model.train(resume=True, epochs=1000)

