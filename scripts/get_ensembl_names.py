# Get the bacteria names from the ensemblgenomes list

import os

base_dir = '/project/cr_055_883/ds_189/'
ensemble_dir = base_dir + 'ftp.ensemblgenomes.org/pub/bacteria/release-43/fasta'
bacteria_dirs = os.listdir(ensemble_dir)
ensemble_list = []

target_file = base_dir + 'ensembl/ensembl_list.txt'

for bac_dir in bacteria_dirs:
  bac_dir_path = ensemble_dir + '/' + bac_dir
  bacteria_list = os.listdir(bac_dir_path)
  ensemble_list.extend(bacteria_list)

final_ensemble_list = list(set(ensemble_list))

with open(target_file, "w") as f:
     for i in range(len(final_ensemble_list)):
        item = final_ensemble_list[i] + "\n"
        f.write(item)

f.close()

#print(len(final_ensemble_list))
