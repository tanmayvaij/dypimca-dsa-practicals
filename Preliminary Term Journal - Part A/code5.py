"""
Create class Pizza_order_management_system with the class 
attributes like ordered, Pizza_order, Pizza_type, Quantity,
Address, Distance_Kilometer. If the customer distance kilometer 
is greater than 3.5 than Rs 45 will the extra charge will be added 
in bill. Print bill details in printBill() 
"""

class Pizza_order_management_system:
    def __init__(self, pizza_order, pizza_type, quantity, address, distance_kilometer, price):
        self.pizza_order = pizza_order
        self.pizza_type = pizza_type
        self.quantity = quantity
        self.address = address
        self.price = price + 45 if distance_kilometer > 3.5 else price

    def print_bill(self):
        print(self.pizza_order, self.pizza_type, self.quantity, self.address, self.price)

p1 = Pizza_order_management_system("Farmhouse", "S", 1, "Pune", 3.2, 300)
p2 = Pizza_order_management_system("Peppy Panner", "L", 2, "Goa", 4.5, 400)

p1.print_bill()
p2.print_bill()
