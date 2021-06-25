count_worker = int(input("Кол-во сотрудников в офисе: "))
list_worker_id = []

for _ in range(count_worker):
    id_worker = int(input("ID сотрудника: "))
    list_worker_id.append(id_worker)

search_id_worker = int(input("Какой ID ищем?: "))

if search_id_worker in list_worker_id:
    print("Сотрудник на месте")
else:
    print("Сотрудник не работает")



