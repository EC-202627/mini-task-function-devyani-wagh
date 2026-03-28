M = str(input())
N = int(input())
F = int(input())
X = int(input())


def calculate_fine(name, days, fine, due):
    fine = float(due)
    print(f"Book: {name}")
    print(f"Days overdue: {days}")
    print(f"Fine: Rs. {fine}")
    return fine

f = calculate_fine(M, N, F, X)
