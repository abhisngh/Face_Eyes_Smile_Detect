# Face_eyes_smile-detection
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)  [![HitCount](http://hits.dwyl.io/ASH1998/android-digit-recogniser.svg)](http://hits.dwyl.io/ASH1998/android-digit-recogniser)   
This is an OpenCV application for face, eyes, smile detection. It uses haarcascade provided by OpenCV

## Requirements :
1. The PC should have a working Webcam(mainwebcam 0, other cams 1 or further numbers)
2. Must allow third party connection with WebCam

## Dependencies :
1. Python     
2. Opencv-Python
3. Download the required haars from [here](https://github.com/opencv/opencv/tree/master/data/haarcascades). 
4. Some of the haars are provided like for face,eyes and smile.    
4. cx_freeze(if you want to run `setup.py` for making a windows binary(.exe) file).

## Usage:
After successful installation of opencv-python and downloading the haars, run the script and change in the haar name in `cv2.CascadeClassifier` in the program `FACE_EYES_SMILE_DETECTION.PY`

## Copyright
MIT License