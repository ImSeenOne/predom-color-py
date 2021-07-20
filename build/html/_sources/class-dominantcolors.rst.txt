class DominantColors
====================

This is basically the heart of the project. This class has the main method where the image is processed by the class KMeans provided by SciKit Learn, a Python Library for Machine Learning.

CLUSTER constant
----------------
This is the number of clusters that KMeans will be using while processing the image. Let's define a cluster like a collection of data aggregated because of certain similarities.

IMAGE constant
--------------
This is just the path to the image to be processed, this is set when the object is instanciated via the constructor.

COLORS constant
---------------
This constant is set when the clusters are found after processing the image. In the code, I set clusters centers, which are our dominant colors.

LABELS constant
---------------
These labels are set (just like the COLORS constant) right after processing the image and are for future usages, there is not any current useful usage particularly for this project.

``__init__(image, clusters=3)``
-------------------------------
The constructor just sets values to IMAGE and CLUSTERS. In case the clusters are not set, we set it as 3.

``dominantColors()``
--------------------
The main method. Here is where all the magic happens. Firstly we grab our image and pass it tou our kind friend OpenCV, change the order or the RGB pixels, reshape it to a Python list. Then we start using the SciKit Learn class KMeans to start processing the clusters, and finally we return the colors as RGB integers.

``rgb2names(rgb_tuple)``
This method is very useful, because the user will know what color it is, but not its name. So I searched on the  internet for an API that gives names to a given HEX/RGB/HSV color, so we can retrieve the name by our given colors.
So we send the HEX value of a given color and the API gives us a human-readable name.

