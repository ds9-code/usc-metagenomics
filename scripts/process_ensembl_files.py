# Get the bacteria names from the ensemblgenomes list

# Import required packages
import os

# Setup directory paths to read from and target file name to write to
base_dir = '/project/cr_055_883/ds_189/'
ensemble_dir = base_dir + 'ftp.ensemblgenomes.org/pub/bacteria/release-43/fasta'
target_file = base_dir + 'ensembl/ensembl_list.txt'

# Since bacteria names are stored in "collections", we get those directories and store them in a Python list
collection_dirs = os.listdir(ensemble_dir)

# Create an empty list to store the bacteria names
ensemble_list = []

# For each bacteria sub-directory under the collection directory, 
# get the name and store it in our list.
# Loop through all the collections, adding the bacteria names to our main list

for bac_dir in collection_dirs:
  bac_dir_path = ensemble_dir + '/' + bac_dir
  bacteria_list = os.listdir(bac_dir_path)
  ensemble_list.extend(bacteria_list)

# Use the "set" command to convert the bacteria list into a dictionary object, which removes any duplicates
# Then convert it back to a list object
final_ensemble_list = list(set(ensemble_list))

# Loop through our final list and write each bacteria name to a text file.
with open(target_file, "w") as f:
     for i in range(len(final_ensemble_list)):
        item = final_ensemble_list[i] + "\n"
        f.write(item)

# Close the file after writing
f.close()

#print(len(final_ensemble_list))
