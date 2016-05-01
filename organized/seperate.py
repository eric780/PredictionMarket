import numpy as np
import csv

files = ['sweep6','sweep7','sweep8','sweep9','sweep10','sweep11']

with open("manNone.csv", 'wb') as no_man,open("manBuyer.csv", 'wb') as manb,open("manSeller.csv", 'wb') as mans,open("manBoth.csv", 'wb') as man:
    
    csvwriter1 = csv.writer(no_man)
    csvwriter2 = csv.writer(manb)
    csvwriter3 = csv.writer(mans)
    csvwriter4 = csv.writer(man)

    csvwriter1.writerow(["Run","manSellers","Buyers","manBuyers","Sellers","riskAversion","maxRounds",
                        "Trades","manTarget","actualPrice","finalPrice"])
    csvwriter2.writerow(["Run","manSellers","Buyers","manBuyers","Sellers","riskAversion","maxRounds",
                        "Trades","manTarget","actualPrice","finalPrice"])
    csvwriter3.writerow(["Run","manSellers","Buyers","manBuyers","Sellers","riskAversion","maxRounds",
                        "Trades","manTarget","actualPrice","finalPrice"])
    csvwriter4.writerow(["Run","manSellers","Buyers","manBuyers","Sellers","riskAversion","maxRounds",
                        "Trades","manTarget","actualPrice","finalPrice"])
    
    for filen in files:
        filename = filen + "newtable.csv"
        with open(filename, 'rb') as f_in:
            csvreader = csv.reader(f_in)

            for row in csvreader:
                if row[1] == '0' and row[3] == '0':
                    csvwriter1.writerow(row)
                elif row[1] == '0':
                    csvwriter2.writerow(row)
                elif row[3] == '0':
                    csvwriter3.writerow(row)
                elif csvreader.line_num != 1:
                    csvwriter4.writerow(row)
