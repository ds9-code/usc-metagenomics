# Get the bacteria names from the ensemblgenomes list

import os

data_dir = '/project/cr_055_883/ds_189/ensembl/data/'
target_file = '/project/cr_055_883/ds_189/ensembl/ensembl_list.csv'

with open(target_file, "w") as f:
     for collection_name in os.listdir(data_dir):
         bacteria_dir = os.listdir(os.path.join(data_dir, collection_name))
         for bac_dir in bacteria_dir:
             f.write(collection_name + ',' + bac_dir + '\n')

f.close()

#print(len(final_ensemble_list))
