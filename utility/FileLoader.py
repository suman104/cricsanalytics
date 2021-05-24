import yaml
from yaml import FullLoader, SafeLoader



def load(stream, Loader=None):
    """
    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    """
    if Loader is None:
        yaml.load_warning('load')
        Loader = FullLoader

    loader = Loader(stream)
    try:
        return loader.get_single_data()
    finally:
        loader.dispose()

def safe_load(stream):
    """
    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    Resolve only basic YAML tags. This is known
    to be safe for untrusted input.
    """
    return load(stream, SafeLoader)