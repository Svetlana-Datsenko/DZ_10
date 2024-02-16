# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data)

def check_robot(element):
    if element == 'robot': 
        return 1
    else: 
        return 0

robot_lst = list(map(check_robot, lst))
print(robot_lst)

data_new = pd.DataFrame({'robot':robot_lst,'human': map(lambda x: (x + 1) % 2, robot_lst)})
data_new.head(n = 20)
print(data_new)