import json
from checker_functions import check_sequence_category, check_completed
from cleaner_functions import clean_seq_category, clean_argument_strings

def input_additional_metadata(sequence_category = "INCOMPLETE",
                              metadata_collection = "INCOMPLETE",
                              fasta_name = "INCOMPLETE",
                              assembly_quality = "INCOMPLETE",
                              assembly_software = "INCOMPLETE",
                              binning_parameters = "INCOMPLETE",
                              binning_software = "INCOMPLETE",
                              completeness_score = "INCOMPLETE",
                              completeness_software = "INCOMPLETE",
                              contamination_score = "INCOMPLETE",
                              isolation_and_growth_condition = "INCOMPLETE",
                              number_of_contigs = "INCOMPLETE",
                              number_of_replicons = "INCOMPLETE",
                              reference_for_biomaterial = "INCOMPLETE",
                              single_cell_lysis_approach = "INCOMPLETE",
                              source_of_uvigs = "INCOMPLETE",
                              sorting_technology = "INCOMPLETE",
                              target_gene = "INCOMPLETE",
                              taxonomic_identity_marker = "INCOMPLETE",
                              virus_enrichment_approach = "INCOMPLETE",
                              wga_amplification_approach = "INCOMPLETE"):
    
    """
        Parameters
        ----------
        sequence_category : str
            The category/standard of the sequence for which we want to add additional metadata
        metadata_collection : str
            The collection of metadata of the sequence
        fasta_name : str
            The name of the FASTA file of the sequence
        assembly_quality : str
            The assembly quality of the sequence
        assembly_software : str
            The assembly software of the sequence
        binning_parameters : str
            The binning parameters of the sequence
        binning_software : str
            The binning software of the sequence
        etc. etc. due to time constraints, I did not do the full docstring documentation
        
    """
    
    #extract arguments
    arguments = locals().copy()
    
    #clean sequence category name 
    sequence_category = clean_seq_category(sequence_category)
    check_sequence_category(sequence_category)
    
    # for the specific sequence category, subset to keep only informative arguments
    if sequence_category.__eq__("migs_eu"):
        to_extract = {"metadata_collection", "fasta_name",
                      "assembly_quality", "assembly_software", 
                      "isolation_and_growth_condition", "number_of_contigs"}
        arguments = {key: arguments[key] for key in arguments.keys() & to_extract}
    if sequence_category.__eq__("migs_ba"):
        to_extract = {"metadata_collection", "fasta_name",
                      "number_of_replicons", "reference_for_biomaterial", 
                      "assembly_quality", "assembly_software", 
                      "isolation_and_growth_condition", "number_of_contigs"}
        arguments = {key: arguments[key] for key in arguments.keys() & to_extract}
    if sequence_category.__eq__("migs_pl") | sequence_category.__eq__("migs_vi"):
        to_extract = {"metadata_collection", "fasta_name",
                      "propagation", "assembly_software", 
                      "isolation_and_growth_condition"}
        arguments = {key: arguments[key] for key in arguments.keys() & to_extract}
    if sequence_category.__eq__("migs_org"):
        to_extract = {"metadata_collection", "fasta_name",
                      "assembly_software", "isolation_and_growth_condition"}
        arguments = {key: arguments[key] for key in arguments.keys() & to_extract}
    if sequence_category.__eq__("mimarks_s"):
        to_extract = {"metadata_collection", "fasta_name",
                      "target_gene"}
        arguments = {key: arguments[key] for key in arguments.keys() & to_extract}
    if sequence_category.__eq__("mimarks_c"):
        to_extract = {"metadata_collection", "fasta_name",
                      "isolation_and_growth_condition", "target_gene"}
        arguments = {key: arguments[key] for key in arguments.keys() & to_extract}
    if sequence_category.__eq__("misag"):
        to_extract = {"metadata_collection", "fasta_name",
                      "taxonomic_identity_marker",
                      "wga_amplification_approach", "sorting_technology", "single_cell_lysis_approach"
                    "completeness_score", "completeness_software", "contamination_score",
                     "assembly_quality", "assembly_software"}
        arguments = {key: arguments[key] for key in arguments.keys() & to_extract}    
    if sequence_category.__eq__("mimag"):
        to_extract = {"metadata_collection", "fasta_name",
                      "taxonomic_identity_marker",
                      "binning_parameters", "binning_software",
                    "completeness_score", "completeness_software", "contamination_score",
                     "assembly_quality", "assembly_software"}
        arguments = {key: arguments[key] for key in arguments.keys() & to_extract}
    if sequence_category.__eq__("miuvig"):
        to_extract = {"metadata_collection", "fasta_name",
                      "virus_enrichment_approach", "source_of_uvigs"}
        arguments = {key: arguments[key] for key in arguments.keys() & to_extract}
    
    
    #check all metadata fields have been completed
    check_completed(arguments)
        
    
    #clean all the input strings
    #remove metadata_collection and fasta_name from arguments
    arguments.pop("metadata_collection")
    arguments.pop("fasta_name")
    arguments = clean_argument_strings(arguments)
    
    fasta_file_name = fasta_name.split("/")[-1]
    #read in and add to metadata collection
    # Opening metadata collection
    with open(metadata_collection, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
     
    # edit existing entry
    temp_dict = json_object[fasta_file_name] 
    #add each new metadata info
    for key, val in arguments.items():
        temp_dict[key] = val
    json_object[fasta_file_name] = temp_dict
    
    with open(metadata_collection, "w") as outfile:
        #outfile.write(json_object)
        json.dump(json_object, outfile)
        
    
    
    
    