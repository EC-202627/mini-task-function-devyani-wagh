M = str(input())
N = int(input())

def calculate_fine(name, days):
    fine = float(days * 5)
    if fine > 150:
        fine = 150.0
    print(f"Book: {name}")
    print(f"Days overdue: {days}")
    print(f"Fine: Rs. {fine}")
    if fine == 150.0:
        print(f"You have accumulated the maximum fine of INR: {fine}")
    return fine

f = calculate_fine(M, N)
