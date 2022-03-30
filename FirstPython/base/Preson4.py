import pprint

preson4 ={'Ford': {'Name': 'Ford Prefect',
                   'Gender': 'Male',
                   'Occupation': 'Researcher',
                   'Home Planet': 'Betelgeuse Seven'},
          'Arthur': {'Name': 'Arthur Dent',
                     'Gender': 'Male'},
          'Robot': {'Name': 'Marvin',
                    'Occupation': 'Researcher'}}
pprint.pprint(preson4)

print(preson4['Ford']['Name'])


