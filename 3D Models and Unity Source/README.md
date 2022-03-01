## Separate 3D models

[3D modeles](https://drive.google.com/file/d/1p14lhyvYNYCJvl-qhXdb_StuNZN7C_q-/view?usp=sharing) are released. Please see 100 3D scans in the formate of '.obj'. 

## Source Code 

Source Code is based on [Unity](https://unity.com/). Here we released the whole [Unity project](https://drive.google.com/file/d/1LIYmYmK0jh2V-Bj0CD7BHATK9xRhA7Pb/view?usp=sharing) include both **3D retail models** and **Unity python interface**. The project is stored in the google drive due to its size. [Background images](https://drive.google.com/file/d/1_hm088938cvUIK1TcotH50nmKjXTCbSL/view?usp=sharing), selected from COCO, are also required. Please download them by click links above. Once you download them the file structure should be like:

```
~
└───Source
    └───Assets
    │   │ Resources
    │   │ ...
    │
    └───train2014
    │   │ COCO_train2014_000000000151
    │   │ ...
    │
    └───Library
    │
    ...
```

[Unity hub](https://docs.unity3d.com/Manual/GettingStartedInstallingHub.html) is recommended to manage Unity projects. Please use Unity version 2019.3.0a8 or above. Once both the project and Unity editor are ready. The project can be opened easily by the Unity hub.    

![fig1](https://github.com/yorkeyao/VehicleX/blob/master/Unity%20Source/Images/unity_hub.PNG)  

## Image Generation by Unity Editor

* Open the project using Unity hub and you will see the interface below.
* Download the Unity python interface files.
* Comment out line 35 and uncomment line 36 for Inference.py in Unity python interface.  
* Run Inference.py and you will see a notice to press the play button. 
* Press the play button ▶️ in Unity Editor to get the images of Vehicles. 

![fig2](https://github.com/yorkeyao/VehicleX/blob/master/Unity%20Source/Images/interface.PNG) 

## Notice

* Please make sure the resolution of the game is 1920*1080. It can be controled in the game tab.
* If you see error CS1061: 'RawImage' does not contain a definition for 'm_Texture'. Please replace Unity/Hub/Editor/2019.3.0a8/Editor/Data/Resources/PackageManager/BuiltInPackages/com.unity.ugui/Runtime/UI/Core/Rawimages.cs with ./Script/RawImage.cs in this github project (Path can be different depends on your Unity version).
* Due to copyright issues. We are only able to release part of vehicle models in source code. The build version has all vehicle models included.  




