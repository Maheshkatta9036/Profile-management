from logger import *
import re
from constants import *

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


def is_valid_record(record):
    """
    This function  a new record for inserting in to DATA
    param: record: dict
    return: bool
    """

    if is_valid_name(record["name"]):
        if is_valid_dob(record["dob"], record["name"]):
            if is_valid_gender(record["gender"], record["name"]):
                if is_valid_password(record["password"]):
                    return True


def is_valid_gender(gender, name):
    """
    This function is for validate the gender
    :param gender: str    :param name: str
    :return: bool
    """
    if gender in VALID_GENDER:
        return True
    else:
        logging.error(f'User={name} has invalid gender = {gender}')
        raise Exception(f'Error:-User={name} has invalid gender = {gender}')


def is_valid_password(password):
    if len(password) < 6:
        logging.error(f"Length of password should not be less than 6")
        raise Exception(f"Length of password should not be less than 6")

    patterns = {
        "uppercase": r'[A-Z]',
        "lowercase": r'[a-z]',
        "digit": r'\d',
        "special": r'\W'
    }

    for name, pattern in patterns.items():
        if not re.search(pattern, password):
            logging.error(f"Password {password} doesn't contain {name} character")
            raise Exception(f"Password {password} doesn't contain {name} character")

    return True


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


def create_user_info(role):
    global admin
    user = input(f"Enter username:")
    name = input(f"Enter Name:")
    initial = input(f"Enter first character of surname:")
    dept = input(f"Enter the department:")
    dob = input(f"Enter the DOB:")
    gender = input(f"Enter the gender:")
    password = input(f'Enter the password that contains one Upper,lower,digit,special char = ')
    if role == "normal":
        admin = False
    elif role == "admin":
        admin = True
    return {"username": user, "name": name + "." + initial, "dept": dept, "dob": dob, "gender": gender,
            "password": password, "isadmin": admin}





