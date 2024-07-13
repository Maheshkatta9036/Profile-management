from logger import *
from validate_product_utils import *
from constants import PRODUCT_DETAILS

class product_operations():
    '''
    This class insert's, update's and delete's the product information based on user requirement
    '''
    def __init__(self):
        self.product_details = PRODUCT_DETAILS

    def insert_product(self, product_details):
        '''
        This function inserts a new product into the product database
        param : product_details : dict
        return : bool
        '''
        logging.info("\nProduct Insertion started...\n")
        logging.info
        try:
            product_id = product_details.get('product_id')
            name = product_details.get('name')
            price = product_details.get('price')
            description = product_details.get('description')
            specifications = product_details.get('specifications')

            if (is_valid_product_id(product_id) and is_valid_product_name(name) and is_valid_product_price(price) 
                and is_valid_product_description(description) and is_valid_product_specifications(specifications)):
                if product_id not in self.product_details:
                    self.product_details[product_id] = {
                        'name': name, 
                        'price': price,
                        'description': description,
                        'specifications': specifications
                    }
                    logging.debug(f'Product inserted successfully: {self.product_details[product_id]}')
                    return True
                else:
                    logging.error(f'Product ID already exists: {self.product_details}')
                    raise ValueError(f'Product ID already exists: {self.product_details}')
        except Exception as err:
            logging.error(f'Error while insert :- {err} ')

    def update_product(self, product_id, update_details):
        '''
        This function updates an existing product in the product database
        param1 : product_id : int
        param2 : update_details : dict
        return : bool
        '''
        logging.info("\nProduct details updating...\n")
        try:
            if is_valid_product_id(product_id):
                print(self.product_details)
                print(product_id)
                if product_id in self.product_details:
                    name = update_details.get('name')
                    price = update_details.get('price')
                    description = update_details.get('description')
                    specifications = update_details.get('specifications')

                    if name is not None and is_valid_product_name(name):
                        self.product_details[product_id]['name'] = name
                    if price is not None and is_valid_product_price(price):
                        self.product_details[product_id]['price'] = price
                    if description is not None and is_valid_product_description(description):
                        self.product_details[product_id]['description'] = description
                    if specifications is not None and is_valid_product_specifications(specifications):
                        self.product_details[product_id]['specifications'] = specifications
                    logging.info(f'Product updated successfully: {self.product_details[product_id]}')
                    return True
                else:
                    logging.debug(f'Product ID does not exist: {product_id}')
                    raise ValueError(f'Product ID does not exist: {product_id}')
        except Exception as err:
            print(err)
            logging.error(f'Error while update :- {err} ')

    def delete_product(self, product_id):
        '''
        This function deletes an existing product from the product database
        param : product_id : int
        return : bool
        '''
        try:
            if is_valid_product_id(product_id):
                if product_id in self.product_details:
                    del self.product_details[product_id]
                    logging.deug(f'Product deleted successfully: {self.product_details}')
                    return True
                else:
                    logging.debug(f'Product ID does not exist: {self.product_details}')
                    raise ValueError(f'Product ID does not exist: {self.product_details}')
        except Exception as err:
            logging.error(f'Error while deletion :- {err} ')

  
new_product = {
    'product_id': 1,
    'name': "T-Shirt",
    'price': 99.99,
    'description': "This is a good product",
    'specifications': {"color": "red", "size": "M"}
    }
            
updated_details = {
    'price': 109.99,
    'description': "It is a fantastic one"
    }

  

obj = product_operations()
obj.insert_product(new_product)
obj.update_product(1, updated_details)
#obj.delete_product(1)