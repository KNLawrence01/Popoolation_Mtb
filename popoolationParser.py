import sys
import csv
tsv = input("Name of .tsv file:")
minimumFreq = input("Minimum Frequency Change: ")
tsv_file = open(tsv)
read_tsv = csv.reader(tsv_file, delimiter="\t")
filename = tsv.replace('.tsv', "") + ".csv"
passages = []
tCount = 1
rowsToAdd = []
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in read_tsv:
        try:
            if (row[0] == "pos"):
                passages = row[3:]
                csvwriter.writerow(['trajectory'] + passages + ['pos'])
            elif ((abs(int(row[len(passages) + 2]) - int(row[3])) >= int(minimumFreq))):
                rowsToAdd.append(row)
        except:
            pass
        rowsToAddCopy = rowsToAdd.copy()
    for x in rowsToAddCopy:
        thearray = x[3:]
        csvwriter.writerow(["t" + str(tCount)] + thearray + [x[0]])
        tCount += 1
