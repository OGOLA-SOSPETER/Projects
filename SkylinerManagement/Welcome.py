#Skyliner Financial Budget Management System
import datetime
import time
import pyodbc


class Welcome:
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Users\ogola\Projects\SkylinerManagement\BudgetTracker.accdb;')

    def __init__(self):
        self.name = "Budget TRacker Management System."
        self.optionmenu = {1:'Proceed',2:'Quit'}
        self.menu1 = {1:'View Month Data', 2:'View All', 3:'Add Budget', 4:'Add Expense',5:'Print Statement',6:'View Expenses'}
        self.budget = 20000.00
        self.cursor = None
        self.data = None

    def getdatta(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from  budget ")
        self.data = self.cursor.fetchall()

        list = []

        for row in self.data:
            list.append(row)
            print(list)
            list = []
        self.wait()
        self.menu()


    def welcome(self):
        print(f'Welcome to your {self.name}\n Track your finances in a go.')

    def menu(self):
        global k
        print('Select an option to continue:\n')
        for k,v in self.optionmenu.items():
            print(k, '.', v)
        # self.optionmenu.items()

        option = input(f'Select your Next Option:\t')

        if int(option) == 1:
            self.land()

        else:
            self.quit()

    def getbudget(self):
        self.budget = float(input("Enter your Monthly budget."))
        return  self.budget

    def budgetType(self):
        if (self.budget != 0):
            type = eval(input("Input the expense."))


    def land(self):
        self.spacer()
        print('Welcome to your Financial Management System.......')
        self.wait()
        self.getoption()

    def getmonth(self):
        m = input('Enter the month.\n')
        return  m.upper()

    def viewmonth(self,month):
        cursor = self.conn.cursor()
        cursor.execute(f"select * from budget WHERE Month = ?",month)
        self.waits()
        self.menu()

    def getexpense(self):
        expense = float(input("Enter your Monthly expense."))
        return  expense

    def addbudget(self,month,budget):
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT Budget from budget WHERE Month = ?',month)
        mt = cursor.fetchone()
        if(mt[0] <= 0):
            cursor = self.conn.cursor()
            cursor.execute(f'UPDATE budget SET Budget = ?  WHERE Month = ?',budget,month )
            cursor.commit()
            self.wait()
            print('Budget Added successfully.')
            self.waits()
            self.menu()
        else:
            print('The Budget is not Null.')
            self.waits()
            self.menu()


    def addexpense(self,month,expense):
        new_exp = []
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT Expenses from budget WHERE Month = ?', month)
        exp = cursor.fetchone()
        new_exp.append(exp[0])
        new_exp.append(expense)

        cursor = self.conn.cursor()
        cursor.execute(f'UPDATE budget SET Expenses = ?  WHERE Month = ?',new_exp,month )
        cursor.commit()


    def getoption(self):
        print('Select the Next Option:\n')
        for k,v in self.menu1.items():
            print(f"{k}. {v}")

        option = eval(input('Option Select:'))
        if (option == 1):
            mon = self.getmonth()
            self.wait()
            return self.viewmonth(mon)

        elif (option == 2):
            return self.getdatta()
        elif (option == 3):
            return self.addbudget(self.getmonth(), self.getbudget())
        elif (option == 4):
            mn = self.getmonth()
            ex = self.getexpense()
            self.wait()
            self.addexpense(mn,ex)
        elif (option == 5):
            return self.printbudget()

        else:
            return self.printexpenses()


    def quit(self):
        self.spacer()
        print('Thank you for checking in.\nSystem Shutting down shortly...')
        self.wait()
        print('System closed.')
        sys.exit()

    def spacer(self):
        print('\n')


    def wait(self):
        time.sleep(1)

    def waits(self):
        time.sleep(5)

    def getexpenses(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT MonthId,Month,Expenses from budget')
        data = cursor.fetchall()

        for item in data:
            print(f"{item[0]:2} {'':16} {item[1]:20} Kshs. {item[2]}")

    def printexpenses(self):
        print(f"\n{'Index':20} {'Month':20} {'Expense':25}")
        self.getexpenses()
        self.waits()
        self.menu()

    def printbudget(self):
        def geta():
            cursor = self.conn.cursor()
            cursor.execute('SELECT MonthId,Month,Budget,Expenses,Balance from budget')
            data = cursor.fetchall()

            for item in data:
                print(f"{item[0]:2} {'':16} {item[1][:3]} {'':20} Kshs. {item[2]} {'':20} Kshs. {item[3]} {'':20} Kshs. {item[4]} {'':20}")

        print(f"\n{'Index':20} {'Month':21} {'Budget':25} {'Expenses':25} {'Balance':25}")
        geta()
        self.waits()
        self.menu()

    def printStatement(self):
        title = "Monthly Account Statement."
        month = 'July'
        date = datetime.datetime.today()
        mont = datetime.date.today().month


        print(f"\t\t\t\t{title:30}")
        print(f"Statement for {mont}\t\t Date: {date}")
        self.spacer()
        print("\t\t\t\tBudget")
        def getbudgets():
            cursor = self.conn.cursor()
            cursor.execute('SELECT MonthId,Month,Budget from budget')
            data = cursor.fetchall()

            for item in data:
                print(f"{item[0]:2} {'':16} {item[1]:20} Kshs. {item[2]}")

        print(f"{'Index':20} {'Month':20} {'Budget':25}")
        getbudgets()

        self.waits()
        self.menu()
        # self.getdatta()

wl = Welcome()
wl.welcome()
wl.menu()
