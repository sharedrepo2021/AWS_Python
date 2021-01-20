class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

  def welcome(self):
      print("Welcome", self.firstname, self.lastname)


class Student(Person):
  def __init__(self, fname, lname, year):
    #Person.__init__(self, fname, lname)
    #super().__init__(fname, lname)
    self.firstname = fname
    self.lastname = lname
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


#Use the Person class to create an object, and then execute the printname method:

#x = Person("sheela", "balamurugan")

x = Student("mirithika", "balamurugan", 2019)
x.printname()
x.welcome()


class Human(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Human):

    def isEmployee(self):
        return True

emp = Human("Siva")
print(emp.getName(), emp.isEmployee())

emp = Employee("Siva")
print(emp.getName(), emp.isEmployee())


class A:
    def __init__(self, fname):
        self.name = fname


class B(A):
    def __init__(self, fname, roll):
        A.__init__(self, fname)
        self.roll = roll


object = B("bala", 23)
print(object.name)
print(object.roll)



