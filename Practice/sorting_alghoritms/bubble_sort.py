def bubble_sort(sequence): #оголошуємо метод bubble_sort з аргументом sequence
    for counter in range(len(sequence)): #визначаємо довжину послідовності
        for index in range(len(sequence) - counter - 1): #для індексу в діапазоні довжини послідовності визначаємо рахувальник довжини -1
            if sequence[index] > sequence[index+1]: #створюємо умову якщо індекс більше індекса+1 значення,
                sequence[index], sequence[index+1] = sequence[index+1], sequence[index] #то, виводимо поточний індекс та наступний індекс зміщаємо на +1
        print(sequence) #виводимо проміжний результат
    return sequence #виконуємо результат

if __name__ == "__main__": #перевіряємо об'єкт локальний чи імпортований
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14] #значення до сортування
    print(bubble_sort(to_sort)) #виводимо результат

