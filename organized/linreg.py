from scipy import stats
import numpy as np
import csv

files = ['manBoth', 'manBuyer', 'manNone','manSeller']

for filen in files:
	filename = filen + "LinReg" + ".csv"
	with open (filename, 'wb') as f_out, open (filen+".csv", 'rb') as f_in:
		csvwriter = csv.writer(f_out)
		csvreader = csv.reader(f_in)
		final = []
		actual = []
		target = []
		for row in csvreader:
			if csvreader.line_num != 1:
				final.append(row[10])
				actual.append(row[9])
				target.append(row[8])
		fin = np.array(map(float,final))
		act = np.array(map(float,actual))
		tar = np.array(map(float,target))
		
		csvwriter.writerow(["slope","intercept","r-value","p_value","std_err"])
		csvwriter.writerow(stats.linregress(act,fin))
		if filen != 'manNone':
			csvwriter.writerow(stats.linregress(tar,fin))
