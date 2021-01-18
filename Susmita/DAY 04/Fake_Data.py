import faker
import pandas as pd

fake = faker.Faker()
df = pd.DataFrame(columns=['Name', 'Address', 'Phone'])

for i in range(100):
    name = fake.name_female() + '01'
    address = fake.street_address()
    phone_number = fake.phone_number()
    df = df.append({'Name': name, 'Address': address, 'Phone': phone_number}, ignore_index=True)

df.to_csv('Fake_Data.csv')
