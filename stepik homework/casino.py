a = int(input())

pocket_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pocket_2 = [11, 12, 13, 14, 15, 16, 17, 18]
pocket_3 = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
pocket_4 = [29, 30, 31, 32, 33, 34, 35, 36]

if a % 2 == 0 and a in pocket_1:
    print('черный')
else:
    if a % 2 == 1 and a in pocket_2:
        print('черный')
    else:
        if a % 2 == 0 and a in pocket_3:
            print('черный')
        else:
            if a % 2 == 1 and a in pocket_4:
                print('черный')
            else:
                if a == 0:
                    print('зеленый')
                else:
                    if a >= 37 or a <= -1:
                        print('ошибка ввода')
                    else:
                        print('красный')