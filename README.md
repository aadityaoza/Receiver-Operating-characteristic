# Receiver-Operating-characteristic
This is a small python script used to construct ROC curves and computing corresponding AUC (Area under the curve) - to determine accuracy of a binary classifier. 
<p>
This script was developed as a part of analyzing results for research paper - http://www.sciencedirect.com/science/article/pii/S0167404814000959
</p>

####Usage
python roc.py attacks.dat benign_traffic.dat \[roc_curve_plot_title\]

####Pre-requisites
Script uses gnuplot utility to construct 2D plot from results. Please install 'Gnuplot' and add it to your PATH variable to run it from command line.<br/>
Instructions can be found here - http://www.gnuplot.info/ 



