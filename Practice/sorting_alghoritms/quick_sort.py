def quick_sort(sequence): #визначаємо метод
    if len(sequence) <= 1: #цикл з умовою
        return sequence #проміжний результат

    pivot = sequence[0] #присвоєння значаень
    left = [element for element in sequence[1:] if element < pivot]
    #цикл для лівого елементу = елемент як елемент в послідовності +1,
    #наступна умова якщо елемент менше півот
    right = [element for element in sequence[1:] if element >= pivot]
    #цикл для правого елементу, елемент як елемент в послідовності +1, умова
    #якщо елемент більше або дорівнює півот
    return quick_sort(left) + [pivot] + quick_sort(right) #проміжний результат


if __name__ == "__main__": #перевіряємо чи файл імпортований чи локальний
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14] #дані до сортування
    print(quick_sort(to_sort)) #результат