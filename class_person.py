#類別
class Person:
    def __init__(self, name, age): #建構子, self可以省去宣告name, age成員
        self.name = name
        self.age = age
        
    def print_name(self):
        return self.name
            
    def print_age(self):
        return self.age