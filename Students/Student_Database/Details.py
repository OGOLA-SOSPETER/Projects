# Student Database
import string
from Students.DatabaseDataModels.DataBaseAccess import MyDatabase

class StudentData(MyDatabase):
    def __init__(self):

        super().__init__()
        self.fee_balance = None

    def GetLevel(self):
        school = input('Enter the full name of your School: ')
        my_school = school.upper()
        if 'PRIMARY' in my_school:
            print('\nSorry. Your school : ' + my_school + ' is not registered with our servers.')

        elif 'SECONDARY' in my_school or 'HIGH' in my_school:
            address = input('Enter the box code: ')
            town = input('Enter town address: ')
            print('Welcome to our School System Management, ' + school)

        else:
            print(my_school + ' Undefined!!')


    def GetFeeBalance(self):
        for record in self.student_records:
            self.fee_balance = record['fees_due'] - record['fees_paid']
            return self.fee_balance

    def Get_Details(self):
        self.counter = eval(input('Enter the number of entries you need to make: '))

        for count in range(self.counter):
            print("Enter your details: ")
            name = input('Name: ')
            stream = input('Stream: ')
            form = input('Form: ')
            print('\n')
            rg1 = self.Reg_Nos[0:4]
            rg2 = self.Reg_Nos[7:10]
            rgn = eval(self.Reg_Nos[4:7]) + (count+1)
            if count < 10:
                rgnmbr = rg1 + '00' + str(rgn) + rg2
            elif 10 > count < 100:
                rgnmbr = rg1 + '00' + str(rgn) + rg2
            else:
                rgnmbr = rg1 + str(rgn) + rg2

            if name not in self.student_records[['name']]:
                self.student_records.append(name)

            self.Name.append(name)
            self.Form.append(form)
            self.Reg_No.append(rgnmbr)
            self.Stream.append(stream)
            self.database.update()


    def DisplayStudent(self):
        for count in range(self.counter):
            print('-'*45, '\n')
            print("Student Name: " + self.Name[count])
            print("Student Reg_No: " + self.Reg_No[count])
            print("Student Form: " + self.Form[count])
            print("Student Stream: " + self.Stream[count])
            print('-'*45, '\n')


    # def splitter(self):
    #     rg1 = self.Reg_Nos[0:4]
    #     rg2 = self.Reg_Nos[7:10]
    #     rgn = eval(self.Reg_Nos[4:7]) + 1
    #     print(rg1)
    #     print(rg2)
    #     print(rgn)

    # def databases(self):
    #     print(self.database.items())
    #




#
# Student1 = StudentData()
# Student1.GetLevel()
# Student1.Get_Details()
# Student1.DisplayStudent()
# Student1.databases()



