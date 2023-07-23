# Read an fna file and print its contents

from Bio import SeqIO
import gzip

bacteria_dir = "data/bacteria_163_collection/salmonella_enterica_subsp_enterica_serovar_senftenberg_gca_001479095/dna/"

file_name = "Salmonella_enterica_subsp_enterica_serovar_senftenberg_gca_001479095.Salmonella_enterica_CVM_N31402-SQ_v1.0.dna.toplevel.fa.gz"

file_path = bacteria_dir + file_name
with gzip.open(file_path, "rt") as handle:
     for seq_record in SeqIO.parse(handle, "fasta"):
         print(seq_record.description)
         print(repr(seq_record.seq))
         print(len(seq_record))


#     for index, record in enumerate(SeqIO.parse(handle, "fasta")):      # read the records using SeqIO
#         if (index == 0):                                                # get the first record's description
#            print(record.description + '\n')
#handle.close()
