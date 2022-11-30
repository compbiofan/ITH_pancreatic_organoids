from cgitb import small
from copy import deepcopy
import pandas as pd
from scipy.spatial import distance
import argparse

def main():
  print("hPT1_P3_P14\n")
  df1 = pd.read_csv("hPT1_P3_P14_merged_segs.tsv", sep= "\t")
  P3 = list(range(4, 9) )
  P14 = list(range(9, 15))

  P14_ = {}
  while(len(P14)):
    smallest = 9999999
    selected14 = -1
    selected3 = -1
    for p14 in P14:

      for p3 in P3:
        count = 0
        for index, row in df1.iterrows():
          if (df1.iat[index,p14] != df1.iat[index,p3]):
            count += df1.iat[index, 3] - df1.iat[index, 2]
        #print(df1.columns[p14], df1.columns[p3], count)
        count = count / 1000000
        #print(df1.columns[p14], "to", df1.columns[p3], count)
        if count <=  smallest:
          smallest = count
          selected14 = p14
          selected3 = p3
          #print("update smallest", smallest)
    P14_[selected14] = selected3
    P14.remove(selected14)
    P3.append(selected14)
    print(df1.columns[selected14], "is attached to", df1.columns[selected3], "\n")
  for key in P14_:
    lossIdx = []
    gainIdx = []
    loss = 0
    gain = 0
    for index, row in df1.iterrows():
      if (df1.iat[index,key] != df1.iat[index,P14_[key]]):
        if df1.iat[index,key] < df1.iat[index,P14_[key]]:
          loss += df1.iat[index, 3] - df1.iat[index, 2]
          lossIdx.append(index)
        else:
          gain += df1.iat[index, 3] - df1.iat[index, 2]
          gainIdx.append(index)
    print(df1.columns[key], "attached to", df1.columns[P14_[key]], "gain:", round(gain/1000000.0, 3), "loss:", round(loss/1000000.0, 3), "total:", round(gain/1000000.0, 3) + round(loss/1000000.0, 3))
    print("Gain segment")
    for idx in gainIdx:
      print(df1.iat[idx, 0], df1.iat[idx, 1], df1.iat[idx, 2], df1.iat[idx, 3])
    print("Loss segment")
    for idx in lossIdx:
      print(df1.iat[idx, 0], df1.iat[idx, 1], df1.iat[idx, 2], df1.iat[idx, 3])
    print()

  df2 = pd.read_csv("hPT2_P6_P16_merged_segs.tsv", sep= "\t")
  P3 = list(range(4, 9) )
  P14 = list(range(9, len(df2.columns)))

  P14_ = {}
  while(len(P14)):
    smallest = 9999999
    selected14 = -1
    selected3 = -1
    for p14 in P14:
      for p3 in P3:
        count = 0
        for index, row in df2.iterrows():
          if (df2.iat[index,p14] != df2.iat[index,p3]):
            count += df2.iat[index, 3] - df2.iat[index, 2]
        #print(df1.columns[p14], df1.columns[p3], count)
        count = count / 1000000
        #print(df2.columns[p14], "to", df2.columns[p3], count)
        if count <=  smallest:
          smallest = count
          selected14 = p14
          selected3 = p3
          #print("update smallest", smallest)
    P14_[selected14] = selected3
    P14.remove(selected14)
    P3.append(selected14)
    print(df2.columns[selected14], "is attached to", df2.columns[selected3], "\n")
  for key in P14_:
    lossIdx = []
    gainIdx = []
    loss = 0
    gain = 0
    for index, row in df2.iterrows():
      if (df2.iat[index,key] != df2.iat[index,P14_[key]]):
        if df2.iat[index,key] < df2.iat[index,P14_[key]]:
          loss += df2.iat[index, 3] - df2.iat[index, 2]
          lossIdx.append(index)
        else:
          gain += df2.iat[index, 3] - df2.iat[index, 2]
          gainIdx.append(index)
    print(df2.columns[key], "attached to", df2.columns[P14_[key]], "gain:", round(gain/1000000.0, 3), "loss:", round(loss/1000000.0, 3), "total:", round(gain/1000000.0, 3) + round(loss/1000000.0, 3))
    print("Gain segment")
    for idx in gainIdx:
      print(df2.iat[idx, 0], df2.iat[idx, 1], df2.iat[idx, 2], df2.iat[idx, 3])
    print("Loss segment")
    for idx in lossIdx:
      print(df2.iat[idx, 0], df2.iat[idx, 1], df2.iat[idx, 2], df2.iat[idx, 3])
    print()
if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument("--cnFile", type = str)
  args = parser.parse_args()
  main()
