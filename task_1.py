#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
#который должен принимать данные (список списков) для формирования матрицы.
#[[], [], []]
#Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add()__ для реализации операции
#сложения двух объектов класса Matrix (двух матриц).
#Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно —
#первый элемент первой строки первой матрицы складываем
#с первым элементом первой строки второй матрицы и т.д.



class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        for row in self.my_matrix:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ""

    def __add__(self, other):
        for i in range(len(self.my_matrix)):
            for i_2 in range(len(other.my_matrix[i])):
                self.my_matrix[i][i_2] = self.my_matrix[i][i_2] + other.my_matrix[i][i_2]
        return Matrix.__str__(self)


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
new_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(matrix.__add__(new_matrix))
