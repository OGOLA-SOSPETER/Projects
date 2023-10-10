import pyodbc

from Students.Student_Database.Details import StudentData
from Students.DatabaseDataModels.DataBaseAccess import MyDatabase

#Student examinations records and reports

class Examinations(MyDatabase):
    def __init__(self):
        super().__init__()
        self.English:int = 0
        self.Kiswahili:int = 0
        self.Maths:int = 0
        self.Science:int = 0
        self.Social:int = 0
        self.student:str = ''

        self.new_database = {'name': self.name, 'reg': self.reg_no,
                             'english': self.English, 'maths':self.Maths, 'kiswahili': self.Kiswahili,
                             'science': self.Science, 'social': self.Social}

    def GetGrades(self):
        print('Select the student to enter their marks.')
        self.student = input('Name: ')
        # return self.student

        for self.record in self.student_records:
            if self.student in self.record['name']:
                print(f"Name Exists.\t Registration Number : {self.record['reg_no']}")
            else:
                print('Name does not exist!!!')


            print(f"{self.record['name']}, your registration number is {self.record['reg_no']}")



NewRecord = Examinations()
NewRecord.GetGrades()
