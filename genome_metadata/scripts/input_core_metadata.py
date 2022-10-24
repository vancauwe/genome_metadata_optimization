import json
from checker_functions import check_date_format, check_completed
from cleaner_functions import clean_argument_strings
from standardize_fasta_name import standardize_fasta_name

def input_core_metadata(metadata_collection = "INCOMPLETE",
                    fasta_name = "INCOMPLETE",
                    project_name = "INCOMPLETE",
                    sample_name = "INCOMPLETE",
                    taxonomy_ID = "INCOMPLETE",
                    sequencing_method = "INCOMPLETE",
                    collection_date = "INCOMPLETE",
                    geographic_latitude = "INCOMPLETE",
                    geographic_longitude = "INCOMPLETE",
                    geographic_location = "INCOMPLETE",
                    geographic_country = "INCOMPLETE",
                    environment = "INCOMPLETE"):
    
    """
        Parameters
        ----------
        metadata_collection : str
            The collection of metadata of the sequence
        fasta_name : str
            The name of the FASTA file of the sequence
        project_name : str
            The name of the project within which the sequence is being studied
        sample_name : str
            The sequence's sample name
        taxonomy_ID : str
            The taxonomy of the sequence
        sequencing_method : str
            The sequencing method use to obtain the sequence
        collection date : str
            The day the sample was collected (format should be YYYY-MM-DD)
        etc. etc. due to time constraints, I did not do the full docstring documentation
        
    """
    
    #check all metadata fields have been completed
    arguments = locals().copy()
    check_completed(arguments)
    
    #check date format
    check_date_format(collection_date)
    
    
    #clean all the input strings
    #remove metadata_collection and fasta_name from arguments
    arguments.pop("metadata_collection")
    arguments.pop("fasta_name")
    arguments = clean_argument_strings(arguments)
    
    #read in and add to metadata collection
    # Opening metadata collection
    with open(metadata_collection, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    
    fasta_name_key = fasta_name.split("/")[-1]
    # add new entry
    json_object[fasta_name_key] = {
            "project name": arguments["project_name"],
            "sample name": arguments["sample_name"],
            "taxonomy ID": arguments["taxonomy_ID"],
            "sequencing method": arguments["sequencing_method"],
            "collection date": arguments["collection_date"],
            "geographic latitude": arguments["geographic_latitude"],
            "geographic longitude": arguments["geographic_longitude"],
            "geographic location": arguments["geographic_location"],
            "geographic country": arguments["geographic_country"],
            "environment": arguments["environment"]
       }
    
    with open(metadata_collection, "w") as outfile:
        #outfile.write(json_object)
        json.dump(json_object, outfile)

    #standardize name of the metadata file
    standardized_fasta_name = standardize_fasta_name(metadata_collection, fasta_name)
    
        
    
    
    
    