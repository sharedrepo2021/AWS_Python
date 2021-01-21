import faker
import pyodbc


class PopulateSqlTable():
    def __init__(self):
        self.fake = faker.Faker()
        self.cursor=None

    def connect(self):
        con = pyodbc.connect('Driver={SQL Server};'
                             'Server=BIJI-PC\SQLEXPRESS;'
                             'Database=employee;'
                             'Trusted_Connection=yes;')
        self.cursor = con.cursor()

    def insertdata(self):
         firstname =self.fake.first_name()
         zip =self.fake.postcode()
         query = "INSERT INTO person.details(name,phone) VALUES ('{}','{}')".format(firstname,zip)
         self.cursor.execute(query)

    def comitresults(self):
        query = 'COMMIT'
        self.cursor.execute(query)

if __name__ == "__main__":
   obj= PopulateSqlTable()
   obj.connect()
   for i in range(1000):
    obj.insertdata()
   obj.comitresults()
   print("items inserted")