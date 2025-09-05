from sql_connection import get_sql_connection

def get_products(connection):

    cursor = connection.cursor()

    query="select * from medicine_inventory.products"
    
    cursor.execute(query)

    response =[]

    for (product_id, product_name, unit, product_price, unit_type) in cursor:
        response.append(
            {
                'product_id':product_id, 
                'product_name':product_name,
                'unit':unit,
                'product_price':product_price, 
                'unit_type':unit_type
            }
        )

    return response

def insert_products(connection , product):

    cursor1 = connection.cursor()

    try:

        query = "insert into medicine_inventory.products(product_id, product_name, unit_type, unit, product_price) values(%s, %s, %s, %s, %s)"
        data = (product['product_id'], product['product_name'], product['unit_type'], product['unit'], product['product_price'])

        cursor1.execute(query, data)
        connection.commit()

        print(f"Record inserted Successfully!!")

        return cursor1.lastrowid
    
    except Exception as e:
        print(f"Error Inserting Product:{e}!!")

        return None

def delete_products(connection, product_id):

    cursor2 = connection.cursor()

    cursor2.execute("SELECT product_id FROM medicine_inventory.products")

    #row[0] is for selecting first column from each of the tuple
    product_ids = [row[0] for row in cursor2.fetchall()]

    #use 'if statement' insted of 'for loop'
    if product_id in product_ids:
        query = "delete from medicine_inventory.products where product_id = %s"
        cursor2.execute(query, (product_id,))
        connection.commit()
        print("Record deleted!!")

    else:
        print("Product ID invalid!!")

    cursor2.close()

    # not found means found==False
if __name__=='__main__':
     connection = get_sql_connection()

     '''print(insert_products(connection , {
         'product_id': '5', 
         'product_name':'DOLO', 
         'unit_type':'strip', 
         'unit':'10', 
         'product_price':'40'
     }))'''
     

     '''print(get_products(connection))'''

     delete_products(connection, 6)
     # -> when used data variable to store product id, treated prouct id as string
     # -> here we are directly taking product id as argument, so treated as integer


# Make all functions dynamic   ---not happening
# While deleting a record make sure that record is already present in the database ----done///
# Add quantity of stock in database ---on hold//
#Exception Handling -----done///