# **Cartoon Detector**
*Project for fun / time-pass to utilize quarantine period* 😜  
A deep learning model that detects which cartoon is there in the image or video using YOLO Object Detection algorithm
## Dataset
The dataset consists of 1472 images belonging to 5 different cartoon categories and 1258 annotation files (yolo format):
1. Shinchan - 336
2. Doraemon - 362
3. Detective Conan - 295
4. Mr Bean (animated) - 240
5. Naruto - 239  
### Gathering Images
Images were downloaded using [**Bing Image Search API**](https://azure.microsoft.com/en-in/services/cognitive-services/bing-image-search-api/)  
  
Search queries included : "shinchan", "doraemon", "detective conan", "mr bean animated", "naruto"  
  
Here is the [Script](https://github.com/jainamshah17/cartoon-detector/blob/master/scripts/bing_images.py) to download images using bing image search api  
  
### Annoting Images
Images were annoted using [**Label Img Tool**](https://github.com/tzutalin/labelImg), you can easily install LabelImg with pip from the Terminal:  
```
pip install labelimg
```  
Once labelImg is successfully installed, launch it by typing:  
```
labelImg [path to image directory] [classes file]
```  
After launching labelimg, you can draw bounding box around the objects and it will automatically save them in a seperate .txt file, don't forget to change format to "yolo" in labelimg  
  
![labelImg](https://github.com/jainamshah17/cartoon-detector/blob/master/images/labelimg.jpg)  
  
Refer to this [video](https://youtu.be/zSda1AoUTkc) if any doubts
## Deep Learning Model
I have used [**yolov2**](https://arxiv.org/pdf/1612.08242.pdf) object detection algorithm  
### Training  
[**darknet**](https://github.com/AlexeyAB/darknet) - open source deep learning framework is used to train the model. I won't explain how to install darknet, refer [link](https://pjreddie.com/darknet/install/) for installation.  
  
Model was initialized with [**yolov2's pre-trained weights**](https://pjreddie.com/darknet/yolo/)  
  
Configuration file **yolov2.cfg** was changed, filters in last convolutional layer and no of classes as:  
```
237: filters=50
244: classes=5
```  
No. of Filters are calculated using the following formula, so if you are training on different dataset, change accordingly
```
filters = (5 + no. of classes) * 5
```  
**Note:** No. of classes in cfg file should match with no. of classes in your labels file  
  
Model was initialized with following training parameters:  
```
learning_rate = 0.001  
decay = 0.0005  
momentum = 0.9  
```
*Model was trained for 250 Epochs on google collab using batch size of 64 and subdivision of 4*    
  
To train the model using darknet, run the following code:  
  ```
  ./darknet detector train cfg/cartoon.data cfg/yolov2.cfg weights/yolov2_pretrained.weights
  ```
  
*Accuracy*  
  - Region Avg IOU : 87.8429  
  - Class : 99.8973  
  - Obj : 84.0069  
  - Avg Recall : 100  
    
*Losses*  
  - Overall loss : 0.025661  
    
**Trained Weights File** [Download from here](https://drive.google.com/file/d/1zx5nlMvY95NlH1qmDjS8TWo2a0N2Nspi/view)  
### Detection on Images
To perform detection on image, run the following code:  
  ```
  ./darknet detector test cfg/cartoon.data cfg/yolov2.cfg weights/cartoon_yolo.weights "path_to_img/img.jpg"
  ```  
      
**Input Image**  
![Input Image](https://github.com/jainamshah17/cartoon-detector/blob/master/images/inputs/bean_4.jpg)  
  
**Output Image**  
![Output Image](https://github.com/jainamshah17/cartoon-detector/blob/master/images/outputs/bean_4.jpg)  
  
*Refer to "images" folder for more*  
  
### Detection on Video  
*Required to compile darknet with opencv=1 in Makefile*  
  
To perform detection on video, run the following code:  
  ```
  ./darknet detector demo cfg/cartoon.data cfg/yolov2.cfg weights/cartoon_yolo.weights "path_to_video/video.mp4"
  ```  
## References  
- [Yolov2](https://arxiv.org/pdf/1612.08242.pdf)  
- [Darknet](https://github.com/AlexeyAB/darknet)  
- [LabelImg](https://github.com/tzutalin/labelImg)  
- [Bing Search Api](https://azure.microsoft.com/en-in/services/cognitive-services/bing-image-search-api/)  
