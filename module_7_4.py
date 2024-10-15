team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1862.51
team2_time = 2253.41
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %
print('В команде Мастера кода участников: %(name)s!' % {'name': team1_num})
print('Итого сегодня в командах участников: %(name1)s и %(name2)s!' % {'name1': team1_num, 'name2': team2_num})

# Использование `format()`
print("Команда Волшебники данных решила задач: {score_2} !".format(score_2=score_2))
print("Волшебники данных решили задачи за {} с !".format(team2_time))

# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')

# Расчет среднего времени
average_time = round(sum([team1_time, team2_time]) / float(tasks_total), 2)
print(f"Сегодня было решено {tasks_total} задач, в среднем по {average_time} секунд на задачу!")