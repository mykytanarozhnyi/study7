def choice_sort(sequence): #визначаємо метод з аргументом sequence
    def get_max_index(): #визначаємо метод
        max_index = 0 #визначаємо атрибут методу та його значення на 0
        for index in range(right_bound + 1): #цикл for in в довжіні правого крила та додаємо по +1
            if sequence[max_index] < sequence[index]: #умова якщо послідовність max_index менше індекс то макс індекс дорівнює індексу
                max_index = index
        return max_index #запускаємо на виконання

    right_bound = len(sequence) - 1 #праве крило дорівнює довжині послідовності та -1
    while right_bound > 1: #умова: поки праве крило більше ніж 1, макс індекс дорівнює функції гет макс індекс()
        max_index = get_max_index()
        sequence[right_bound], sequence[max_index] = sequence[max_index], sequence[right_bound] #визначаэмо що послідовність правого крила, та послідовність максимального індексу дорівнює ним же тільки поміняним місцями
        right_bound -= 1 #при кожному проході віднімаємо 1 від правого крила
        print(sequence) #виводимо проміжний результат
    return sequence #запускаємо виконання


if __name__ == "__main__": #перевіряємо об'єкт локальний чи імпортований
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14] #значення до сортування
    print(choice_sort(to_sort)) #виводимо результат