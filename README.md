# Receiver-Operating-characteristic
This is a small python script used to construct ROC curves and computing corresponding AUC (Area under the curve) - to determine accuracy of a binary classifier. 
<p>
This script was developed as a part of analyzing results for research paper - http://www.sciencedirect.com/science/article/pii/S0167404814000959
</p>

####Usage
python roc.py attacks.dat benign_traffic.dat \[roc_curve_plot_title\] <br/>
Sample input files are provided in '/samples' directory <br/>
Resulting files are provided in '/samples/results' directory

####Pre-requisites
Script uses gnuplot utility to construct 2D plot from results. Please install 'Gnuplot' and add it to your PATH variable to run it from command line.<br/>
Instructions can be found here - http://www.gnuplot.info/ 

####Concepts
In an ROC curve, we plot the true positive rate vs the false positive rate as the threshold varies over the range of scores.<br/>
<p>Lets say a binary classifier X is trained to detect entities of type A based certain characteristics of an entity. <br/>
If X is able to detect an unknown entity of type A - then that entity is a true positive <br/>
If X classifies an entity of type B incorrectly as an entity of type A - then that entity is a false postive <br/>
</p>
<p>
Computing true postive rate and false postive rate over a range of varying thresholds helps determine how accurately X is able correctly distinguish between entity of type A and entities of other types. <br/>
An ROC curve gives a visual indication about accuracy of detection of binary classifier X
</p>
<p>Area under the curve (AUC) is area under the ROC curve and is a numerical representation of accuracy of X. An AUC of 1.0 indicates that classifier X is able to perfectly distinguish between entities of type A and others. <br/>
While an AUC of 0.5 indicates that classifier X is no more effective than flipping a coin - ie - it is 50% likely to misclassify an unknown entity
</p>





