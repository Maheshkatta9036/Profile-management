

from flask import Flask, jsonify, request
from logger import *
from constants import *
import constants as config
#from validate_utils import *
from user_manager_utils import *
from ..emails.email_operations import *
from ..errors.exceptions import *

app = Flask('__name__')
class profileManagement:
    '''
    The profileMnagament class validates the users info and manages records
    '''
    
    def __init__(self):
        logging.info("User details validation and posting started")

        
    @app.route('/create_user', methods = ["POST"])
    def post_new_record(self):
        '''
        This Function takes the new record and posts it
        return : response : dict  
        '''
        data = request.args
        name = data.get("name")
        logging.info(f'{name} - create_user function has started...')

        try:
            if not authenticate_user(name):
                raise AuthenticationError(f"Invalid user: {name}")

            if name in ADMINS:
                role = input(f"Enter the role for {name} (user or admin) :-")

                if role == config.NORMAL:
                    user_info = create_user_info(role=role)
                    if is_valid_record(user_info):
                        logging.debug(f'{name} - Admin has created a {role} user')
                        ALL_USERS.append(user_info["name"])
                        DATA["records"].append(user_info)

                        send_email([member for member in receivers], RECORD_ADDED.format(name, user_info["name"], user_info))
                        logging.debug(f"{name} - {user_info['name']} {role} user record added.")
                        return jsonify(message=user_info["name"] + " record has been created", admin=(role == 'admin'),
                                    status=config.SUCCESS), 200
                    
                elif role == config.ADMIN:
                    user_info = create_user_info(role=role)
                    if is_valid_record(user_info):
                        logging.debug(f"{name} - Admin has created the admin user")
                        ALL_USERS.append(user_info["name"])
                        DATA["records"].append(user_info)

                        send_email([members for members in receivers],
                                RECORD_ADDED.format(name, user_info["name"], user_info))
                        logging.debug(f"{name} - {user_info['name']} admin user record added..")
                        return jsonify(message=user_info["name"] + " record has been created", admin=True,
                                    status=config.SUCCESS), 200
                
                else:
                    logging.debug(f'{name} - Incorrect role :- {role}')
                    raise ValueError(f"{name} - Invalid role selected -{role},  choose admin or normal")
            else:
                logging.error(f"{name} - does not have create user profile permission")
                raise ValueError(f"{name} does not have the permission to create user")
                
           
        except Exception as err:
            logging.error(err)
            return jsonify(error=str(err), status=config.FAILED), 400

        except ValueError as err:
            logging.error(f"{name} - {err}")
            return jsonify(error=str(err), status=config.FAILED), 500

        finally:
            logging.info(f'{name} - Post new record function has ended...')


    
    @app.route('/update_user', methods=["PUT"])
    def update_user(self):
        """
        This function is used to update the full record of a user in DATA.
        return: json
        """
        data = request.args
        name = data.get("name")
        logging.info(f'{name} - update_user function has started...')
        try:
            if not authenticate_user(name):
                raise AuthenticationError(f"Unauthorized user: {name} detected.")

            if name in ADMINS:
                Name = input("Enter the name of the user to update: ")
                if Name in ALL_USERS:
                    for item in DATA["records"]:
                        if Name == item["name"]:
                            logging.debug(f'{name} - Modifying User={Name} record')
                            logging.debug(f'{name} - Previous record of User={Name} is: {item}')

                            Username = input(f"Enter the username for User={Name} record: ")
                            Name = input(f"Enter name for User={Name} record: ")
                            Gender = input(f'Enter the gender for User={Name} record: ')
                            Dept = input(f'Enter the department for User={Name} record: ')

                            if is_valid_name(Name) and is_valid_gender(Gender, Name):
                                item.update({"username": Username, "name": Name, "gender": Gender, "dept": Dept})
                                logging.debug(f'{name} - Modified User={Name} record is: {item}')

                                send_email([member for member in receivers], UPDATE_MESSAGE.format(Name, item))
                                return jsonify(message=item["name"] + " record has been updated", admin=item["isadmin"],
                                               status=config.SUCCESS), 200
                else:
                    logging.error(f'{name} - user={Name} has no records, check name once')
                    return jsonify(error=f'{Name} has no records, check name once', status=config.FAILED), 400

            else:
                logging.error(f"{name} - does not have update user permission")
                raise AuthorizationError(f"{name} - does not have update user permission")

        except (ValueError, AuthorizationError, AuthenticationError) as err:
            logging.error(err)
            return jsonify(error=str(err), status=config.FAILED), 400 if isinstance(err, ValueError) else 403 if isinstance(err, AuthorizationError) else 401

        except Exception as err:
            logging.error(f"{name} - {err}")
            return jsonify(error=str(err), status=config.FAILED), 500

        finally:
            logging.info(f'{name} - update_user function has ended...')


    @app.route('/reset_password', methods=["PATCH"])
    def reset_password(self):
        """
        This function  reset's the user password.
        :return: json
        """
        data = request.args
        name = data.get("name")
        logging.info(f'{name} - reset_password function has started...')
        try:
            if not authenticate_user(name):
                raise AuthenticationError(f"Unauthorized user: {name} detected.")

            if name in ADMINS:
                Name = input("Enter the name of the user to reset password: ")
                if Name in ALL_USERS:
                    for item in DATA["records"]:
                        if Name == item["name"]:
                            Password = input(
                                "Enter the password that should contains minimun of (aB!1) ")
                            if is_valid_password(Password):
                                logging.debug(f"{name} - Resetting {Name} password...")
                                item["password"] = Password
                                logging.debug(f"{name} - {Name} password has been reset.")
                                send_email([member for member in receivers], RESET_PASSWORD.format(Name))
                                return jsonify(message=Name + " has reset his password", admin=item["isadmin"],
                                               status=config.SUCCESS), 200
                else:
                    logging.error(f"{name} - user={Name} has no records, check name once")
                    return jsonify(error=f'{Name} has no records, check name once', status=config.FAILED), 400

            else:
                logging.error(f"{name} - does not have reset password permission")
                raise AuthorizationError(f"{name} - does not have reset password permission")

        except (ValueError, AuthorizationError, AuthenticationError) as err:
            logging.error(err)
            return jsonify(error=str(err), status=config.FAILED), 400 if isinstance(err, ValueError) else 403 if isinstance(err, AuthorizationError) else 401

        except Exception as err:
            logging.error(f"{name} - {err}")
            return jsonify(error=str(err), status=config.FAILED), 500

        finally:
            logging.info(f'{name} - reset_password function has ended...')


    @app.route('/delete_record', methods=["DELETE"])
    def delete_record(self):
        """
        This function deletes user record from DATA.
        :return: json
        """
        data = request.args
        name = data.get("name")
        logging.info(f"{name} - delete_record function has started...")
        try:
            if not authenticate_user(name):
                raise AuthenticationError(f"Unauthorized user: {name} detected.")

            if name in ADMINS:
                Name = input("Enter the name of the user to delete his record: ")
                if Name in ALL_USERS:
                    for item in DATA["records"]:
                        if Name == item["name"]:
                            logging.debug(f"{name} - Deleting record of {Name}")
                            send_email([member for member in receivers], DELETE_MESSAGE.format(Name))
                            DATA["records"].remove(item)
                            ALL_USERS.remove(Name)
                            logging.debug(f"{name} - {Name} record deleted.")
                            return jsonify(message=Name + " record has been deleted", status=config.SUCCESS), 200

                else:
                    logging.error(f'{name} - user={Name} has no records, check name once')
                    return jsonify(error=f'{Name} has no records, check name once', status=config.FAILED), 400

            else:
                logging.error(f"{name} - does not have delete record permission")
                raise AuthorizationError(f"{name} - does not have delete record permission")

        except (AuthorizationError, AuthenticationError) as err:
            logging.error(err)
            return jsonify(error=str(err), status=config.FAILED), 403 if isinstance(err, AuthorizationError) else 401

        except Exception as err:
            logging.error(f"{name} - {err}")
            return jsonify(error=str(err), status=config.FAILED), 500

        finally:
            logging.info(f"{name} - delete_record function has ended...")


    @app.route('/get_users_list', methods=["GET"])
    def get_users_list(self):
        """
        This function returns records of all the users.
        return: json
        """
        data = request.args
        name = data.get("name")
        logging.info(f"{name} - get_users_list function has started...")
        try:
            if not authenticate_user(name):
                raise AuthenticationError(f"Unauthorized user: {name} detected.")

            return jsonify(DATA["records"]), 200

        except AuthenticationError as err:
            logging.error(err)
            return jsonify(error=str(err), status=config.FAILED), 401

        except Exception as err:
            logging.error(f"{name} - {err}")
            return jsonify(error=str(err), status=config.FAILED), 500

        finally:
            logging.info(f"{name} - get_users_list function has ended...")


if __name__ == '__main__':
    app.run(debug=True)