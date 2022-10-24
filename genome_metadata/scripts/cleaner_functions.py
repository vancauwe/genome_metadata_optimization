from checker_functions import check_completed

def clean_seq_category(seq_category="INCOMPLETE"):
    
    """
        Parameters
        ----------
        sequence_category : str
            The category/standard of the sequence for which we want to add additional metadata
    """
    
    arguments = locals()
    check_completed(arguments)
    seq_category = seq_category.lower().replace(' ','_').replace('-','_')
    
    return(seq_category)

def clean_argument_strings(arguments):
    
    """
        Parameters
        ----------
        arguments : dictionary
            A dictionary where the keys are the names of the mandatory variables of the metadata 
            and the values are the values entered by the user    
    """
    
    arguments = dict([(ind, arg.lower().replace(' ','_')) for ind, arg in arguments.items()])
    return(arguments)    