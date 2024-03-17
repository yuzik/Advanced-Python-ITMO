import numpy as np

# Aрифметические операций


class ArithmeticMixin:
    def __add__(self, other):
        return SimpleMatrix(self.data + other.data)

    def __sub__(self, other):
        return SimpleMatrix(self.data - other.data)

    def __mul__(self, other):
        if isinstance(other, SimpleMatrix):
            return SimpleMatrix(self.data * other.data)
        else:
            return SimpleMatrix(self.data * other)

    def __matmul__(self, other):
        return SimpleMatrix(self.data @ other.data)

    def __truediv__(self, other):
        return SimpleMatrix(self.data / other.data)

# Ввод-вывод


class IOMixin:
    def save(self, filename):
        with open(filename, "w") as f:
            f.write(np.array2string(self.data))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            data = np.loadtxt(f)
        return SimpleMatrix(data)

# отображение


class DisplayMixin:
    def __str__(self):
        return np.array2string(self.data)

# getter и setter


class AccessorMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value)

# Основной класс, все примеси


class SimpleMatrix(ArithmeticMixin, IOMixin, DisplayMixin, AccessorMixin):
    def __init__(self, data):
        self.data = data  # Используется setter из AccessorMixin


# Генерация и выполнение
np.random.seed(0)
matrix1 = SimpleMatrix(np.random.randint(0, 10, (10, 10)))
matrix2 = SimpleMatrix(np.random.randint(0, 10, (10, 10)))

added_matrix = matrix1 + matrix2
multiplied_matrix = matrix1 * matrix2
dotted_matrix = matrix1 @ matrix2

# Сохранение
added_matrix.save("artifacts/matrix+.txt")
multiplied_matrix.save("artifacts//matrix*.txt")
dotted_matrix.save("artifacts//matrix@.txt")
