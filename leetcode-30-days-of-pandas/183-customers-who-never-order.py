import pandas as pd
'''
        Table: Customers
        +-------------+---------+
        | Column Name | Type    |
        +-------------+---------+
        | id          | int     |
        | name        | varchar |
        +-------------+---------+
        id is the primary key (column with unique values) for this table.
        Each row of this table indicates the ID and name of a customer.
        

        Table: Orders

        +-------------+------+
        | Column Name | Type |
        +-------------+------+
        | id          | int  |
        | customerId  | int  |
        +-------------+------+
        id is the primary key (column with unique values) for this table.
        customerId is a foreign key (reference columns) of the ID from the Customers table.
        Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
        

        Write a solution to find all customers who never order anything.

        Return the result table in any order.

        The result format is in the following example.

        

        Example 1:

        Input: 
        Customers table:
        +----+-------+
        | id | name  |
        +----+-------+
        | 1  | Joe   |
        | 2  | Henry |
        | 3  | Sam   |
        | 4  | Max   |
        +----+-------+
        Orders table:
        +----+------------+
        | id | customerId |
        +----+------------+
        | 1  | 3          |
        | 2  | 1          |
        +----+------------+
        Output: 
        +-----------+
        | Customers |
        +-----------+
        | Henry     |
        | Max       |
        +-----------+
'''

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    result = result.loc[result['customerId'].isna(), ['name']] # REMEMBER that loc needs square brakets :)
    result = result.rename(columns={'name': 'Customers'})
    return result

# MUUUUCH MORE EFFICIENT:
def find_customers2(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    never_order_df = customers[~customers['id'].isin(orders['customerId'])]
    return never_order_df[['name']].rename(columns={'name': 'Customers'})

customers = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
})

orders = pd.DataFrame({
    'id': [1, 2],
    'customerId': [3, 1]
})

print(find_customers2(customers, orders))