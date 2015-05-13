#!/usr/bin/python -tt

import sys
import subprocess
import math

def read_data(filename):
  f = open(filename , 'r')
  lines = f.readlines()

  scores = []
  for line in lines:
    scores.append((line.split())[1])

  f.close()
  return scores

def calc_tp(scores,threshold):
  count = 0 
  for score in scores:
    if float(score) <= float(threshold):
      count = count + 1
  return float(count)/float(len(scores))

# The main() function
def main():
  
  scores1 = [] ## Array to store scores of attack traffic
  scores2 = [] ## Array to store scores of benign traffic

  if(len(sys.argv)!= 4):
    print 'Incorrect number of arguments'
    print 'Correct input - python generateROC.py attackFile.dat benignFile.dat  ROC_plot_title'
    sys.exit()

  print(sys.argv)
  scores1 = read_data(sys.argv[1]) ## Read attack scores
  scores2 = read_data(sys.argv[2]) ## Read benign traffic scores

  thresholds = []
  # Thresholds
  for score in scores1:
    thresholds.append(float(score))

  for score in scores2:
    thresholds.append(float(score))

  #thresholds = []
  #for i ,v in enumerate(thresholds_all):
  #  if(i == 0 or i == (len(thresholds_all)-1) or i % 5000 == 0):
  #    thresholds.append(v)

  
  thresholds = sorted(thresholds)
  #thresholds.append((sorted(thresholds_all))[-1])

  # Extract filenames from command line arguments
  arg1 = sys.argv[1].split('.dat')
  arg2 = sys.argv[2].split('.dat')

  # Results file for writing false positive and true positive rate
  f =open('roc.dat' , 'w')

  # Calculate true positives and false positives for each threshold
  # and write it in the roc results file
  for threshold in thresholds:
    fp_rate = calc_tp(scores1,threshold)
    tp_rate = calc_tp(scores2,threshold)
    f.write(str(fp_rate)+'\t'+str(tp_rate)+'\n')
  f.close()

  # Command line interface to Gnuplot
  proc = subprocess.Popen(['gnuplot','-p'],shell=True,stdin=subprocess.PIPE)

  # plot Box plot using 2 input files
  proc.stdin.write('reset\n')
  proc.stdin.write('set terminal png\n')
  proc.stdin.write('set xlabel "Packets"\n')
  proc.stdin.write('set ylabel "Scores"\n')
  proc.stdin.write('set output \'BOX_'+arg1[0]+'.png\'\n')
  proc.stdin.write('set title \''+sys.argv[3]+'\'\n')
  proc.stdin.write('plot "'+sys.argv[1]+'" title "Attack Traffic" , "'+sys.argv[2]+'" title "Benign Traffic"\n')
  
  

  # plot ROC curve using generated results file
  proc.stdin.write('reset\n')
  proc.stdin.write('set terminal png\n') 
  proc.stdin.write('set xlabel "False positive rate"\n')
  proc.stdin.write('set ylabel "True positive rate"\n')
  proc.stdin.write('set xrange [-0.025:1.025]\n')
  proc.stdin.write('set yrange [0:1.025]\n')
  proc.stdin.write('set output \'ROC_'+arg1[0]+'.png\'\n')
  proc.stdin.write('set xtics 0.1\n')
  proc.stdin.write('set ytics 0.1\n')
  proc.stdin.write('set key off\n')
  proc.stdin.write('set grid\n')
  proc.stdin.write('set title "'+sys.argv[3]+'"\n')
  proc.stdin.write('plot \'roc.dat\' using 1:2 with lines\n')
  proc.stdin.write('quit')

  # Calculate Area under the curve (AUC)
  f =open('roc.dat' , 'r')
  lines = f.readlines()
  area = 0

    # Write AUC to file
  f2 =open('auc.dat' , 'w')

  x_prev = float(lines[0].split()[0])
  y_prev = float(lines[0].split()[1])
  flag = 1
  
  for line in lines[1:]:
    x_score = float(line.split()[0])
    y_score = float(line.split()[1])

    if x_score > 0.10 and flag == 1:
      f2.write("The partial area under the curve = "+str(area +((y_prev)*(0.1 - x_prev)))+"\n")
      flag = 0
      
    area += ((y_score+y_prev)/2)*(x_score-x_prev)
    x_prev = x_score
    y_prev = y_score

  print 'The area under the curve =' ,str(area)

  # Calculate standard error
  q1 = area/(2-area)
  q2 = 2*area*area/(1+area)
  
  error = ((area*(1-area)) + ((len(scores2)-1)*(q1-(area*area))) + ((len(scores1)-1)*(q2 - (area*area))))/(len(scores1)*len(scores2))
  error = math.sqrt(error)
  
  f.close()


  f2.write(str(area)+'\t'+str(error))
  f2.close()

  sys.exit()
  
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
