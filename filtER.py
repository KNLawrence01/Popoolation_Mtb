##Script to filter output from poolER to desired frequency and annotate variants in a high throughput manner. 
#Written by Mohamed Mohamed & Madeline Topf; edited by Madison Youngblom.

import csv
import sys
import subprocess
if len(sys.argv) != 4:
    print("Usage: filtER.py <Reference .bed file> <tsv output from poolER> <filter %>")
    sys.exit()
referenceBed = sys.argv[1]
namesOfTsvs = sys.argv[2]
namesOfTsvs = namesOfTsvs.split(",")
filter = sys.argv[3]
bedInfo = []


for x in namesOfTsvs:
    subprocess.run(["python3", "poolER/popoolationParser.py", x,  filter])

with open(referenceBed, 'r') as bedfile:
    reader = csv.reader(bedfile, delimiter='\t')
    for row in reader:
        if "header" not in row[0]:
            annot = row[9].split(";")
            product =  annot.pop()
            tupleToAdd = (int(row[1]), int(row[2]), product)
            bedInfo.append(tupleToAdd)

for x in namesOfTsvs:
   with open(x.replace(".tsv",".csv"), 'r') as file:
        reader_obj = csv.reader(file) #read the current csv file
        with open(x.replace(".tsv","") + "_withAnnot.csv", mode="w") as new_file:
            writer_obj = csv.writer(new_file) # Writes to the new CSV file 
            for row in reader_obj:
                if row[0] != "trajectory":
                    lengthofRow = len(row)
                    position = int(row[(lengthofRow-1)])
                    # added a variable for the annotation
                    annot = ""
                    # search through bedInfo to find if this position is within an annotated gene
                    for y in bedInfo:
                        if (y[0] <= position) and (position <= y[1]):
                            annot = y[2]
                    # if no annotation has been found by searching through bedInfo (above), then the annotation is NA
                    # ie if annot is still equal to "" and hasnt been set to a gene, set it instead to NA
                    if annot == "":
                        annot = "NA"
                    # whatever the annotation is, append it to the end of the row
                    row.append(annot)
                    # write the new row to the output file
                    writer_obj.writerow(row)
                else:
                    row.append("annot")
                    writer_obj.writerow(row)

