# Problem 1: Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

# Problem 2: Queue
class Queue:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop(0) if self.items else None

    def peek(self):
        return self.items[0] if self.items else None

# Problem 3: Matrix
class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[0] * m for _ in range(n)]

    def set(self, x, y, value):
        if 0 <= x < self.n and 0 <= y < self.m:
            self.data[x][y] = value
            return True
        return False

    def get(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.m:
            return self.data[x][y]
        return None

    def transpose(self):
        transposed_matrix = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed_matrix.set(j, i, self.data[i][j])
        return transposed_matrix

    def multiply(self, matrix):
        if self.m != matrix.n:
            return None  # Matrices cannot be multiplied

        result_matrix = Matrix(self.n, matrix.m)
        for i in range(self.n):
            for j in range(matrix.m):
                result_matrix.data[i][j] = sum(
                    self.data[i][k] * matrix.data[k][j] for k in range(self.m)
                )
        return result_matrix

    def apply(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.data[i][j] = func(self.data[i][j])
