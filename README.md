# Image Processing 
This is the final stage in the image processing diagram. In this stage, features are extracted to detect objects in the image. 
The ROV team participated in MATE 2020, an international student underwater robotics competition (Remotely Operated Vehicle – ROV). The competition included three tasks, one of which focused on coral reefs.
The objective of this task was to identify coral reef growth and bleaching (where pink areas change to white) by comparing current images with previous data, represented by the left image in the figure below.

<img width="718" height="262" alt="image" src="https://github.com/user-attachments/assets/b5dd135d-fa08-4d54-9047-40f72361646a" />

The first step is to remove the background for the image to remove the varying in pixels when subtracting the two image by removing the background in the same area will be zero which equal to black color. 
There are many ways to remove the background. The easiest one is to identify the upper and lower range of the background and remove every pixel in this range of the color.

<img width="707" height="274" alt="image" src="https://github.com/user-attachments/assets/3de95da5-8b12-4abf-bb1a-77f4a24a3402" />


The second step is to align the two images to ensure that the data in both images are properly matched. When the images are correctly aligned, subtracting them results in zero values, 
producing a black image. This is achieved by selecting points of interest in each image and matching the two images accordingly.

<img width="787" height="238" alt="image" src="https://github.com/user-attachments/assets/3501f3b7-3945-4da8-ba64-1679ae04be4d" />

The third step is to subtract the current image from the previous data to determine the growth area and apply a threshold to the resulting subtraction image.


<img width="789" height="249" alt="image" src="https://github.com/user-attachments/assets/40e1277e-701b-417a-9b8d-1ffbd20da4d0" />


The fourth step is to subtract the past data from the current image in order to detect growth in the coral reef.


<img width="409" height="246" alt="image" src="https://github.com/user-attachments/assets/d0476956-af00-4fe9-a6e8-e6d6ff67f16f" />


The Final Step is to get the contour of largest shapes in the image and Draw the bounding box in each shape Red color to detect the growth and the green color to detect the Blotching.


<img width="691" height="252" alt="image" src="https://github.com/user-attachments/assets/3214ac28-af86-4f9d-917e-053a0685bd5b" />

# Yolo (You Only Look Once)

The Predictions Vector
YOLO (You Only Look Once) is a neural network for object detection. It's an object detector that uses features learned by a convolutional neural network to detect an object. Take an image as input and pass it through a neural network that looks similar to a normal CNN, and you get a vector of bounding boxes and class predictions in the output. 
The input image is divided into an S x S grid of cells. The confidence reflects the presence or -absence of an object one grid cell is said to be “responsible” for predicting it. That is the cell where the center of the object falls into. 
Each grid cell predicts B bounding boxes as well as C class probabilities. The bounding box prediction has 5 components: (x, y, w, h, confidence). The (x, y) coordinates represent the center of the box, relative to the grid cell location (remember that, if the center of the box does not fall inside the grid cell, than this cell is not responsible for it). These coordinates are normalized to fall between 0 and 1. The (w, h) box dimensions are also normalized to [0, 1]


<img width="510" height="238" alt="image" src="https://github.com/user-attachments/assets/902775da-0556-49f4-83f7-9ad7f3676197" />

Training 
First, pre-train the first 20 convolutional layers using the ImageNet 1000-class competition dataset, using an input size of 224x224.
Then, increase the input resolution to 448x448.
Train the full network for about 135 epochs using a batch size of 64, momentum of 0.9 and decay of 0.0005.
Learning rate schedule: for the first epochs, the learning rate was slowly raised from 0.001 to 0.01. Train for about 75 epochs and then start decreasing it.


Training Custom data using Yolo 


<img width="880" height="668" alt="image" src="https://github.com/user-attachments/assets/6f4a681f-9e9e-4bd7-b22a-a64c6d2e15fc" />

In the figure above, the dataset consists of 77 images, including 67 images of coral reefs and 93 images of fish. The dataset is relatively small, which negatively affected the overall accuracy; however, the results were still acceptable. In some images, the confidence score reached up to 83%, which is considered a good result for a small dataset.


<img width="748" height="302" alt="image" src="https://github.com/user-attachments/assets/9e38766a-9302-4d63-a46e-e49971ac8864" />



![Uploading image.png…]()


