import numpy as np


class SimpleMatrix:
    def __init__(self, data):
        self.data = np.array(data)

    # Сложение
    def add(self, other_matrix):
        if self.data.shape != other_matrix.data.shape:
            print("Ошибка: размеры матриц не совпадают!")
            return None
        result = self.data + other_matrix.data
        return SimpleMatrix(result)

    # Умножение – покомпонентное
    def multiply(self, other_matrix):
        if self.data.shape != other_matrix.data.shape:
            print("Ошибка: размеры матриц не совпадают!")
            return None
        result = self.data * other_matrix.data
        return SimpleMatrix(result)

    # Умножение – Матричное
    def dot(self, other_matrix):
        if self.data.shape[1] != other_matrix.data.shape[0]:
            print("Ошибка: размеры матриц не подходят для матричного умножения!")
            return None
        result = np.dot(self.data, other_matrix.data)
        return SimpleMatrix(result)


# Уseed для воспроизводимости
np.random.seed(0)

# Генерация
matrix_a = SimpleMatrix(np.random.randint(0, 10, (10, 10)))
matrix_b = SimpleMatrix(np.random.randint(0, 10, (10, 10)))

# Выполнение
added_matrix = matrix_a.add(matrix_b)
multiplied_matrix = matrix_a.multiply(matrix_b)
dotted_matrix = matrix_a.dot(matrix_b)

# Сохранение
with open("artifacts/matrix+.txt", "w") as f:
    f.write(np.array2string(added_matrix.data))

with open("artifacts/matrix*.txt", "w") as f:
    f.write(np.array2string(multiplied_matrix.data))

with open("artifacts/matrix@.txt", "w") as f:
    f.write(np.array2string(dotted_matrix.data))
