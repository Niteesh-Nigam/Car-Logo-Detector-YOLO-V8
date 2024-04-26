# Car Logo Detection System Using YOLOv8
# Project Overview
This project develops a sophisticated car logo detection system (34 distinct car logos) leveraging the capabilities of YOLOv8, a state-of-the-art object detection model. The repository holds the training scripts, comprehensive configuration details, and robust dataset information to facilitate advanced computer vision tasks in automotive applications.

To access any of my trained models contact me at niteesh.nigam99@gmail.com

# Repository Contents
YOLO_Resume.py: Python script to resume YOLO model training from the latest checkpoint.
train_logo.py: Script to start training the YOLO model on car logo images from scratch.
logo.yaml: Configuration file for dataset paths, class names, and data sources.
args.yaml: Encapsulates the training hyperparameters and settings for the YOLO model.
Visualization Images: Confusion matrices, F1 curves, precision-recall curves, etc. (To be uploaded to the repository separately)
README.dataset.txt and README.roboflow.txt: Documentation providing dataset details and sourcing.

# Model Configuration and Training
# Configuration
The configuration is managed through logo.yaml, outlining paths and training parameters, such as:

Train: Path to training images
Validation: Path to validation images
Test: Path to test images
Classes: 34 distinct car logos
The args.yaml file further defines operational parameters for the training process, such as batch size, image dimensions, and the number of epochs.

# Training Scripts
train_logo.py: Initiates a fresh training session utilizing the YOLOv8 model on car logo images.
YOLO_Resume.py: Picks up training from a partially trained model checkpoint, facilitating prolonged or interrupted training periods.

# Dataset
A comprehensive dataset from multiple sources is compiled to cover a wide range of car logos, totaling over 18,000 annotated images. This data is central to training the detection model.

# Preprocessing and Augmentation
Documented in README.roboflow.txt, the dataset images undergo rigorous preprocessing and augmentation to enhance model robustness:

Brightness adjustments
Gaussian blur
And other transformations as detailed in the file

# Visualization of Results
![labels](https://github.com/Niteesh-Nigam/Car-Logo-Detector-YOLO-V8/assets/164087550/6bd01296-81e8-4f2e-bc9c-e3a49ec88433)
![labels_correlogram](https://github.com/Niteesh-Nigam/Car-Logo-Detector-YOLO-V8/assets/164087550/432b02a6-065e-4cf7-906e-c7e0b8285371)
![train_batch2](https://github.com/Niteesh-Nigam/Car-Logo-Detector-YOLO-V8/assets/164087550/6ff2af08-0c44-4047-a178-2248d50c778d)
![train_batch1](https://github.com/Niteesh-Nigam/Car-Logo-Detector-YOLO-V8/assets/164087550/e8aa1234-887e-4f76-a177-a620a3e9cc00)


