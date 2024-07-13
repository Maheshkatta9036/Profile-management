"""This is the main file for posting data"""

from logger import *
from constants import DATA
from validate_utils import *

class PostUserData():
    '''
    The PostUserData class validates the users info and post 
    '''
    
    def __init__(self):
        logging.info("User details validation and posting started")
       

    def post_new_record(self, record):
        '''
        This Function takes the new record and post 
        param : record : dict
        return : response : dict  
        '''
        try:
            logging.debug(f"Validating for new user {record}")
            if isinstance(record, dict):
                if 'mobile' in record:
                    logging.debug(f"Validating for mobile...")
                    if is_valid_mobile(record['mobile']):
                        logging.debug(f"Mobile number validated successfully")
                        if 'name' in record:
                            logging.debug(f"Validating for name...")
                            if is_valid_name(record['name']):
                                logging.debug(f"Name validated successfully")
                                DATA['records'].append(record)
                                response = {"Message":"Record Inserted SUCCESSFULLY", "record":record}
                                logging.debug(f"{response}")
                                return response
                        else:
                            response = {"Message": "Missing name key in record", "record":record}
                            logging.debug(f"{response}")
                            return response
                else:
                    response = {"Message": "Missing mobile key in record", "record":record}
                    logging.debug(f"{response}")
                    return response
            else:
                response = {"Message": f"Incorrect record type {type(record)}"}
                logging.debug(f"{response}")
                return response
                
        except Exception as err:
            logging.error(f"Error while validating user details :- {err}")
        finally:
            logging.info(f"Execution completed")
            print("Program executed succesfully")

obj = PostUserData()
obj.post_new_record({'mobile':469036318984, 'name':'Yaswant_Kumar.P'})