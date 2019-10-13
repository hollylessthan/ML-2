# Homework 3-1

**Introduction**
-
This code is written in Python 3.7.0 64-bit

**Explanation of the Code**
-

As a start, I open the data in .txt file and give them lebels of positive class or negative class. Then I put those lebels into c_train list.

Secondly, I define a function, per, using perceptron learning as a linear classifier.

Thridly, I use for-loops to train the data. Note that "init" list is the initial weights of all attributes and "learn" list is the learning rates we have to try one by one. If the class classified by the "per" function is equal to the class lebeled in c_train, we use the same weight of attributes. Otherwise, we change its weight according to the learning rates (adjust the "init" list at the same time) and also add one to the number of example-presentations(h_c). Furthermore, I print out the final weights of the attributes of differentlearning rates and the "h_c" list as well.

Finally, I used matplotlib to draw a diargram to compare the numner of example presentations of different learning rates. Unfortunately, it seems like there's no significant difference between them.
