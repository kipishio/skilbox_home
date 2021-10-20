def create_dict(data, template=dict()):
    if isinstance(data, dict):
        return data

    if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        return {data: data}


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        if create_dict(i_element, old_list) is not None:
            new_list.append(create_dict(i_element, old_list))
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]

data = data_preparation(data)

print(data)

