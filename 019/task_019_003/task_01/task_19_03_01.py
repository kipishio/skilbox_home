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

family_member = {"name": "Jane", "surname": "Doe",}

family_member['hobbies'] = ["running", "sky diving", "singing"]

family_member['age'] = 35

family_member['children'] = [
    {"name": "Alice", "age": 6},
    {"name": "Bob", "age": 8}
]
print(family_member)
name_search = family_member.get('children')[1]['name']
print(name_search)

for name_count in family_member.get('children'):
    print(name_count['name'])
    if name_count.get('name') == 'Bob':
        print("Фамилия у {0} = {1}".format(name_count['name'], family_member['surname']))

