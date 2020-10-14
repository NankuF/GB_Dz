with open('file3.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()

dictionary = {text[i][0:5]: text[i][5:11] for i in range(0, len(text))}
key_value = dictionary.items()
worker = []
worker_salary = []
for key, value in key_value:
    if int(value) < 20000:
        worker.append(key)
        worker_salary.append(value)

average_salary = ((int(worker_salary[0])) + (int(worker_salary[1]))) / 2
print(worker)
print(worker_salary)
print(average_salary)  # cредняя величина дохода 2х сотрудников с наименьшим доходом
