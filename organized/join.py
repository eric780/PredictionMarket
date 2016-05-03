import numpy as np
import csv

files = ['sweep6','sweep7','sweep8','sweep9','sweep10','sweep11']

with open("allData.csv", 'wb') as f_out:
    
    csvwriter1 = csv.writer(f_out)

    csvwriter1.writerow(["Run","manSellers","Buyers","manBuyers","Sellers","riskAversion","maxRounds",
                        "Trades","manTarget","actualPrice","finalPrice"])
    
    for filen in files:
        filename = filen + "newtable.csv"
        with open(filename, 'rb') as f_in:
            csvreader = csv.reader(f_in)

            for row in csvreader:
                if csvreader.line_num != 1:
                    csvwriter1.writerow(row)
