import numpy as np


class HashMixin:
    def __hash__(self):
        # Хэш-функция, которая суммирует все элементы матрицы
        # и возвращает хэш этой суммы.
        return hash(np.sum(self.data))


class ArithmeticMixin:
    def __add__(self, other):
        return Matrix(self.data + other.data)

    def __sub__(self, other):
        return Matrix(self.data - other.data)

    def __mul__(self, other):
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        return Matrix(np.dot(self.data, other.data))

    def __truediv__(self, other):
        return Matrix(self.data / other.data)


class IOMixin:
    def save(self, filename):
        np.savetxt(filename, self.data, fmt="%d")

    @staticmethod
    def load(filename):
        data = np.loadtxt(filename, dtype=int)
        return Matrix(data)


class DisplayMixin:
    def __str__(self):
        return np.array2string(self.data)


class AccessorMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value)


class Matrix(ArithmeticMixin, IOMixin, DisplayMixin, AccessorMixin, HashMixin):
    def __init__(self, data):
        self.data = data


class MatrixProductCache:
    def __init__(self):
        self.cache = {}

    def multiply_and_cache(self, matrix_a, matrix_b):
        hash_key = hash(matrix_a) ^ hash(matrix_b)
        if hash_key in self.cache:
            return self.cache[hash_key]
        else:
            result = matrix_a @ matrix_b
            self.cache[hash_key] = result
            return result


# Поиск коллизии
cache = MatrixProductCache()
found = False
for seed in range(10000):
    np.random.seed(seed)
    A = Matrix(np.random.randint(0, 10, (2, 2)))
    B = Matrix(np.random.randint(0, 10, (2, 2)))
    C = Matrix(np.random.randint(0, 10, (2, 2)))
    D = B  # B == D

    if hash(A) == hash(C) and not np.array_equal(A.data, C.data) and not np.array_equal(A @ B, C @ D):
        A.save("artifacts/A.txt")
        B.save("artifacts/B.txt")
        C.save("artifacts/C.txt")
        D.save("artifacts/D.txt")
        AB = cache.multiply_and_cache(A, B)
        CD = cache.multiply_and_cache(C, D)
        AB.save("artifacts/AB.txt")
        CD.save("artifacts/CD.txt")
        with open("artifacts/hash.txt", "w") as f:
            f.write(str(hash(AB)))
        found = True
        break

if found:
    print("Коллизия найдена. Seed:", seed)
else:
    print("Коллизия не найдена.")
