# -*- coding: utf-8 -*-
"""PROGRAM TRASH GO YOLO V5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cdt1HLF3ZnIdoEaxU_66TSslQsCLw9kI

# Setup

Clone repo, install dependencies and check PyTorch and GPU.
"""

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/ultralytics/yolov5  # clone
# %cd yolov5
# %pip install -qr requirements.txt  # install

# Commented out IPython magic to ensure Python compatibility.
import torch, torchvision
!git clone https://github.com/WongKinYiu/yolov7.git
# %cd yolov7
# %pip install -qr requirements.txt
!wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt

import torch

from yolov5 import utils
display = utils.notebook_init()  # checks

!unzip /content/train2.zip

# Training
!python train.py --img 640 --batch 8 --epochs 300  --data custom_data.yaml --weights yolov7_training.pt --cfg cfg/training/yolov7.yaml --hyp data/hyp.scratch.custom.yaml

!python train.py
--img 640
--batch 8
--epochs 300
--data custom_data.yaml
--weights yolov7_training.pt
--cfg cfg/training/yolov7.yaml
--hyp data/hyp.scratch.custom.yaml

"""

```
# Ini diformat sebagai kode
```


`detect.py` runs YOLOv5 inference on a variety of sources, downloading models automatically from the [latest YOLOv5 release](https://github.com/ultralytics/yolov5/releases), and saving results to `runs/detect`. Example inference sources are:

```shell
python detect.py --source 0  # webcam
                          img.jpg  # image
                          vid.mp4  # video
                          path/  # directory
                          path/*.jpg  # glob
                          'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                          'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```"""

--logdir runs/train

!unzip /content/test.zip

#testing
!python detect.py --weights /content/yolov7/runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source /content/test

model.save_weights('/content/yolov7/runs/detect/exp')

#testing with images
!python detect.py --weights /content/best.pt --img 640 --conf 0.25 --source /content/testing/test1.jpg

!unzip /content/testing.zip

#performa
from utils.plots import plot_results
plot_results('/content/yolov5/runs/train/exp2/results.csv')