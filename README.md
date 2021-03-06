## Whalematch
A project designed and developed by [Rich Bean](https://github.com/rbeanqa), [Eric W. Brown](https://github.com/Feneric), [Rhianon Brown](https://github.com/Rhi-Bot), [Ted Greene](https://github.com/tngreene), [Isaac Vandor](https://github.com/isaacvandor), and subject matter expert [Chris Zadra](https://www.linkedin.com/in/chriszadra/).

![Logo](https://raw.githubusercontent.com/hackforthesea/whalematch/master/docs/WhaleMatchLogo.png)

### Introduction
Whalematch is a [Hack for the Sea 2018](https://www.hackforthesea.tech/GLO) project designed to detect, identify, and classify whales based on their blowholes. 

Using a dataset provided by Ocean Alliance, we built a framework to extract still frames from drone footage shot over a whale, pass those still images into a testing and a training set to create a convolutional neural network model, and then predict the unique identifier of a whale given an input image. The block diagram below outlines the way data is passed through Whalematch to create a successful detection.

![This block diagram](https://raw.githubusercontent.com/hackforthesea/whalematch/master/docs/whalematch.jpg)

### Things We Tried that Didn't Work
We tried two different approaches to the identification and classification problem: one used computer vision techniques while the other used machine learning techniques. Ultimately, the machine learning approach produced more accurate classifications. Future work could include a blending of these approaches, such as using computer vision to pre-process images and improve the machine learning model.

#### OpenCV
1. Haar classification using the full dataset of positive blowholes
2. Haar classification using an auto-generated dataset

#### Machine Learning (Keras)
1. A CNN using the SGD optimizer
2. A CNN using the Adadelta optimizer
3. A CNN using the RMSprop optimizer

For more on the OpenCV approach, see [this tutorial on face recognition using Haar classifiers](https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html). For more on the machine learning approaches, see [this tutorial on face recognition using Keras](https://medium.freecodecamp.org/making-your-own-face-recognition-system-29a8e728107c).

### The End Product
Ultimately, the machine learning approach utilizing a convolutional neural net and the Adam optimizer worked best for recognizing and classifying blowholes. Example output from running Whalematch can be seen below.

![Example Whalematch Output](https://raw.githubusercontent.com/hackforthesea/whalematch/master/docs/Whalematch%20Output.jpg)

### Future Work and Improvements
A (not even close to complete) list of things to make Whalematch 2.0 better:
1. A larger dataset (both in size and variation) of images without a blowhole for training and images with a blowhole for testing
2. A dataset mapping whale names to blowholes (for labelling the testing data with more than alphabetical letters)
3. Fine-tuning the convolutional neural network model for this task specifically
4. An automatic method for generating the dataset
5. Investigation into how we can improve results by using blowhole movement time signatures from video streams

### Running the code yourself
To run the code yourself, you'll need to:
1. clone this repository - `git clone https://github.com/hackforthesea/whalematch.git`
2. If you don't have pip installed, `sudo apt-get install python-pip python-dev build-essential` 
3. cd into the whalematch folder where you cloned the whalematch repository
4. run `pip install -r requirements.txt`
5. run `python prediction.py` with a command-line arg for your filename input image
6. Example command to run classification: `python prediction.py -i 'whale589.jpg' `

### Optional: Running with Docker ([requires Docker > 0.5.3](https://askubuntu.com/a/477554/151917))

1. clone this repository - `git clone https://github.com/hackforthesea/whalematch.git`
2. Build the docker comtainer - `docker build -t whalematch:dev .`
3. Run the built container

```
docker run -it --rm -v `pwd`:/usr/src/app --name whalematch whalematch:dev bash
```

4. From the new bash shell within the container, run `python prediction.py -i 'whale589.jpg'`

### Troubleshooting
If you have problems with installation or running the code, [start here](https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/). Otherwise, contact one of the developers above or [Isaac Vandor](mailto:isaacvandor@gmail.com).
