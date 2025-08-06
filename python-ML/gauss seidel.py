class GaussSeidelSolver:
    def __init__(self, A, b, tolerance=1e-10, max_iterations=100):
        self.A = A
        self.b = b
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def solve(self):
        n = len(self.A)
        x = [0 for _ in range(n)]
        for itr in range(self.max_iterations):
            x_new = x.copy()
            for i in range(n):
                s1 = sum(self.A[i][j] * x_new[j] for j in range(i))
                s2 = sum(self.A[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = (self.b[i] - s1 - s2) / self.A[i][i]
            if all(abs(x_new[i] - x[i]) < self.tolerance for i in range(n)):
                return x_new 
            x = x_new
        return x

A = [
    [4, 1, 2],
    [3, 5, 1],
    [1, 1, 3]
]
b = [4, 7, 3]
solver = GaussSeidelSolver(A, b)
solution = solver.solve()
print("Solution:", solution)
print("Expected:", [1, 1, 1])  


