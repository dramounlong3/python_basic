from class_person import Person #只引入類別

#繼承
class Student(Person):
    def __init__(self,name,age,school):
        super().__init__(name,age) #從父類別繼承建構子, 但自身還是得宣告變數
        self.school = school
        
    #函數會自動從父類別繼承
    def print_school(self):
        return self.school
        