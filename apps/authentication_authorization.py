from ..logs.logger import *
from constants import USERS, ADMINS, LOG_SWITCH
from user_manager_utils import *

class UserManager():
    '''
    This classs manage's the user's authentication and authorization
    '''
    def __init__(self):
        '''
        Constants are defined in the constructor
        '''
        self.users = USERS
        self.admins = ADMINS
        self.log_switch = LOG_SWITCH

    def create_user_role(self, user_name, user_role):
        '''
        This method takes the user information and validates it
        param : user_role : str
        return : None
        '''
        logging.info(f"creating user details with the admin access {user_name}")
        user_name = input("Enter the User name here :-")
        is_valid_user_name(user_name, self.users, self.admins)

        firstname = input("Enter first name: ")
        is_valid_name(firstname)

        middlename = input("Enter middle name (optional): ")
        if middlename:
            is_valid_name(middlename)

        lastname = input("Enter last name (optional): ")
        if lastname:
            is_valid_name(lastname)

        dept = input("Enter the department: ")
        is_valid_dept(dept)

        dob = input("Enter the DOB (DD-MM-YYYY): ")
        is_valid_dob(dob)

        if user_role == 'a':
            is_admin = True
        else:
            is_admin = False

        user_info = {
            "username": user_name,
            "name": f"{firstname} {middlename} {lastname}".strip(),
            "dept": dept,
            "dob": dob,
            "isadmin": is_admin
        }
        
        return user_info


    def create_user(self, name):
        '''
        This method take's the argument name in the str format and create's user
        param : name : str
        return : None
        '''
        if not authenticate_user(name, self.users, self.admins):
            logging.error(f"Permission denined for the user {name}")
            raise Exception (f"Unauthorized user {name}, trying to access the application")

        if name in self.admins:
            if self.log_switch:
                logging.debug(f"User {name} Authorized successfully")
            
            user_role = input("Enter the role ('a' for admin and 'n' for normal) for the user {name} :-")
            if user_role in ['n','a']:
                user_info = self.create_user_role(name, user_role)
                if user_role == 'n':
                    self.users.append(user_info['username'])
                    if self.log_switch:
                        logging.debug(f"{user_info['username']} added as normal user")
                else:
                    self.admins.append(user_info['username'])
                    if self.log_switch:
                        logging.debug(f"{user_info['username']} added as an admin user")
                if self.log_switch:
                    logging.debug(f"Final user info: {user_info}")
            else:
                logging.debug("Incorrect role chosen - available options are n and a only")
                raise ValueError("Incorrect role chosen - available options are n and a only")
        else:
            logging.debug(f"User {name} does not have create profile permission")
            raise PermissionError(f"User {name} does not have create profile permission")


obj = UserManager()
obj.create_user(input('Enter the userame here to access :-'))




    