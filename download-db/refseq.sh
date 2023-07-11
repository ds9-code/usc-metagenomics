#!/bin/bash

#bacteria
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/assembly_summary.txt
awk -F "\t" '{print $20}' assembly_summary.txt > ftpdirpaths
awk 'BEGIN{FS=OFS="/";filesuffix="genomic.fna.gz"}{ftpdir=$0;asm=$10;file=asm"_"filesuffix;print ftpdir,file}' ftpdirpaths > ftpfilepaths

while read line;do wget $line;done<ftpfilepaths


mv ftpfilepaths ./metadata/
mv ftpdirpaths ./metadata/
mv assembly_summary.txt .metadata/