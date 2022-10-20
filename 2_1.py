input("Чтобы начать нажмите ENTER")
print()
SIZEA = int(input("Введите размер масcива A: "))
ARRAYA = [0] * SIZEA
SIZEB = int(input("Введите размер масcива B: "))
ARRAYB = [0] * SIZEB
def explanations (LETTER):
    print()
    print("Выберите  K  если хотите ввести элементы для массива", LETTER, "с клавиатуры")
    print("Выберите  R  если хотите, чтоб элементы для массива", LETTER, "были сгенерированы рандомно в диапозоне от -999999 до 999999")
def chekc (CHOICE, ARRAY, SIZE, LETTER):
    while CHOICE != "K" and CHOICE != "R":
        CHOICE = input("Ошибка! Введите заглавные K или R: ")
    else:
        if CHOICE == "K":
            print("Хорошо!")
            print()
            for i in range(SIZE):
                print("Введите элемент №", i + 1, " для массива ", LETTER, ":", sep="", end=" ")
                ARRAY[i] = float(input())
        else:
            from random import uniform
            for i in range(SIZEA):
                ARRAY[i] = uniform(-999999, 999999)
    return (ARRAY)
explanations ("A")
CHOICEA = input("Введите K или R: ")
chekc (CHOICEA, ARRAYA, SIZEA, "A")
explanations ("B")
CHOICEB = input("Введите K или R: ")
chekc (CHOICEB, ARRAYB, SIZEB, "B")
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
ARRAYN = ""
for i in range(SIZEA):
    for j in range(SIZEB):
        if ARRAYA[i] < ARRAYB[j]:
            if ARRAYA[i] == ARRAYB[j]:
                K = K + 1
                ARRAYN = ARRAYN + str(ARRAYA[i]) + " "
        else:
            if ARRAYB[j] == ARRAYA[i]:
                K = K + 1
                ARRAYN = ARRAYN + str(ARRAYB[j]) + " "
print()
if K != 0:
    print("Найдено общих эементов:", K)
    print("Общие элементы:", ARRAYN)
else:
    print("Общих элементов не найдено")
print()
input("Чтобы завершить нажмите ENTER")