#!/bin/bash
#Usage: snpEff.sh <_withAnnot.csv>

# Run R script to generate VCF file from CSV input
Rscript poolER/csvToVCF.R $1

# Use the output file of the R script as input for the Java script
# Assuming $f contains a filename with .csv extension

file="${1%.csv}"
output="${file/_popoolation_withAnnot/_snpEff.tsv}"

java -Xmx8g -jar /opt/PepPrograms/snpEff_v5.0/snpEff.jar JNFY15 "$file.vcf" > $output


#run R script to combine 
Rscript poolER/combine.R $1 $output
