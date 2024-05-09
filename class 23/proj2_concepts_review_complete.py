from datetime import datetime

'''Write a program that will take the user's first name, and than the users last name, and print the value to a text file on 2 separate lines'''


# one method
# with open('my_name.txt', 'w') as output:
#     firstname = input("First name: ")
#     lastname = input("Last name: ")
#     output.write(f'First name: {firstname}\nLast name: {lastname}')

# other method, with open preferred, no manual close
# f = open("my_output.txt", 'w')
# f.write(f'First name: {firstname}\nLast name: {lastname}')
# f.close()


''' Write a function called print_even_numbers that will take in a list of integer values and will extract the even numbers from that list and write to a text file let's try different parameters in our open function x, a, w'''

def print_even_numbers(my_list):
    output_list = []
    for m in my_list:
        if m % 2 == 0:
            output_list.append(m)
    with open('even_numbers.txt', 'w') as output:
        for o in output_list:
            o = str(o)
            output.writelines(o)
    
    print('File Printed Successfully')

my_list = [1,2,3,4,5,6,7,12,14,15,21,22]

print_even_numbers(my_list)

''' Lets read in the song lyrics and put it into a list, but before we do, lets look at other options we have to read files in'''


# with open('time_to_say_goodbye.txt', 'r') as lyrics:
    # my_paragraph = lyrics.read()
    # my_line = lyrics.readline()
    # my_list = lyrics.readlines()


# print(my_paragraph)
# print(my_line)
# print(my_list)



''' Bank account class 
Create the bank account class per the specifications in the powerpoint.  
'''

class BankAccount:
    def __init__(self, customer_name, account_number, date_of_opening, balance, ):
        self.customer_name = customer_name
        self.account_number = account_number
        self.date_of_opening  = date_of_opening 
        self.balance = balance
        
    def __str__(self):
        return f'''Customer Name: {self.customer_name}\nAccount Number: {self.account_number}\nDate of Opening: {self.date_of_opening}\nBalance: {self.balance:.02f}'''
    
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited in your account.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
    
    def check_balance(self):
        print(f"Current balance is ${self.balance}.")
    
    def days_since_opened(self):
        open_date = datetime.strptime(self.date_of_opening, '%m-%d-%y')
        today = datetime.now()
        days_since_opened = today - open_date
        return f'Account opened {days_since_opened.days} days ago.'
    
    def print_customer_details(self):
        f = open("customer_details.txt", "w")
        f.write( f'''Acct Number: {self.account_number}\nAccount holder name: {self.customer_name}\nBalance: {self.balance:.02f}\nDays since Account Opened: {self.days_since_opened()}''')
        f.close()


# ac_no_1 = BankAccount("Toninho Takeo", 2345, "05-05-24", 1000 )
# ac_no_2 = BankAccount("Jim Jones", 5424, "01-05-22", 1000 )
# ac_no_3 = BankAccount("Sally Field", 3242, "11-04-15", 1000 )
# ac_no_4 = BankAccount("Burt Reynolds", 4325, "08-11-13", 1000 )

# String representclass20_classes_pt2/semester_end_review.py

# Deposit method
# ac_no_1.deposit(500)

# Check new balance with check balance method
# ac_no_1.check_balance()

# Withdraw method
# ac_no_1.withdraw(250)

# Check new balance with check balance method
# ac_no_1.check_balance()

# How many days ago did this account get setup?
# print(ac_no_1.days_since_opened())

# Lets print acct details to a file
# ac_no_1.print_customer_details()