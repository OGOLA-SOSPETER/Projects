# displaying the student data and details
from Students.Student_Database.Details import StudentData


class StudentDisplay(StudentData):
    def __init__(self):
        super().__init__()
        self.School = None

    # Student1 = StudentData()

    def GetLevel(self):
        super().GetLevel()
    def Get_Details(self):
        super().Get_Details()
    def DisplayStudent(self):
        super().DisplayStudent()

    def DisplayForm(self):
        for counter1 in range(len(self.School)):
            tabb = '\t\t\t\t'
            print(tabb, 'Welcome to ' + self.School[counter1] + '!')
            print(tabb, 'P.O BOX ', self.Address[counter1], ', ', self.Town[counter1])
            print('\n')
            tab = '\t\t\t'
            print('\tNAME: ' + tab + ' \tREG_NO: ' + tab + '\tSTREAM: ' + tab + '    CLASS/FORM: ' + tab + 'BOX ADDRESS: '
                  + tab + 'TOWN: ')
            for count in range(len(self.Name)):
                print(count+1,'. ',  self.Name[count], tabb,  self.Reg_No[count], tabb, self.Stream[count], tabb, '\t', self.Form[count],
                      tabb,self.Address[counter1], tabb, self.Town[counter1])





# Student1 = StudentData()
StudentDisplayed = StudentDisplay()
StudentDisplayed.GetLevel()
StudentDisplayed.Get_Details()
StudentDisplayed.DisplayStudent()
StudentDisplayed.DisplayForm()
