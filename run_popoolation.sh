#! bin/bash
#####
#Script to run Popoolation. Written by Madison Youngblom and edited by Madeline Topf.
# Additional edits by Kadee N Lawrence
# Usage: run_popoolation.sh <strain_name> <path/to/ref> <path/to/bed> <bam1> ... <bamN>
#####
strain="$1"
ref="$2"
bed="$3"
bams="${@:4}"

# make mpileup file
echo "Creating mpileup file ..."
samtools mpileup -B -f ${ref} -o ${strain}.mpileup "${bams}"

# convert mpileup file to sync
echo "Converting mpilup file to sync file ..."
mpileup2sync.pl --input ${strain}.mpileup --output ${strain}.sync --fastq-type sanger --min-qual 20

# use python script to convert sync file to TSV
python3 popoolationSynctoTSV.py --bed ${bed} --min-count 5 --min-coverage 20 --min-freq 5 --output ${strain}_popoolation.tsv ${strain}.sync
