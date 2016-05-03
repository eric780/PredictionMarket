from scipy import stats
import numpy as np
import csv

filen = "allData"

filename = filen + "Analysis1" + ".csv"
with open (filename, 'wb') as f_out, open (filen+".csv", 'rb') as f_in:
	csvwriter = csv.writer(f_out)
	risk = 0
	while risk <= 1:
		csvreader = csv.reader(f_in)
		f_in.seek(0)
		final = []
		actual = []
		target = []
		for row in csvreader:
			if csvreader.line_num != 1:
				if (row[2] == row[4]) and (row[1] == '0' and row[3] == '0') and (row[5] == str(risk) or row[5] == '1'):
					final.append(row[10])
					actual.append(row[9])
					target.append(row[8])
		fin = np.array(map(float,final))
		act = np.array(map(float,actual))
		tar = np.array(map(float,target))
		if len(fin)>0:	
			if risk <= 1:
				csvwriter.writerow(["risk: "+ str(risk)])
				csvwriter.writerow(["nonMan vs Market"])
				csvwriter.writerow(["slope","intercept","r-value","p_value","std_err"])
				csvwriter.writerow(stats.linregress(fin,act))
				csvwriter.writerow([])
				csvwriter.writerow(final)
				csvwriter.writerow(actual)
				csvwriter.writerow([])
		risk += 0.25

