from re import A
import statistics
import pandas as pd
  
sr = pd.Series([12,45,23,15,21,3,8])

mean = sr.mean()
median = sr.median()
mode = sr.mode()
range1 = sr.max() - sr.min(); 
stdeviation = sr.std(axis=0,skipna=True)

print(mean)
print(median)
print(mode)
print(range1)
print(stdeviation)
print("Variance of sample set is % s"
      %(statistics.variance(sr)))
