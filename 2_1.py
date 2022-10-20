input("Чтобы начать нажмите ENTER")
print()
SIZEA = int(input("Введите размер масcива A: "))
ARRAYA = [0] * SIZEA
SIZEB = int(input("Введите размер масcива B: "))
ARRAYB = [0] * SIZEB
print()
print("Выберите  K  если хотите ввести элементы для массива A с клавиатуры" )
print("Выберите  R  если хотите, чтоб элементы для массива A были сгенерированы рандомно в диапозоне от -999999 до 999999" )
CHOICEA = input("Введите K или R: ")
while CHOICEA != "K" and CHOICEA != "R":
    CHOICEA = input("Ошибка! Введите заглавные K или R: ")
else:
    if CHOICEA == "K":
        print("Хорошо!")
        print()
        for i in range(SIZEA):
            print("Введите элемент №", i + 1," для массива A:", sep="", end=" ")
            ARRAYA[i] = float(input())
    else:
        from random import uniform
        for i in range(SIZEA):
            ARRAYA[i] = uniform(-999999, 999999)
print()
print("Выберите  K  если хотите ввести элементы для массива B с клавиатуры" )
print("Выберите  R  если хотите, чтоб элементы для массива B были сгенерированы рандомно в диапозоне от -999999 до 999999" )
CHOICEB = input("Введите K или R: ")
while CHOICEB != "K" and CHOICEB != "R":
    CHOICEB = input("Ошибка! Введите заглавные K или R: ")
else:
    if CHOICEB == "K":
        print("Хорошо!")
        print()
        for j in range(SIZEB):
            print("Введите элемент №", j + 1," для массива B:", sep="", end=" ")
            ARRAYB[j] = float(input())
    else:
        from random import uniform
        for j in range(SIZEB):
            ARRAYB[j] = uniform(-999999, 999999)
print()
print("Принято! Сверьтесь всё ли верно?")
print()
print("Размера массива A:", SIZEA)
print("Mассив A:", ARRAYA)
print()
print("Размера массива B:", SIZEB)
print("Mассив B:", ARRAYB)
print()
input("Нажмите ENTER")
K = 0
X = ""
for i in range(SIZEA):
    for j in range(SIZEB):
        if ARRAYA[i] <= ARRAYB[j]:
            if ARRAYA[i] == ARRAYB[j]:
                K = K + 1
                X = X + str(ARRAYA[i]) + " ; "
        else:
            if ARRAYB[j] == ARRAYA[i]:
                K = K + 1
                X = X + str(ARRAYB[j]) + " ; "
print()
if K != 0:
    print("Найдено общих эементов:", K)
    print("Общие элементы: ", X, sep="")
else:
    print("Общих элементов не найдено")
print()
input("Чтобы завершить нажмите ENTER")