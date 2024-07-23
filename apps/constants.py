"""This file contains the constants for the project"""

# ---------MOBILE VALIDATION-------------------
DATA = {'records':[]}
VALID_COUNTRY_CODE = ['91', '46', '16']
EXCLUDED_NUMBERS = [9036318984, 9945383132]

#----------------PRODUCT OPERATION's-----------
PRODUCT_DETAILS = {}


#----------Authentication and Authorization----
USERS = ['maheshk', 'yaswanthp', 'vigneshl']
ADMINS = ['prasad']
USER_DATA = {}
LOG_SWITCH = True


DATA = {"records": [
    {'username': 'maheshk', 'name': 'maheshkatta', 'dept': 'IT', 'dob': '1998-06-15', 'gender': 'M', 'isadmin': False},
    {'username': 'yashwanth', 'name': 'yashwanthp', 'dept': 'Dev', 'dob': '1997-08-15', 'gender': 'M','isadmin': False},
    {'username': 'vignesh', 'name': 'vigneshp', 'dept': 'Sales', 'dob': '1999-15-08', 'gender': 'M',  'isadmin': True}
]}
VALID_GENDER = ["MALE", "FEMALE", "OTHERS", "M", "F"]
USERS = ["yashwanth", "vignesh"]
ADMINS = ["MAHESHK"]
ALL_USERS = ["mahesh", "vignesh", "yashwanth"]
PASSWORDS = {
    "mahesh": "Mahesh@123",
    "yashwanth": "Yashwanth@123",
    "vignesh": "Vignesh@345"
}

ADMIN = "admin"
NORMAL = "normal"
SUCCESS = "success"
FAILED = "failed"


# emails configurations
SMTP_PORT = 587
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "k.mahesh7675@gmail.com"
RECEIVER_EMAIL = ["kattamahesh.pydev@gmail.com", "pathipatiyaswanth@gmail.com"]
PASSWORD = "izdlrkcuyzrlwxec"

DELETE_MESSAGE = """
Hello Team,\n
Admin has deleted user {} Record in DATA
Thank you 
"""
UPDATE_MESSAGE = """
Hello Team,\n
Admin has updated user={} record.
Record = {}\n
Thank You
"""
GET_ALL_MESSAGE = """
Hello Team,\n
User, is checking all users information from the table.\n
Thank You
"""
PARTIAL_UPDATE = """
Hello Team\n
Admin has partially updated the user={} records in DATA.\n
Partially updated user record = {}\n
Thank you
"""
UNAUTHENTICATED_MESSAGE = """
Hello team\n
ALERT:-Unauthenticated user={}, trying to access the application
check logs\n
Thank You
"""
UPDATE_USER_RECORD = """
Hello team\n
''User={} has updated his profile''
Updated Record = {}
\nThank you
"""
RECORD_ADDED = """
Hello Team,\n 
Admin={} added the user={} record = {}.\n
Thank You
"""
RESET_PASSWORD = """
Hello Team\n
Admin has reseted the user={} password\n
Thank You
"""
CHECK_USER_INFO = """
Hello Team,\n
Admin checking user={} information.\n
Thank You
"""
USER_INFO = """
Hello Team,\n
User={} checking his information.\n
Thank You
"""