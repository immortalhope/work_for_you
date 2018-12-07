
# Функція, що рекурсивно сумує елементи списку
def sum_list(data):
    if data == []:
        return 0
    return data[0]+sum_list(data[1:])

#Функція, що рекурсивно множить елементи списка
def mult_list(data, end_of_list):
    if end_of_list == 0:
        return 1
    return data[0]*mult_list(data[1:], end_of_list-1)
