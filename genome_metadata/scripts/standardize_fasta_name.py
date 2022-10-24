import json
import os
from checker_functions import check_completed

def standardize_fasta_name(metadata_collection,
                           fasta_name):
    
    """
        Parameters
        ----------
        metadata_collection : str
            The collection of metadata of the sequence
        fasta_name : str
            The name of the FASTA file of the sequence
        
    """


    #check all metadata fields have been completed
    #important to have here because the function can be used stand-alone to rename a FASTA file
    arguments = locals()
    check_completed(arguments)
    
    # Opening JSON file
    with open(metadata_collection, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
 
    #extract just the fasta file name, without the path
    fasta_file_name = fasta_name.split("/")[-1]
    #fetch : 
    collection_date = json_object[fasta_file_name]['collection date'].replace('-','_')
    taxonomy_ID = json_object[fasta_file_name]['taxonomy ID'].lower()
    sample_name = json_object[fasta_file_name]['sample name'].lower().replace(' ','_').replace('-','_')
    sequencing_method = json_object[fasta_file_name]['sequencing method'].lower().replace(' ','_').replace('-','_')
    project_name = json_object[fasta_file_name]['project name'].lower().replace(' ','_').replace('-','_')
                    
    path = "genome_metadata/FASTA_files/"
    standardized_name = path + collection_date + "_" + taxonomy_ID + "_" + sample_name + "_" + sequencing_method + ".fasta"
     
    print(f"OLD Name: {fasta_name}")
    os.rename(fasta_name, standardized_name)
    print(f"NEW Standardized Name: {standardized_name}")
    
    standardized_name = standardized_name.split("/")[-1]

    print("New name entered into the associated metadata collection.")
    #if you do not return the name then the standardization is being done on its own
    json_object[standardized_name] = json_object[fasta_file_name]
    del json_object[fasta_file_name]
    with open(metadata_collection, "w") as outfile:
        json.dump(json_object, outfile)

