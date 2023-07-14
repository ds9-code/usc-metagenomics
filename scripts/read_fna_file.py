# Read an fna file and print its contents

from Bio import SeqIO
import gzip

filename = "data/GCF_951803545.1_ARM46_genomic.fna.gz"
with gzip.open(filename, "rt") as handle:
     for seq_record in SeqIO.parse(handle, "fasta"):
         print(seq_record.description)
         print(repr(seq_record.seq))
         print(len(seq_record))
