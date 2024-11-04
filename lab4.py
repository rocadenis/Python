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

def main():
    # Testing Stack
    print("Testing Stack:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushes:", [stack.pop() for _ in range(3)])  # Expected: [3, 2, 1]
    stack.push(4)
    print("Peek:", stack.peek())  # Expected: 4
    print("Pop:", stack.pop())    # Expected: 4
    print("Pop empty stack:", stack.pop())  # Expected: None
    print()

    # Testing Queue
    print("Testing Queue:")
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print("Queue after pushes:", [queue.pop() for _ in range(3)])  # Expected: [1, 2, 3]
    queue.push(4)
    print("Peek:", queue.peek())  # Expected: 4
    print("Pop:", queue.pop())    # Expected: 4
    print("Pop empty queue:", queue.pop())  # Expected: None
    print()

    # Testing Matrix
    print("Testing Matrix:")
    matrix = Matrix(2, 3)
    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)
    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)
    print("Matrix:")
    for row in matrix.data:
        print(row)
    
    # Testing transpose
    transposed = matrix.transpose()
    print("Transposed Matrix:")
    for row in transposed.data:
        print(row)

    # Testing multiplication
    matrix_b = Matrix(3, 2)
    matrix_b.set(0, 0, 7)
    matrix_b.set(0, 1, 8)
    matrix_b.set(1, 0, 9)
    matrix_b.set(1, 1, 10)
    matrix_b.set(2, 0, 11)
    matrix_b.set(2, 1, 12)
    product = matrix.multiply(matrix_b)
    if product:
        print("Matrix Multiplication Result:")
        for row in product.data:
            print(row)
    else:
        print("Matrix dimensions incompatible for multiplication")

    # Testing apply with a lambda function
    print("Applying lambda function (increment by 1) to original matrix:")
    matrix.apply(lambda x: x + 1)
    for row in matrix.data:
        print(row)

if __name__ == "__main__":
    main()
