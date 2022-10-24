import json

def list_metadata_collection(metadata_collection):
    
    """
        Parameters
        ----------
        metadata_collection : str
            The collection of metadata of the sequence
    """
    keys = []

    with open(metadata_collection, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)

    for key, var in json_object.items():
        keys.append(key)

    print(keys)
    
    return(keys)