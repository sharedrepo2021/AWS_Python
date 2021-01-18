import faker
import pyodbc


class PopulateSQLTable():
    def __init__(self):
        self.fake = faker.Faker()
        self.cursor = None

    def connect(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-1HL1TR2\SQLEXPRESS;'
                              'Database=AdventureWorks2019;'
                              'Trusted_Connection=yes;')
        self.cursor = conn.cursor()

    def insert_data(self):
        first_name = self.fake.first_name().upper()
        last_name = self.fake.last_name().upper()
        address = self.fake.street_address().upper()
        city = self.fake.city().upper()
        zip = self.fake.postcode()
        weight = float('{}.{}'.format(self.fake.random_number(digits=2), self.fake.random_number(digits=2)))
        birth_date = self.fake.date()
        date_enrolled = self.fake.date_time()

        query = "INSERT INTO Susmita.Student VALUES('{}', '{}', '{}', '{}', '{}', {}, '{}', '{}')" \
            .format(first_name, last_name, address, city, zip, weight, birth_date, date_enrolled)

        self.cursor.execute(query)

    def commit_results(self):
        query = 'COMMIT'
        self.cursor.execute(query)


if __name__ == "__main__":

    p = PopulateSQLTable()

    p.connect()
    for i in range(1000):
        p.insert_data()
    p.commit_results()