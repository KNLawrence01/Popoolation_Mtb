import sys
import re
import subprocess
import csv
import pandas as pd
if len(sys.argv) != 4:
    print("Usage: Auto_popoolation.py <csv file>  <Reference .fasta file> <Reference .bed file> <filter %>")
filename = sys.argv[1]
referenceBed= sys.argv[3]
referenceFasta = sys.argv[2]
filter = sys.argv[3]
commands = []
namesOfTsvs = []
with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] != "ID ":
            ancestor = row[1].strip() + ".ready.bam"
            passages = ""
            row = list(filter(None, row))
            print(row)
            for x in range(2,len(row)):
                passages = passages + " " + row[x] + ".ready.bam"
            command = "/home/mtopf/scripts/MT_run_popoolation.sh " + row[0] + " " + referenceBed + " " + referenceFasta + " " + ancestor + passages + "\n"
            namesOfTsvs.append(row[0] + ".tsv")
            commands.append(command)
for x in commands:
    subprocess.run(x.split(" "))
for x in namesOfTsvs:
    subprocess.run(["python3", "popoolation_MT_updated.py"], text=True, input= x + " " + filter)
bedInfo = []
with open(referenceBed, 'r') as bedfile:
    reader = csv.reader(bedfile, delimiter='\t')
    for row in reader:
        annot = row[9].split(";")
        product =  annot.pop()
        tupleToAdd = (int(row[1]), int(row[2]), product)
        bedInfo.append(tupleToAdd)
for x in namesOfTsvs:
  theCSV = pd.read_csv(x.replace(".csv",".tsv"))  
  



