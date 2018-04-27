import pandas as pd
import csv, sys


csvfile = sys.argv[1]
odf = pd.read_csv(csvfile)
del odf['Unnamed: 0']
print(odf)
s = csvfile.replace(".csv","",1) + "_result.csv"
odf.to_csv(s, index=None)
