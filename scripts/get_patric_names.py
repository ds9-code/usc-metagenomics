# Get the bacteria names rom the Patic dataset

#from Bio import SeqIO
import os
import re

patric_dir = "/project/cr_055_883/dsreedhar/code/"
target_file =  "/project/cr_055_883/dsreedhar/patric/patric_list.txt"

with open(target_file, "w") as f:
  for file in os.listdir(patric_dir):
    if file.endswith(".fna"):
       file_path = patric_dir + file
       # print(file_path)
       fline=open(file_path).readline().rstrip()
       organism = str(re.findall(r'\[.*?\]', fline))
       species = organism.split("|")[0]
       f.write(file + ',' + species + '\n')
f.close()

#for seq_record in SeqIO.parse(file_path, "fasta"):
    #print(seq_record.description)
    #print(repr(seq_record.seq))
    #print(len(seq_record))
