print('Толстуха Надія, КМ-82\nВаріант 23. Завдання 1.\nСформувати в програмі масив з цілих чисел від 2 до n. Підрахувати суму квадpатов парних і суму квадратів непарних чисел.')
correct = False
while not correct:
    paired = []
    unpaired = []
    while True:
        try:
            n = int(input("Введіть число n. \nn="))
            break
        except ValueError:
            print("Введіть коректні дані.")

    num = 2
    def divide(num, n, paired, unpaired):
        if num > n:
            return paired, unpaired
        if num %2==0:
            paired.append(num)
        else:
            unpaired.append(num)
        return divide(num+1, n, paired, unpaired)
    print (divide(num, n, paired, unpaired))
    squares_paired = []
    for elm in paired:
        number = elm**2
        squares_paired.append(number)
    squares_unpaired = []
    for elm in unpaired:
        number = elm**2
        squares_unpaired.append(number)
    sum = 0
    for elm in squares_paired:
        sum += elm
    print ("Сума квадратів парних чисел:", sum)
    sum = 0
    for elm in squares_unpaired:
        sum += elm
    print ("Сума квадратів непарних чисел:", sum)
    choice = input("Якщо хочете завершити програму - натисніть 1, а якщо повторити - будь-що.\n")
    if choice == "1":
        correct = True
    else:
        correct = False
