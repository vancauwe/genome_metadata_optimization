import datetime
from NoneError import NoneError

def check_date_format(date): 
    
    """
        Parameters
        ----------
        date : str
            A date that we want to ensure is in YYYY-MM-DD format
        
        Raises
        ------
        ValueError
            If the date format is incorrect, it raises an error.
        
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        
    except ValueError:
        print('Your date format should be in the format YYYY-MM-DD.')
        raise ValueError("Date format incorrect.")

def check_completed(arguments):
    
    """
        Parameters
        ----------
        arguments : dictionary
            A dictionary where the key is the metadata field and the value is the user input
        
    """
    
    for ind, arg in arguments.items():
        if arg.__eq__("INCOMPLETE"):
            print('The following arguments are incomplete: ', ', '.join(ind for ind, arg in arguments.items() if arg.__eq__("INCOMPLETE")))
            raise NoneError("Some of the metadata fields are incomplete.")

           
def check_sequence_category(sequency_category): 
    
    """
        Parameters
        ----------
        sequence_category : str
            The category / standard of the sequence
        
    """
    
    category_list = ["migs_eu", "migs_ba", "migs_pl", "migs_vi", "migs_org", "mimarks_s", "mimarks_c", "mimag", "misag", "miuvig"]
    
    if sequency_category.__eq__("INCOMPLETE"):
            print('The sequence category information is missing.')
            raise NoneError("Some of the metadata fields are incomplete.")
    elif not sequency_category in category_list : 
        print('The sequence category does not exist.' )
        raise NoneError("The sequence category does not exist.")
                    