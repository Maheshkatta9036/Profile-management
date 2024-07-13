from ..logs.logger import *
import re


def authenticate_user(name, users, admins):
    '''
    This function take's name, users and admins as argument and validates
    param : {name : str, users : dict, admins : dict}
    return : bool
    '''
    logging.debug(f"Authenticating for the user :- {name}")
    if (name in users) or (name in admins):
        logging.debug(f"User Authenticated succesfully")
        return True
    return False


def is_valid_user_name(user_name, users, admins):
    '''
    This function take's user_name as argument and validate's 
    param : {name : str, users : dict, admins : dict}
    retunr : bool 
    '''
    if (user_name in users)  or (user_name in admins):
        suggestions = [f"{user_name}{i}{user_name[:1]}" for i in range(6)]
        logging.error(f"user name {user_name} already exists. suggestions: {', '. join(suggestions)} ")
        raise ValueError(f"user name {user_name} already exists.\nsuggestions: {', '. join(suggestions)} ")
    
    if len(user_name) < 8:
        logging.error(f"User name must me 8 character's long")
        raise ValueError(f"User name must me 8 character's long")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', user_name):
        logging.error("Username must contain at least one special character")
        raise ValueError("Username must contain at least one special character")
    if not re.search(r'[0-9]', user_name):
        logging.error("Username must contain at least one number")
        raise ValueError("Username must contain at least one number")
    if not re.search(r'[A-Z]', user_name):
        logging.error("Username must contain at least one uppercase letter")
        raise ValueError("Username must contain at least one uppercase letter")

    return True


def is_valid_name( name):
    """
    This function takes name as argument 
    param : name : str
    return : bool
    """
    if not name or not isinstance(name, str) or not re.match("^[a-zA-Z ]*$", name):
        raise ValueError("Name must be a non-empty alphabetic string")
    return True

def is_valid_dept(dept):
    """
    This function takes dept as argument and validates
    param : dept : str
    return : bool
    """
    if not dept or not isinstance(dept, str):
        raise ValueError("Department must be a non-empty string")
    return True


def is_valid_dob(dob):
    """
    This function takes dept as argument and validates
    param : dob : str
    return : bool
    """
    if not re.match(r"\d{1,2}-\d{1,2}-\d{4}", dob):
        raise ValueError("DOB must be in the format DD-MM-YYYY")
    return True    





