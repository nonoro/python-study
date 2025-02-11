# # 결과
# {
#     "group1": [
#         {
#             "name": "Park",
#             "age": "32",
#             "sex": "Male"
#         },
#         {
#             "name": "Cho",
#             "age": "44",
#             "sex": "Female"
#         },
#         {
#             "name": "Kang",
#             "age": "39",
#             "sex": "Female",
#             "married": "No"
#         }
#     ],
#     "group2": [
#         {
#             "name": "Kim",
#             "age": "23",
#             "sex": "Male",
#             "married": "Yes"
#         },
#         {
#             "name": "Lee",
#             "age": "37",
#             "sex": "Male",
#             "married": "No"
#         }
#     ],
#     "type": {
#         "a": "employee",
#         "b": "officer",
#         "c": "director",
#         "d": "manager",
#         "e": "service provider"
#     }
# }
# ```
import json
import sys

d = {"group1":[
                {'name': 'Park', 'age': '32', 'sex': 'Male'},
                {'name': 'Cho', 'age': '44', 'sex': 'Female'},
                {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
    }

# dumps = json.dumps(d, indent=4)
# print(dumps)
# print(type(dumps))

with open('employee.json', 'w') as file:
    json.dump(obj =d, fp = file, indent=4)
