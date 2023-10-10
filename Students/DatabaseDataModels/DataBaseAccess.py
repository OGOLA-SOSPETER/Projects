import sys

import pyodbc

class MyDatabase:
    def __init__(self):
        self.student_records = []
        self.name:str = ''
        self.reg_no:int = 0
        self.record = {}
        self.conn = None

    def Database(self):
        self.conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Users\ogola\Projects\Students\StudentDatabase.accdb;')

        cursor = self.conn.cursor()

        # Fetching all the student records
        cursor.execute('select * from StudentData')
        rows = cursor.fetchall()

        # Assigning every table data to a variable
        for row in rows:
            record = {
                'reg_no': row[1],
                'name': row[2],
                'age': row[3],
                'stream': row[4],
                'form': row[5],
                'fees_due': row[6],
                'fees_paid': row[7],
                'fee_balance': row[8],
                'maths': row[9],
                'english': row[10],
                'kiswahili': row[11],
                'science': row[12],
                'socialstudies': row[13]
            }
            self.name = record['name']
            self.student_records.append(record)

            # cursor.execute(f"UPDATE StudentData SET {} = 'Joseph Maina', {} = 23,{} = 'Blue', {} = 100, {} = 98,{} = 57, {} = 50, {} = 88,{} = 76 WHERE {} = REG0001T".format(record['name'],record['age'],record['stream'],record['fees_paid'],record['maths'],record['english'],record['kiswahili'],record['reg_no'],record['science'],record['socialstudies'] ))
        cursor.execute(
            "UPDATE StudentData SET NAME = ?, AGE = ?, STREAM = ?, FEESPAID = ?, MATHS = ?, ENGLISH = ?, KISWAHILI = ?, SCIENCE =?, SOCIALSTUDIES = ? WHERE REG_NO = ?",'Joseph Maina',23,'Blue',100,98,57,50,88,76,'REG0001T')
        self.conn.commit()
        # Printing the student records
        for record in self.student_records:
            print(f"{record['name']}, your registration number is {record['reg_no']}")


        # # Inserting a new student record
        # cursor.execute(f"INSERT INTO StudentData (REG_NO) VALUES ('{self.Reg_No}')")
        # cursor.commit()
        print(self.student_records)

    def enter_marks(self, reg_no, maths, english, kiswahili, science, socialstudies):
        update_query = f"UPDATE StudentData SET MATHS = {maths}, ENGLISH = {english}, KISWAHILI = {kiswahili}, SCIENCE = {science}, SOCIALSTUDIES = {socialstudies}"
        update_query += f" WHERE REG_NO = '{reg_no}'"

        cursor = self.conn.cursor()
        cursor.execute(update_query)
        self.conn.commit()

    def stud(self):
        self.name = input('Enter the student name to find: ')

    def getStudent(self,name):
        name_query = f"SELECT * FROM StudentData WHERE  {name} IN NAME"

        cursor = self.conn
        std = cursor.execute(name_query)
        self.conn.commit()

        print(zip(std))





# Data = MyDatabase()
# Data.Database()
# # Data.enter_marks('REG0004T',78,67,98,77,87)
# Data.stud()
# Data.getStudent(sys.stdin)
