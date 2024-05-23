team1 = '"Мастера Кода"'
team2 = '"Волшебники Данных"'
team1_num = 11
team2_num = 14
score_1 = 10
score_2 = 8
team1_time = 1587
team2_time = 1411
task_total = score_1 + score_2
time_avg = (team1_time + team2_time) / task_total


# примеры с %s

print('В команде %s %s участников!' %(team1, team1_num))

print('*'*40)

print('Итого сегодня в командах %s и %s участников!' %(team1_num, team2_num))

print('*'*40)

# примеры с format()


print('Команда {} решила {} задач!'.format(team2, score_2))

print('*'*40)

print('Время, за которое команда {} решила {} задач - {} секунд!'.format(team2, score_2, team2_time))

print('*'*40)

# примеры с f-строкой

print(f'Команды решили {score_1} и {score_2} задач')

print('*'*40)

challenge_res = max(score_1, score_2)
if challenge_res == score_1:
    print(f'Результат битвы: победа команды {team1}')
else:
    print(f'Результат битвы: победа команды {team2}')

print('*'*40)

print(f'В сегодняшней битве было решено {task_total} задач, со средним временем {time_avg} секунд на 1 задачу')