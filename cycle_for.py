car_list_1 = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
for i in range(len(car_list_1)):
    print('I drive a', car_list_1[i], 'car')

car_list_2 = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
cars_count = 0
for i in range(len(car_list_2)):
    cars_count += 10
print('I drive a', car_list_2[i], 'car', cars_count)
