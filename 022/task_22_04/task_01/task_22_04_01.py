file_payment = open('numbers.txt', 'r', encoding='utf-8')
sum_ = 0

for i_elem in file_payment:
    sum_ += int(i_elem)

file_payment.close()

file_write = open('answer.txt', 'w')
file_write.write(str(sum_))
file_write.close()