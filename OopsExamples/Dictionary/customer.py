class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location


list_of_customers = [
    Customer(101, 'Mark', 'US'),
    Customer(102, 'Jane', 'Japan'),
    Customer(103, 'Kumar', 'India')
]

dict_of_customer = {}

# Grouping
for customer in list_of_customers:
    if customer.location not in dict_of_customer:
        dict_of_customer[customer.location] = []
    dict_of_customer[customer.location].append(customer)


# Print List
print("List of Customers:")
for c in list_of_customers:
    print(c.cust_id, c.cust_name, c.location)

print("\n-------------------\n")

# Print Dictionary
print("Dictionary of Customers by Location:")
for location, customers in dict_of_customer.items():
    print(location, "->")
    for c in customers:
        print(" ", c.cust_id, c.cust_name)