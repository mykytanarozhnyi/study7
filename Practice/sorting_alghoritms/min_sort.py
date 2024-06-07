def min_sort(sequence): #визначаємо метод
    result = list() #результат будемо виводити у лист
    for counter in range(len(sequence)): #визначаємо цикл
        min_element = min(sequence) #умова цикла
        index_of_min = sequence.index(min_element) #друга умова
        sequence.pop(index_of_min) #видаляємо індекс оф мін
        result.append(min_element) #додаэмо результат
        # result.append(sequence.pop(sequence.index(min(sequence))))
    return result #повертаємо проміжний результат

if __name__ == "__main__": #перевірка чи файл локальний чи імпортований
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14] #дані до сортування
    print(min_sort(to_sort)) #виводимо результат
