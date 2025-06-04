Character = str

class InvalidIndexError(Exception):
    pass

class CharacterTypeError(Exception):
    pass

def is_character(element) -> bool:
    return isinstance(element, str) and len(element) == 1