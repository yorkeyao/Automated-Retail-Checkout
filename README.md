## Automated Retail Checkout

<!-- ![fig1](https://github.com/yorkeyao/Automated-Retail-Checkout/blob/main/3D%20Models%20and%20Unity%20Source/Images/auto_retail.jpg)   -->
![auto_retail](3D%20Models%20and%20Unity%20Source/Images/auto_retail.jpg?raw=true "auto_retail")

This repository includes data and related code for [CVPR AI City Challenge 2023 Track 2](https://www.aicitychallenge.org/). This code, inherited from [VehicleX](https://github.com/yorkeyao/VehicleX/), is also part of the [Paper](https://arxiv.org/abs/2202.14034) 'Attribute Descent: Simulating Object-Centric Datasets on the Content Level and Beyond'. 

Related material: [Data](https://drive.google.com/file/d/1LIYmYmK0jh2V-Bj0CD7BHATK9xRhA7Pb/view?usp=sharing), [Demo](https://simmer.io/@yorkeyao/retail-demo). 

You may play with our [Demo](https://simmer.io/@yorkeyao/retail-demo) for a quick view of our data. This demo contains 3 objects out of 100.

## Synthetic Training Data  

[Synthetic data](https://drive.google.com/file/d/1LIYmYmK0jh2V-Bj0CD7BHATK9xRhA7Pb/view?usp=sharing) is provided for model training. There are 100,000 synthetic images from 100 3D objects. Following the generation pipeline in [1], images are filmed with random attributes, i.e., random object orientation, camera pose, and lighting. Random background images, which are selected from Microsoft COCO, are used to increase the dataset diversity. The labeling format for synthetic data is “id_num.jpg”: 

Taking “00001_697.jpg” for example: 

00001 means the object class id is 00001. 

697 is the counting number. 

We also provide segmentation labels for these images. For example, “00001_697_seg.jpg” is the segmentation label for image “00001_697.jpg”. The white area denotes the area of the object while the black shows the background.   


## Engine for Generating Synthetic Data (Unity-python Interface)

We provide a Unity-Python Interface, which you may generate your own images from python code without modifying Unity Environment or C# programming. Please check [./Unity-python Interface](https://github.com/yorkeyao/Automated-Retail-Checkout/tree/main/Unity-python%20interface) for more details.

## 3D Models and Unity source

3D Models are released together with images. They are in ".obj" format and can be imported into different graphic engines. We also released entire Unity project. Please check [./3D Models and Unity Source](https://github.com/yorkeyao/Automated-Retail-Checkout/tree/main/3D%20Models%20and%20Unity%20Source) for more details.

## Citation 

The synthetic data is generated using the pipeline from

```
@article{yao2021attribute,
  title={Attribute Descent: Simulating Object-Centric Datasets on the Content Level and Beyond},
  author={Yao, Yue and Zheng, Liang and Yang, Xiaodong and Naphade, Milind and Gedeon, Tom},
  journal={arXiv preprint arXiv:2202.14034},
  year={2021}
}
```
