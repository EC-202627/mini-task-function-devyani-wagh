book = input()
days = int(input())

fine = days * 5

if fine > 150:
    fine = 150
    print(f"Book: {book} Days overdue: {days} Fine: Rs. {float(fine)}")
    print(f"You have accumulated the maximum fine of INR: {float(fine)}")
else:
    print(f"Book: {book} Days overdue: {days} Fine: Rs. {float(fine)}")
