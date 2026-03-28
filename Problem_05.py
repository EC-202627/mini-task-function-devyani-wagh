book = input()
days = int(input())
rate = float(input())
max_fine = float(input())

fine = days * rate

if fine > max_fine:
    fine = max_fine

print(f"Book: {book} Days overdue: {days} Fine: Rs. {float(fine)}")
