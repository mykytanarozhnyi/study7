def insertion_sort(sequence): #визначаємо метод з аргументом
    for index in range(1, len(sequence)): #створюємо цикл де перебераємо по 1 по всій довжині послідовності
        position = index - 1 #визначаємо стандартне значення
        value = sequence[index] #визначаємо значення
        while position >= 0 and sequence[position] > value: #другий цикл з умовою
            sequence[position + 1] = sequence[position] #умова
            position -= 1 #друга умова
        sequence[position + 1] = value #очікуваннй результат
        print(sequence) #виводимо проміжний результат
    return sequence #виконання

if __name__ == "__main__": #перевірка чи нейм є локальним чи імпортованим
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    print(insertion_sort(to_sort)) #результат