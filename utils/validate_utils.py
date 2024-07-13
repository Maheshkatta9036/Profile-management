"""This file validates the user details"""

from constants import *
from logger import *
def is_valid_mobile(mobile):
    '''
    This functions validate's if it is validate mobile number
    param : mobile : int
    return : bool
    '''
    if isinstance(mobile, int):
        mobile = str(mobile) # converting mobile to str
        if len(mobile) == 12:
            if int(mobile) in EXCLUDED_NUMBERS:
                return True
            if mobile[:2] in VALID_COUNTRY_CODE:
                logging.debug(f'Mobile Number verified Successfully')
                return True
            else:
                raise ValueError(f'Country code is not valid :-{mobile[:2]}')
        else:
            raise ValueError(f'Invalid Mobile Number length :- {len(mobile)}')


def is_valid_name(name):
    '''
    This function validate's if the name is valid or not
    param : name : str
    return : bool
    '''
    if isinstance(name, str):
        clean_name = name.replace('.', '').replace('_', '').replace(' ', '')
        if len(clean_name) > 3:
            if clean_name.isalpha():
                logging.debug(f'Name verified successfully')
                return True
            else:
                raise ValueError(f'User name must be alphabetic after removing special characters: {name}')
        else:
            raise ValueError(f'User name cannot be {len(clean_name)} characters, user: {name}')
    else:
        raise ValueError(f'Name should be a string, received: {type(name).__name__}')

