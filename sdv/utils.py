import importlib
import pickle


def format_table_meta(table_meta):
    """ reformats table meta to turn fields into dictionary """
    new_fields = {}
    for field in table_meta['fields']:
        field_name = field['name']
        new_fields[field_name] = field
    table_meta['fields'] = new_fields
    return table_meta


def load_model(filename):
    """ Loads model from filename
    Args:
        filename (string): path of file to load
    """
    with open(filename, 'rb') as input:
        return pickle.load(input)


def import_object(object_name):
    """Import an object from its Fully Qualified Name."""
    package, name = object_name.rsplit('.', 1)
    return getattr(importlib.import_module(package), name)
