from scipy import stats
import numpy as np
import csv

filen = "allData"

risk = 0.75

filename = filen + "Analysis4" + ".csv"
with open (filename, 'wb') as f_out, open (filen+".csv", 'rb') as f_in:
    csvwriter = csv.writer(f_out)

    csvreader = csv.reader(f_in)
    f_in.seek(0)
    final = []
    actual = []
    target = []
    for row in csvreader:
        if csvreader.line_num != 1:
            if (row[5] == str(risk)) and (((row[1] == row[3] == '500') and (row[2] == row[4] == '498')) or ((row[1] == row[3] == '1000') and (row[2] == row[4] == '999'))):
                final.append(row[10])
                actual.append(row[9])
                target.append(row[8])
    fin = np.array(map(float,final))
    act = np.array(map(float,actual))
    tar = np.array(map(float,target))
    if len(fin)>0:  
        csvwriter.writerow(["reg: " + 'equal' + ", man: " + 'equal'])
        csvwriter.writerow(["final vs target"])
        csvwriter.writerow(["slope","intercept","r-value","p_value","std_err"])
        csvwriter.writerow(stats.linregress(fin,tar))
        csvwriter.writerow([])
        csvwriter.writerow(final)
        csvwriter.writerow(target)
        csvwriter.writerow([])

