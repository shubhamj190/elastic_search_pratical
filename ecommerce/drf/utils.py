class convert_to_dot_notation(dict):

    __getattr__ = dict.get
    __setattr__ = dict.__setattr__
    __delattr__ = dict.__delattr__