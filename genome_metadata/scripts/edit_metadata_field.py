import json
from checker_functions import check_completed, check_date_format

def edit_metadata_field(metadata_collection = "INCOMPLETE",
                       fasta_name = "INCOMPLETE",
                       field = "INCOMPLETE",
                       new_value = "INCOMPLETE"):
    
    """
        Parameters
        ----------
        metadata_collection : str
            The collection of metadata of the sequence
        fasta_name : str 
            The name of the FASTA file of the sequence
        field : str
            The field that will be changed/edited
        new_value : str
            The new value that will replace the old value of that field in the metadata
        
    """
    #check all metadata fields have been completed
    arguments = locals()
    check_completed(arguments)
    
    if field=="collection date":
        check_date_format(new_value)
    
    # Opening JSON file
    with open(metadata_collection, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
 
    #extract just the fasta file name, without the path
    fasta_file_name = fasta_name.split("/")[-1]
    #fetch : 
    json_object[fasta_file_name][field] = new_value
    
    with open(metadata_collection, "w") as outfile:
        #outfile.write(json_object)
        json.dump(json_object, outfile)
        
    print("In " + metadata_collection + " the metadata for " + fasta_name + " was modified. The field " + field + " was changed to " + new_value)
