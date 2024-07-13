from datetime import datetime

def validate_name(name, mobile):
    print(f'Name validation started for {name}')
    name = name.replace('.', '').replace('_', '').replace(' ', '')

    if len(name)>3:
        pass
    else:
        raise ValueError(f'User name cannot be {len(name)} characters, user:-{mobile}')
    if name.isalpha():
        pass
    else:
        raise ValueError(f'User name must be string only, user:-{mobile} ') 
    print(f'{name} validated successfully')

    return True

def validate_dob(dob, mobile):
    print(f'DOB validation started for {dob}')
    try:
        dob_date = datetime.strptime(dob, '%d-%m-%Y')
        if dob_date < datetime.now():
            print(f'{dob} validated successfully')
            return True
        else:
            raise ValueError(f'Date of birth cannot be in the future, user:-{mobile}')
    except ValueError:
        raise ValueError(f'DOB must be in DD-MM-YYYY format, user:-{mobile}')


def validate_email(email, mobile):
    print(f'Email validation started for {email}')
    if email.endswith('@gmail.com') or email.endswith('@yahoo.com'):
        print(f'{email} validated successfully')
        return True
    else:
        raise ValueError(f'Email must end with @gmail.com or @yahoo.com, user:-{mobile}')
    

def validate_blood_group(blood_group, valid_blood_groups, mobile):
    print(f'Blood group validation started for {blood_group}')
    if blood_group in valid_blood_groups:
        print(f'{blood_group} validated successfully')
        return True
    else:
        raise ValueError(f'Invalid blood group, user:-{mobile}')

def validate_gender(gender, valid_genders, mobile):
    print(f'Gender validation started for {gender}')
    if gender.upper() in valid_genders:
        print(f'{gender} validated successfully')
        return True
    else:
        raise ValueError(f'Invalid gender, user:-{mobile}')

def validate_door_no(door_no, mobile):
    print(f'Door number validation started for {door_no}')
    if door_no.isalnum():
        print(f'{door_no} validated successfully')
        return True
    else:
        raise ValueError(f'Door number must be alphanumeric, user:-{mobile}')

def validate_city(city, mobile):
    print(f'City validation started for {city}')
    if city.isalpha():
        print(f'{city} validated successfully')
        return True
    else:
        raise ValueError(f'City must be alphabetic, user:-{mobile}')

def validate_state(state, mobile):
    print(f'State validation started for {state}')
    if state.isalpha():
        print(f'{state} validated successfully')
        return True
    else:
        raise ValueError(f'State must be alphabetic, user:-{mobile}')

def validate_pin(pin, mobile):
    print(f'PIN validation started for {pin}')
    if pin.isdigit() and len(pin) == 6:
        print(f'{pin} validated successfully')
        return True
    else:
        raise ValueError(f'PIN must be a 6 digit number, user:-{mobile}')
    
    