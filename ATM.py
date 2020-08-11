import sys

class ATM:
    def __init__(self, userid, pin):
        self.customers_dict = {}
        with open('customers.txt', 'r') as fh:
            for data in fh.readlines():
                _userid, _pin, _name, _balance = data.strip().split(',')
                self.customers_dict[_userid] = data.strip().split(',')

        self.userid = userid
        self.pin = pin
        print(f'Welcome {self.customers_dict[userid][2]}!!!') 

    @property
    def userid(self):
        return self.__userid

    @userid.setter
    def userid(self, value):
        if value in self.customers_dict.keys():
            self.__userid = value
        else:
            sys.exit('Not a registered user')

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        if value == self.customers_dict[self.userid][1]:
            self.__pin = value
        else:
            sys.exit('Incorrect PIN')

    def withdraw(self, amount):
        if int(amount) > int(self.balance_enquiry()):
            print('Insufficient Balance')
            return

        if amount > 10000:
            print('Amount should be less than or equal to 10000')

        self.customers_dict[self.userid][3] = str(float(self.customers_dict[self.userid][3]) - amount)
        print(f'Amount withdrawn is {amount}')
        print(f'Your Account balance is {self.balance_enquiry():.2f}')

    def deposit(self, amount):
        self.customers_dict[self.userid][3] = str(float(self.customers_dict[self.userid][3]) + amount)
        print(f'Amount withdrawn is {amount}')
        print(f'Your Account balance is {self.balance_enquiry():.2f}')

    def balance_enquiry(self):
        return float(self.customers_dict[self.userid][3])

    def update_customers(self):
        with open('customers.txt', 'w') as filehandle:
            for key, value in self.customers_dict.items():
                filehandle.write(str(','.join(value)))
                filehandle.write('\n')

            
if __name__ == "__main__":
    userid = input('Enter USERID: ')
    pin = input('Enter PIN: ')
    t1 = ATM(userid, pin)

    print('Please select an option')
    print('1. Withdraw')
    print('2. Deposit')
    print('3. Balance Enquiry')
    print('4. Transfer Money')
    print('5. Exit')
    choice = int(input())

    if choice == 1:
        t1.withdraw(float(input('Enter amount to withdraw: ')))
        t1.update_customers()
    elif choice == 2:
        t1.deposit(float(input('Enter amount to Deposit: ')))
        t1.update_customers()
    elif choice == 3:
        print(f'Your Account balance is {t1.balance_enquiry():.2f}')
        t1.update_customers()
    elif choice == 4:
        print('This option is yet to be implemented')
        pass
    else:
        sys.exit('Thanks for visiting')

    print('Thanks for visiting')
