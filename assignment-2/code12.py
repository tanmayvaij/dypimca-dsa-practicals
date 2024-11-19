# Create two arrays , one for the product name and another for the product price and print the elements of two arrays (string concatenation should be there)

from numpy import array

product_name = array(["titan-watch", "rolex-watch", "sonata-watch", "fastrack-watch"])
product_price = array([2000, 3000, 4000, 5000])

for i in range(4):
    statement = product_name[i] + ": $" + str(product_price[i])
    print(statement)
