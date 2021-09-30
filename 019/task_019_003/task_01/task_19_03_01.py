family_member = {
    'info_user': {"name": "Jane", "surname": "Doe", "age": '35'}
}

family_member = {"hobbies":
    {
        1: "running",
        2: "sky diving",
        3: "singing"
    }
}

family_member = {
    "children": {
        1: {"name": "Alice", "age": '6'},
        2: {"name": "Bob", "age": '8'}}
}
print(family_member)
print(family_member['c'])
print(family_member['info_user']['name'])
# print("Bob", family_member.get('children').get(2).get('name'))
# print(family_member['children'])
# name_fio_b = ''
#
# for chil in family_member["children"].keys():
#     print(family_member["children"][chil]['name'])
#     if family_member["children"][chil]['name'] == 'Bob':
#
#         print(family_member['info_user'])
