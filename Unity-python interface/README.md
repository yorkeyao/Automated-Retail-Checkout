

## Requirements

* OS: Windows 10 or Ubuntu 14.04+. 
* Python 3.6 only.
* Linux Server: X server with GLX module enabled.

## Running with VehicleX Unity-Python Interface

The directly runnable version is available. We have both [windows version](https://drive.google.com/file/d/1ympcEZ8cYyq6rsJ4T1FM9fRKzuCV0_n3/view?usp=sharing) and [linux version](https://drive.google.com/file/d/1vXd5wyKvA4EJ7JwhK4DS7CqccC8U7Q6k/view?usp=sharing). You will also need [backgroud images](https://drive.google.com/file/d/1_hm088938cvUIK1TcotH50nmKjXTCbSL/view?usp=sharing) and [3D assets](https://drive.google.com/file/d/1EAgnQLM3P2uwq4AafkarO_GWGrAXqJcW/view?usp=sharing) prepared. Please download them by click links above and store in a file structure like this: 

```
~
└───Interface
    └───Build-win (is 'Build-linus' if you use linux)
    │   │ Retail.exe(is 'Retail.x86_64' if you use linux)
    │   │ ...
    │
    └───train2014
    │   │ COCO_train2014_000000000151
    │   │ ...
    │
    └───Assets
    │   │ Resources
    │   │ ...
    │
    └───inference_fsl.py
```

For creating environment,

```python
conda create -n py36 python=3.6
conda activate py36
```

Besides, you will need to 

```python
pip install matplotlib
pip install torch torchvision
pip install tensorflow-gpu==1.14
pip install mlagents==0.10.1
pip install scikit-image
pip install scipy==1.0
```
For a quick environment check, you can learning attributes from VehicleID extracted features with attribute descent using

```python
python inference_fsl.py
```

## Unity Development

If you wish to make changes to the Unity assets you will need to install the Unity Editor. The [source code](https://drive.google.com/file/d/17Jn5iov3e1rkWgOhID5c2RCnGWTxiuWA/view?usp=sharing) for the engine itself has been released. Please see more details in page [./Unity source](https://github.com/yorkeyao/VehicleX/tree/master/Unity%20Source). We show how to configure the source code step by step. 




