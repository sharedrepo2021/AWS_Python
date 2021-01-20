import json as js
import pandas as pd
import Faker as fk

with open("ExampleFile.json", "r") as file:
    data = js.load(file)
    print("Data in ason file ", js.dumps(data, indent=5))
    df = pd.DataFrame.from_dict(data, orient='columns')
    print("Dataframe", df)
    print("Values in df", df[Information])

fakedata = Faker()
fakedata.name()