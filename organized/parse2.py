import numpy as np
import csv

# files = ['sweep6', 'sweep7','sweep8', 'sweep9']
files = ['sweep10','sweep11']

for filen in files:
    filename = filen + "new"
    with open(filename+"table.csv", 'wb') as f_out:
        csvwriter = csv.writer(f_out)
        csvwriter.writerow(["Run","manSellers","Buyers","manBuyers","Sellers","riskAversion","maxRounds",
                            "Trades","manTarget","actualPrice","finalPrice"])
        col = 1
        # while col < (640*4):
        while col < (320*4):
            with open(filename+".csv", 'rb') as f_in: 
                csvreader = csv.reader(f_in)
                stuff = []
                for row in csvreader:
                    if csvreader.line_num <= 7 :
                        stuff.append(row[col])
                    if csvreader.line_num == 11:
                        stuff.append(row[col])
                        stuff.append(row[col+1])
                        stuff.append(row[col+2])
                        stuff.append(row[col+3])
                # print stuff
                csvwriter.writerow(stuff)
                col += 4

