# Read all ensembl fna files and save the bacteria metgenomic information
import os
from Bio import SeqIO
import gzip

data_dir = '/project/cr_055_883/ds_189/ensembl/data/'
target_file = data_dir + 'ensembl_metagenomics.csv'

with open(target_file, "w") as f:
     for collection_name in os.listdir(data_dir):
         bacteria_dir = os.listdir(os.path.join(data_dir, collection_name))
         for bac_dir in bacteria_dir:
             fasta_dir = data_dir + collection_name + '/' + bac_dir + '/dna/'

             for fasta_file in os.listdir(fasta_dir):
                 name, ext = os.path.splitext(fasta_file)
                 if ext == '.gz':
                    ff = fasta_dir + fasta_file
                    with gzip.open(ff, "rt") as handle:
                         for seq_record in SeqIO.parse(handle, "fasta"):
                             f.write(collection_name + '||' + bac_dir + '||' + fasta_file + '||' + seq_record.description + '||' + repr(seq_record.seq) + '||' + str(len(seq_record)) + '\n')
                 handle.close()
f.close()

