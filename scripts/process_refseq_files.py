# Get the bacteria names rom the NCBI RefSeq dataset

from Bio import SeqIO
import gzip
import os

source_dir = "/project/cr_055_883/ds_189/ncbi-refseq/"
target_file =  "/project/cr_055_883/ds_189/ncbi-refseq/refseq_list.txt"

# We open each fna.gz file with SeqIO.
# Each file has multiple records for the same bacteria
# Since we only need the bacteria name, we can just take the 
# record description from the first record, which has the bacteria name
# all other records will have the same bacteria name in the file

with open(target_file, "w") as f:            # Open target file for write
  for file in os.listdir(source_dir):        # For each file in the source directory
    if file.endswith(".fna.gz"):             # that ends in fna.gz,
       file_path = source_dir + file         # construct the full file path with file name

       with gzip.open(file_path, "rt") as handle:       # and then use gzip to unzip and open it
           for index, record in enumerate(SeqIO.parse(handle, "fasta")):      # read the records using SeqIO
              if (index == 0):                                                # get the first record's description
                 f.write(file + '|' + record.description + '\n')
       handle.close()
f.close()                                                # Close the target file after writing
