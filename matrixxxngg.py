
import random

result = []
temp_row = []

def generate_number():
    return random.randint(1, 9)

def size_matrix1(rows, cols):
    matrix1 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(generate_number())
        matrix1.append(row)
    return matrix1

def size_matrix2(rows, cols):
    matrix2 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(generate_number())
        matrix2.append(row)
    return matrix2

while True:
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix1 = size_matrix1(rows, cols)
    matrix2 = size_matrix2(rows, cols)

    print("Матрица1:")
    for row in matrix1:
        print(row)

    print("Матрица2:")
    for row in matrix2:
        print(row)

    print("Выберите операцию над матрицами:")
    print("1. Сложить матрицы")
    print("2. Вычесть матрицы")
    print("3. Поделить матрицы")
    print("4. Умножить матрицы")
    sign = input("Введите знак операции:")

    if sign == "1":
        for i in range(rows):
            for j in range(cols):
                temp_row.append(matrix1[i][j] + matrix2[i][j])
            result.append(temp_row)
        for row in result:
            print(row)
            break

    elif sign == "2":
        for i in range(rows):
            for j in range(cols):
                temp_row.append(matrix1[i][j] - matrix2[i][j])
            result.append(temp_row)
        for row in result:
            print(row)
            break

    elif sign == "3":
        for i in range(rows):
            for j in range(cols):
                temp_row.append(matrix1[i][j] / matrix2[i][j])
            result.append(temp_row)
        for row in result:
            print(row)
            break

    elif sign == "4":
        for i in range(rows):
            for j in range(cols):
                temp_row.append(matrix1[i][j] * matrix2[i][j])
            result.append(temp_row)
        for row in result:
            print(row)
            break