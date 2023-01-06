class student:
    def getdata(self,roll,name):
        self.roll = roll
        self.name = name
    def showdata(self):
        print(self.roll)
        print(self.name)
# s1 = student()
# s2 = student()
# s1.getdata(1, 'Rahul')
# s2.getdata(2, 'Raju')
# s1.showdata()
# s2.showdata()

class student2:
    def __init__(self,a,b): #constractor
        self.a = a
        self.b = b
    def showdata(self):
        print(self.a)
        print(self.b)
# a1 = student2(1, 'sdf')
# a1.showdata()


# Destructor is used the deallocate for the object which is no more useful for the program.
class student3:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __del__(self):
        print("object is deleted")
    def showdata(self):
        print(self.a)
        print(self.b)
a1 = student3(1, 'sdf')
a1.showdata()
a2 = student3(2, 'xyz')
a2.showdata()
del a1
a1.showdata()

