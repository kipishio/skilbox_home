# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }

family_member = {"name": "Jane", "surname": "Doe"}

family_member['hobbies'] = ["running", "sky diving", "singing"]

family_member['age'] = 35

family_member['children'] = [
    {"name": "Alice", "age": 6},
    {"name": "Bob", "age": 8}
]
print(family_member)

fam = ''
for name_count in family_member.get('children'):
    for imya in name_count:
        if name_count[imya] == 'Bob':
            print('Имя {0}'.format(name_count[imya]))
            fam = family_member.get('surname', 'Nosurname')

print("Фамилия {0}".format(fam))

