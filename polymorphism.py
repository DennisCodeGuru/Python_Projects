


#Parent Class User
class User:
    name = "Mark"
    email = "mark@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email incorrect.")


#Child Class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"


#This is the same method in the parent class "User".
# The difference is that, insted ofusing entry_password, we're using entry_pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your Pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email incorrect.")
            
            
#Child Class Customer
class Customer(User):
    base_order = 20.00
    department = "General"
    order_number = "11"


#This is the same method in the parent class "User".
# The difference is that, insted ofusing entry_password, we're using entry_order.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_order = input("Enter your Order: ")
        if (entry_email == self.email and entry_pin == self.order_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("Please enter your email. Thank you.")

#The folowing code invokes the methods inside each class for User and Employee and Customer.
        
customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

customer = Customer()
customer.getLoginInfo()