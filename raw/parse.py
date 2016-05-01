import numpy as np
import csv

files = ['sweep10', 'sweep11', 'sweep6', 'sweep7',
'sweep8', 'sweep9']

for filename in files:
    with open(filename+".csv", 'rb') as f_in, open(filename+"new.csv", 'wb') as f_out:
        csvreader = csv.reader(f_in)
        csvwriter = csv.writer(f_out)
        for row in csvreader:
            if csvreader.line_num >= 7:
                csvwriter.writerow(row)
