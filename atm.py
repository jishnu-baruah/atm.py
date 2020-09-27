class Atm(object):
    def __init__(self):
        self.cardNumber = ""
        self.pinNumber = ""
        self.operation = ""

    def getDetails(self):
        self.cardNumber = input('enter your card number: ')
        self.pinNumber = input('enter your pin number: ')

    def getOperation(self):
        print("enter 'cw' for 'Cash withdrawel','be' for 'Bank enquiry','md' for 'Money deposit'")
        self.operation = input('please eter operation mode: ')

    def performOperation(self):
        op = self.operation
        if op == 'cw':
            amount = input('please enter amount in rs: ')
            print('please collect Rs.'+amount+'..')
            print('transaction succesfull!!')
            print('session ended!!')
            # break
        elif op == 'be':
            print('your account currently has Rs.2300')
            print('session ended!!')
            # break
        elif op == 'md':
            amount = input('please enter amount in rs: ')
            print('please deposit Rs.'+amount+' in the deposit slot.')
            print('please wait..')
            print('transaction succesfull!!')
            print('session ended!!')
            # break
        else:
            print('error!! please enter valid function.')
            print(
                "enter 'cw' for 'Cash withdrawel','be' for 'Bank enquiry','md' for 'Money deposit'")
            self.operation = input('please eter operation mode: ')


atm = Atm()
atm.getDetails()
atm.getOperation()
atm.performOperation()
