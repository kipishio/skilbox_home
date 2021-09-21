word_user_list = input("Введите 3-и любых слова: ").split()
text = input("Введите текст в котором будет вестись поиск. ")

number = ''

word_count = ["-".join([word_user_list[i], str(text.count(word_user_list[i]))]) for i in range(len(word_user_list))]

for i in range(len(word_user_list)):
    number ="; ".join(word_count)

print(number)
