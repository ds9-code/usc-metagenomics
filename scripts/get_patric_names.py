# Get the bacteria names rom the Patric dataset

from Bio import SeqIO
import os

source_dir = "/project/cr_055_883/dsreedhar/code/"
source_file = "/project/cr_055_883/dsreedhar/patric/dedupe_genome_list"
target_file =  "/project/cr_055_883/dsreedhar/patric/patric_list.txt"

with open(target_file, "w") as f:            # Open target file for write
    with open(source_file, "rt") as file:
          for filename in file:
              file_path = source_dir + filename.rstrip() + '.fna'         # construct the full file path with file name
              with open(file_path, "rt") as handle:                                  # and then use gzip to unzip and open it
                   for index, record in enumerate(SeqIO.parse(handle, "fasta")):      # read the records using SeqIO
                       if (index == 0):                                                # get the first record's description
                           f.write(filename.rstrip() + '|' + record.description + '\n')
              handle.close()                                                  # Close the actual fna file after getting the bacteria name
    file.close()                                                              # Close the source file after reading
f.close()                                                                     # Close the target file after writing
