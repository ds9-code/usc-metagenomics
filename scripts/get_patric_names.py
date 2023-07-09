# Get the bacteria names rom the Patric genome dataset

# Import necessary packages
#from Bio import SeqIO
import os
import re

# Set up source directory and target file
source_dir = "/project/cr_055_883/ds_189/patric/"
target_file =  "/project/cr_055_883/ds_189/patric/patric_list.txt"

# For each file in the download directory, if it ends with .fna,
# open the file, read the first line and find the string in between the 
# square brackets [] - most of the time, this is the bacteria name
# It doesnt work for all the files, but we will extract the list and then fix issues

with open(target_file, "w") as f:
  for file in os.listdir(source_dir):
    if file.endswith(".fna"):
       file_path = source_dir + file
       # print(file_path)
       fline = open(file_path).readline().rstrip()
       organism = str(re.findall(r'\[.*?\]', fline))
       species = organism.split("|")[0]
       f.write(file + ',' + species + '\n')
f.close()

# Fasta files do not have good annotation, so we cannot extract
# the bacteria name information from the SeqIO record.

#for seq_record in SeqIO.parse(file_path, "fasta"):
    #print(seq_record.description)
    #print(repr(seq_record.seq))
    #print(len(seq_record))
