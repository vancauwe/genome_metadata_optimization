import json
from checker_functions import check_completed

def extract_specific_metadata(metadata_collection = "INCOMPLETE",
                              field = 'INCOMPLETE',
                              value = 'INCOMPLETE'):
    
    """
        Parameters
        ----------
        metadata_collection : str
            The collection of metadata of the sequence
        field : str
            The field of interest to extract/select relevant metadatas in the collection
        value : str
            The value the field should have as a condition to be extracted/selected
        
    """
    arguments = locals().copy()
    check_completed(arguments)
    
    with open(metadata_collection, 'r') as openfile:
                # Reading from json file
                json_object = json.load(openfile)

    extraction = {}     
    #iterate over each fasta file's metadata
    for fasta, metadata in json_object.items():
        #keep the fast file info if its field (key) is equal to the desired value
        if metadata[field]==value:
            extraction[fasta] = json_object[fasta]

    return(extraction)