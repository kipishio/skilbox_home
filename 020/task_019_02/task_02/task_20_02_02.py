def S_cel(R, h) -> object:
    s_bok = 2 * 3.14 * R * h
    s_krug = 2 * (2 * 3.14 * R ** 2)
    s_cilindra = s_krug + s_bok
    return s_cilindra, s_bok


R = int(input('Укажите радиус окружности цилиндра: '))
h = int(input('Укажите высоту цилидра: '))

s_cilindra, s_cel_bok = S_cel(R, h)
print('площади боковой поверхности: {0}'.format(s_cel_bok))
print('площади цилиндра: {0}'.format(s_cilindra))



