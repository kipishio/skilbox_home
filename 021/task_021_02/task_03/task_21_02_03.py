site = {

    'html': {

        'head': {

            'title': 'Мой сайт'

        },

        'body': {

            'h2': 'Здесь будет мой заголовок',

            'div': 'Тут, наверное, какой-то блок',

            'p': 'А вот здесь новый абзац'

        }

    }

}


def poisk(key, data_dict):
    if key in data_dict:
        return data_dict[key]

    for i_key in data_dict.values():
        if isinstance(i_key, dict):
            result = poisk(key, i_key)
            if result:
                break
    else:
        result = None
    return result





search = input('Искомый ключ: ')
print(poisk(search, site))
