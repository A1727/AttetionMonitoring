# DLIB requirements

## DLIB
if we are looking at the problem of computer vision or something related to it you should heard of this library. according to it's git-hub page DLIB is toolkit for making real world machine learning and data analysis applications in c++(though it is also can be used in python).DLIB is written in C++.

<!-- ## HOG for Human detection
here all hog realed data should be present

## SVM in Dlib
here all svm related information include in king's pdf will be present

 -->

## HOG+SVM Based DLIB object Detector

   in dlib version 18.6 there are some great changes are made by author(Davis E. King). one of them was a tool for creating HOG(Histogram of oriented gradient)based object detector. this method which is used for detecting object in image which has become a classic computer vision method since navneet dalal has introduced it in 2005. dlib is included in its new version with tool to train this HOG detectors super fast and easy for face detection .It is tremendously improved version of the haar cascade based on OpenCV model for face detection which takes days to train such a model in it. moreover the HOG trainer uses dlib structural SVM based training algorithm which enables it to train on all the sub-windows in every image. this means we don't have to perform any tedious task such as sub-sampling(converting data into positive and negative samples) or "hard negative mining"(training a network with negative sample where data is not present). it also means we don't need much training data to train the network. This is useful to produce a result better than any state of the arts technique in this domain with such minimal requirements.and also training a data is fast in dlib it will take few minutes to train a dataset of thousand images.

since we are using dlib for identifying 68 facial points we are using already trained weights of dlib. which is trained on the structural SVM based training algorithm of dlib.
