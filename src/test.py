import json
import pandas as pd
import re

json_data = {}

with open("metadata.json", "r", encoding='utf-8') as outfile:
    json_data = json.loads(outfile.read())

data = {}

code = []
column_1 = []
column_2 = []
column_3 = []

for key in json_data:
    code.append(key)
    column_1.append(" ".join(json_data[key].split()).replace('. ', '.').replace(' .', ' ').replace(']', '1'))
    column_2.append((" ".join(json_data[key].split()).replace('. ', '.').replace(' .', ' ')).replace(']', '1').split(' ')[-2])
    column_3.append((" ".join(json_data[key].split()).replace('. ', '.').replace(' .', ' ')).replace(']', '1').split(' ')[-1])

df = pd.DataFrame({
    'ma-so': code,
    # 'column_1': column_1,
    'column_2': column_2,
    'column_3': column_3,
})

df.to_csv('data.csv')

print(df.to_string())